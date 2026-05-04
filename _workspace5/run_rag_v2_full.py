"""
New_RAG v2 - 전체 3352개 공구명 표준화 (GPU 최적화 버전)
실행: /home/neohc/miniconda3/bin/python run_rag_v2_full.py [모델명]
GPU 최적화:
  - sentence-transformers: CUDA 디바이스 사용
  - 3352개 쿼리 임베딩을 루프 전 일괄 배치 처리 (건당 encode 제거)
  - ollama: 이미 100% GPU 사용
"""

import ollama
import json
import pandas as pd
import re
import sys
import time
import numpy as np

# 실시간 출력 (stdout 버퍼링 해제)
sys.stdout.reconfigure(line_buffering=True)
from datetime import timedelta
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')

import torch
import faiss
from sentence_transformers import SentenceTransformer

# ===== GPU 확인 =====
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
if DEVICE == 'cuda':
    print(f"GPU 사용: {torch.cuda.get_device_name(0)} "
          f"(VRAM {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f}GB)")
else:
    print("GPU 없음 - CPU 사용")

# ===== 설정 =====
BASE = '/mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5/'
TOOL_DATA_PATH    = BASE + 'ToolNameData.csv'
GROUND_TRUTH_PATH = BASE + 'standard_tool_names_ground_truth_v2.csv'
OUTPUT_DIR        = BASE

# 커맨드라인 인수로 모델 지정 가능: python run_rag_v2_full.py deepseek-r1:8b
if len(sys.argv) > 1:
    MODEL_NAME = sys.argv[1]
else:
    MODEL_NAME = 'deepseek-r1:8b'

MODEL_SAVE_NAME = MODEL_NAME.replace(':', '_').replace('/', '_').replace('.', '_')
K_VALUE = 5
TEST_N  = None  # None = 전체 실행

print(f"모델: {MODEL_NAME} | 실행 범위: {TEST_N or '전체'} 행\n")

# ===== 데이터 로드 =====
df_tool = pd.read_csv(TOOL_DATA_PATH)
df_gt   = pd.read_csv(GROUND_TRUTH_PATH)
print(f"ToolNameData: {df_tool.shape} | Ground Truth: {df_gt.shape}")

# RAG 지식 베이스: standard_name / brand / power_source 목록만 사용 (original_name 제외)
STANDARD_NAMES = df_gt['standard_name'].dropna().unique().tolist()
BRANDS         = df_gt['brand'].dropna().unique().tolist()
POWER_SOURCES  = df_gt['power_source'].dropna().unique().tolist()
print(f"표준 공구명: {len(STANDARD_NAMES)}종 | 브랜드: {len(BRANDS)}종 | 전원방식: {len(POWER_SOURCES)}종")

# ===== GPU 임베딩 모델 + FAISS Vector DB 구축 =====
t0 = time.time()
print(f"\n[1/3] 임베딩 모델 로드 (device={DEVICE})...")
embed_model = SentenceTransformer(
    'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2',
    device=DEVICE
)

print(f"[2/3] 표준 공구명 {len(STANDARD_NAMES)}개 Vector DB 구축...")
std_vectors = embed_model.encode(STANDARD_NAMES, show_progress_bar=True,
                                  batch_size=64, convert_to_numpy=True)
dim = std_vectors.shape[1]
faiss_index = faiss.IndexFlatL2(dim)
faiss_index.add(std_vectors.astype('float32'))
print(f"      FAISS DB 완료 (d={dim})")

# ===== 핵심 최적화: 전체 쿼리 임베딩 일괄 처리 =====
df_run = df_tool.copy() if TEST_N is None else df_tool.head(TEST_N).copy()
tool_names = df_run['Original_Name'].fillna('').astype(str).tolist()

print(f"[3/3] 쿼리 {len(tool_names)}개 일괄 임베딩 (GPU 배치)...")
query_vectors = embed_model.encode(tool_names, show_progress_bar=True,
                                    batch_size=256, convert_to_numpy=True)

# FAISS 일괄 검색 (3352개 × top-k 한 번에)
_, all_indices = faiss_index.search(query_vectors.astype('float32'), K_VALUE)
t_embed = time.time() - t0
print(f"임베딩 + FAISS 검색 완료: {t_embed:.1f}초\n")

# ===== 프롬프트 =====
PROMPT_TEMPLATE = """당신은 한국어 하드웨어 공구 이름 분류 전문가입니다.
정제되지 않은 공구 이름을 분석하여 아래 목록에서 가장 적합한 표준 정보를 추출하세요.

[표준 공구명 후보 (유사도 상위 {k}개)]
{standard_name_candidates}

[브랜드 목록] (없으면 null)
{brand_list}

[전원 방식 목록] (없으면 null)
{power_source_list}

규칙:
- standard_name은 반드시 위 '표준 공구명 후보' 중 하나를 선택하세요.
- brand/power_source는 각 목록 중 하나이거나 null.
- specification은 규격·크기 등 기타 사양 (없으면 null).

JSON 형식으로만 응답:
{{
  "standard_name": "표준 공구명",
  "brand": null,
  "power_source": null,
  "specification": null
}}

입력 공구 이름: '{tool_name}'
출력:"""

# qwen3 thinking 모델: format='json' 사용 시 빈 응답 반환 → 별도 처리
IS_QWEN3 = 'qwen3' in MODEL_NAME.lower()

# ===== LLM 호출 함수 (임베딩은 이미 사전 계산됨) =====
def call_llm(tool_name, candidates):
    prompt = PROMPT_TEMPLATE.format(
        k=K_VALUE,
        standard_name_candidates='\n'.join(f'  - {c}' for c in candidates),
        brand_list=', '.join(BRANDS),
        power_source_list=', '.join(POWER_SOURCES),
        tool_name=str(tool_name).strip()
    )
    try:
        if IS_QWEN3:
            resp = ollama.generate(
                model=MODEL_NAME, prompt=prompt,
                stream=False, options={"temperature": 0, "num_predict": 3000}
            )
            text = resp.get('response', '{}')
            text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()
            m = re.search(r'\{[^{}]*\}', text, re.DOTALL)
            text = m.group(0) if m else '{}'
        else:
            resp = ollama.generate(
                model=MODEL_NAME, prompt=prompt,
                format='json', stream=False,
                options={"temperature": 0, "num_predict": 800}
            )
            text = resp.get('response', '{}')
            text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()
        parsed = json.loads(text)

        if parsed.get('standard_name') not in STANDARD_NAMES:
            parsed['standard_name'] = candidates[0]
            parsed['fallback_used'] = True
        else:
            parsed['fallback_used'] = False

        return {'status': 'success', 'data': parsed}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

# ===== 실행 (진행률 + 속도 측정 포함) =====
total = len(tool_names)
print(f"--- LLM 처리 시작: {total}개 ({MODEL_NAME}) ---\n")

results = []
t_llm_start = time.time()
report_interval = max(1, total // 20)  # 5%마다 중간 보고

for i, (tool_name, idx_row) in enumerate(zip(tool_names, all_indices)):
    candidates = [STANDARD_NAMES[j] for j in idx_row]
    r = call_llm(tool_name, candidates)

    entry = {
        'Input_Name':     tool_name,
        'status':         r['status'],
        'rag_top1':       candidates[0],
        'rag_candidates': ', '.join(candidates)
    }
    if r['status'] == 'success':
        d = r['data']
        entry['standard_name'] = d.get('standard_name')
        entry['brand']         = d.get('brand')
        entry['power_source']  = d.get('power_source')
        entry['specification'] = d.get('specification')
        entry['fallback_used'] = d.get('fallback_used', False)
    else:
        entry['error_message'] = r.get('message')
    results.append(entry)

    # 진행률 출력 (5%마다 + 마지막)
    done = i + 1
    if done % report_interval == 0 or done == total:
        elapsed   = time.time() - t_llm_start
        pct       = done / total * 100
        speed     = done / elapsed          # 건/초
        eta_sec   = (total - done) / speed if speed > 0 else 0
        eta_str   = str(timedelta(seconds=int(eta_sec)))
        print(f"  [{pct:5.1f}%] {done:4d}/{total}건 | "
              f"속도: {speed:.2f}건/초 | "
              f"경과: {str(timedelta(seconds=int(elapsed)))} | "
              f"남은시간: {eta_str}")

t_llm_total = time.time() - t_llm_start
df_results = pd.DataFrame(results)

# ===== 속도 요약 =====
print(f"\n{'='*55}")
print(f"  모델         : {MODEL_NAME}")
print(f"  처리 건수     : {total}개")
print(f"  임베딩 시간   : {t_embed:.1f}초 (GPU 배치, {len(STANDARD_NAMES)}종 DB + {total}개 쿼리)")
print(f"  LLM 추론 시간 : {str(timedelta(seconds=int(t_llm_total)))}")
print(f"  평균 속도     : {total/t_llm_total:.2f}건/초")
print(f"  총 소요 시간  : {str(timedelta(seconds=int(t_embed + t_llm_total)))}")
print(f"{'='*55}\n")

# ===== 평가 =====
gt_map = df_gt.set_index('original_name')['standard_name'].to_dict()
df_results['gt_standard_name'] = df_results['Input_Name'].map(gt_map)

def check_correct(row):
    if pd.isna(row.get('gt_standard_name')):
        return None
    return str(row.get('standard_name', '')).strip() == str(row['gt_standard_name']).strip()

df_results['is_correct'] = df_results.apply(check_correct, axis=1)

evaluatable = df_results[df_results['gt_standard_name'].notna()]
print(f"=== 평가 결과 ({MODEL_NAME}) ===")
print(f"전체 처리: {len(df_results)}개 | 정답 존재: {len(evaluatable)}개")
if len(evaluatable) > 0:
    correct = (evaluatable['is_correct'] == True).sum()
    fallback = df_results.get('fallback_used', pd.Series([False]*len(df_results))).sum()
    print(f"정확도    : {correct}/{len(evaluatable)} = {correct/len(evaluatable):.2%}")
    print(f"Fallback  : {fallback}건 ({fallback/len(df_results)*100:.1f}%)")

# ===== 저장 =====
n_label = len(df_results)
# 모델명 원본 보존용 컬럼 추가 (리포트에서 정확한 모델명 복원)
df_results.insert(0, 'model_name', MODEL_NAME)
save_path = OUTPUT_DIR + f'New_RAG_v2_{MODEL_SAVE_NAME}_{n_label}.csv'
df_results.to_csv(save_path, index=False, encoding='utf-8-sig')

# stats JSON 저장 (리포트 속도 정보용)
import json as _json
stats = {
    'model_name':       MODEL_NAME,
    'total':            n_label,
    'embed_sec':        round(t_embed, 1),
    'llm_sec':          round(t_llm_total, 1),
    'total_sec':        round(t_embed + t_llm_total, 1),
    'speed_per_sec':    round(total / t_llm_total, 2),
    'eval_count':       int(len(evaluatable)),
    'correct':          int(correct) if len(evaluatable) > 0 else 0,
    'accuracy':         round(correct / len(evaluatable), 4) if len(evaluatable) > 0 else 0,
    'fallback_rate':    round(fallback / n_label, 4),
    'error_rate':       round((df_results['status'] == 'error').mean(), 4)
                        if 'status' in df_results.columns else 0,
}
stats_path = OUTPUT_DIR + f'New_RAG_v2_{MODEL_SAVE_NAME}_stats.json'
with open(stats_path, 'w', encoding='utf-8') as f:
    _json.dump(stats, f, ensure_ascii=False, indent=2)

print(f"\n결과 저장: {save_path}")
print(f"Stats 저장: {stats_path}")
print("완료.")
