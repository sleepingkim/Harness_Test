"""
New_RAG v2 Improved - 4가지 개선 적용 버전
실행: /home/neohc/miniconda3/bin/python -u run_rag_v2_improved.py [모델명]

개선 사항 (기본 버전 대비):
  1. 임베딩 모델 교체: MiniLM-L12 → dragonkue/BGE-m3-ko (한국어 KURE 리더보드 1위)
  2. BM25 + FAISS 하이브리드 검색 (한국어 음절 bigram 토크나이저)
  3. k값 확대: 5 → 15
  4. 카테고리/서브카테고리 프롬프트 주입 (ToolNameData의 SubCategories, Categories 활용)
"""

import os
import ollama
import json
import pandas as pd
import re
import sys
import time
import numpy as np
from datetime import timedelta
from rank_bm25 import BM25Okapi
import warnings
warnings.filterwarnings('ignore')

import torch
import faiss
from sentence_transformers import SentenceTransformer

sys.stdout.reconfigure(line_buffering=True)

# ===== GPU 확인 =====
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
if DEVICE == 'cuda':
    print(f"GPU: {torch.cuda.get_device_name(0)} "
          f"(VRAM {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f}GB)")
else:
    print("GPU 없음 - CPU 사용")

# ===== 설정 =====
BASE              = '/mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5/'
TOOL_DATA_PATH    = BASE + 'ToolNameData.csv'
GROUND_TRUTH_PATH = BASE + 'standard_tool_names_ground_truth_v2.csv'
OUTPUT_DIR        = BASE

# 개선 1: 한국어 특화 임베딩 모델
EMBED_MODEL_NAME = 'dragonkue/BGE-m3-ko'

MODEL_NAME = sys.argv[1] if len(sys.argv) > 1 else 'deepseek-r1:8b'
MODEL_SAVE_NAME = MODEL_NAME.replace(':', '_').replace('/', '_').replace('.', '_')
RESUME = '--resume' in sys.argv

# 개선 3: k값 확대
K_VALUE = 15
# BM25 가중치 (0=순수 FAISS, 1=순수 BM25, 0.4=BM25 40% + FAISS 60%)
BM25_ALPHA = 0.4

TEST_N = None

print(f"\n모델: {MODEL_NAME}")
print(f"임베딩: {EMBED_MODEL_NAME}")
print(f"K값: {K_VALUE} | BM25 가중치: {BM25_ALPHA}\n")

# ===== 데이터 로드 =====
df_tool = pd.read_csv(TOOL_DATA_PATH)
df_gt   = pd.read_csv(GROUND_TRUTH_PATH)
print(f"ToolNameData: {df_tool.shape} | Ground Truth: {df_gt.shape}")

STANDARD_NAMES = df_gt['standard_name'].dropna().unique().tolist()
BRANDS         = df_gt['brand'].dropna().unique().tolist()
POWER_SOURCES  = df_gt['power_source'].dropna().unique().tolist()
print(f"표준 공구명: {len(STANDARD_NAMES)}종 | 브랜드: {len(BRANDS)}종 | 전원방식: {len(POWER_SOURCES)}종")

# ===== 개선 2: BM25 지식 베이스 구축 (한국어 음절 bigram) =====
def tokenize_ko(text: str) -> list:
    """한국어 공구명 음절 unigram + bigram 토크나이저"""
    text = re.sub(r'[^가-힣a-zA-Z0-9]', ' ', str(text)).strip()
    tokens = []
    for word in text.split():
        if not word:
            continue
        tokens.extend(list(word))                                  # 음절 unigram
        tokens.extend([word[i:i+2] for i in range(len(word)-1)])   # 음절 bigram
    return tokens if tokens else [text]

print("\n[1/4] BM25 지식 베이스 구축...")
bm25_corpus = [tokenize_ko(name) for name in STANDARD_NAMES]
bm25_index  = BM25Okapi(bm25_corpus)
print(f"      BM25 완료 ({len(STANDARD_NAMES)}개 문서)")

# ===== 개선 1: 한국어 특화 임베딩 모델 + FAISS =====
t0 = time.time()
print(f"[2/4] 임베딩 모델 로드 ({EMBED_MODEL_NAME}, device={DEVICE})...")
embed_model = SentenceTransformer(EMBED_MODEL_NAME, device=DEVICE)

print(f"[3/4] 표준 공구명 {len(STANDARD_NAMES)}개 FAISS Vector DB 구축...")
std_vectors = embed_model.encode(
    STANDARD_NAMES, show_progress_bar=True, batch_size=64, convert_to_numpy=True
)
dim = std_vectors.shape[1]
faiss_index = faiss.IndexFlatL2(dim)
faiss_index.add(std_vectors.astype('float32'))
print(f"      FAISS 완료 (d={dim})")

# ===== 전체 쿼리 임베딩 일괄 처리 =====
df_run     = df_tool.copy() if TEST_N is None else df_tool.head(TEST_N).copy()
tool_names = df_run['Original_Name'].fillna('').astype(str).tolist()

print(f"[4/4] 쿼리 {len(tool_names)}개 일괄 임베딩 (GPU 배치)...")
query_vectors = embed_model.encode(
    tool_names, show_progress_bar=True, batch_size=256, convert_to_numpy=True
)

# FAISS 일괄 검색: 160개 전체 거리 반환 (하이브리드 혼합에 필요)
print("      FAISS 전체 거리 계산 중...")
all_distances, all_faiss_indices = faiss_index.search(
    query_vectors.astype('float32'), len(STANDARD_NAMES)
)

t_embed = time.time() - t0
print(f"임베딩 + FAISS 완료: {t_embed:.1f}초\n")

# ===== 개선 2: 하이브리드 검색 함수 =====
def hybrid_search(tool_name: str, query_idx: int, k: int = K_VALUE) -> list:
    """BM25(alpha) + FAISS(1-alpha) 하이브리드 → top-k 표준 공구명 반환"""
    # BM25 점수
    tokens     = tokenize_ko(tool_name)
    bm25_raw   = np.array(bm25_index.get_scores(tokens))
    bm25_max   = bm25_raw.max()
    bm25_norm  = bm25_raw / (bm25_max + 1e-9)

    # FAISS 점수 (거리 → 유사도)
    dists = all_distances[query_idx]   # (160,) 거리 배열
    idxs  = all_faiss_indices[query_idx]
    faiss_raw = np.zeros(len(STANDARD_NAMES))
    for d, i in zip(dists, idxs):
        faiss_raw[i] = 1.0 / (1.0 + float(d))
    faiss_max  = faiss_raw.max()
    faiss_norm = faiss_raw / (faiss_max + 1e-9)

    # 혼합 점수
    combined  = BM25_ALPHA * bm25_norm + (1.0 - BM25_ALPHA) * faiss_norm
    top_k_idx = np.argsort(combined)[::-1][:k]
    return [STANDARD_NAMES[i] for i in top_k_idx]

# ===== 개선 4: 카테고리 포함 프롬프트 =====
PROMPT_TEMPLATE = """당신은 한국어 하드웨어 공구 이름 분류 전문가입니다.
정제되지 않은 공구 이름을 분석하여 아래 목록에서 가장 적합한 표준 정보를 추출하세요.

[공구 카테고리 정보]
- 대분류: {categories}
- 소분류: {sub_categories}

[표준 공구명 후보 (하이브리드 검색 상위 {k}개)]
{standard_name_candidates}

[브랜드 목록] (없으면 null)
{brand_list}

[전원 방식 목록] (없으면 null)
{power_source_list}

규칙:
- standard_name은 반드시 위 '표준 공구명 후보' 중 하나를 선택하세요.
- 카테고리 정보를 우선 참고하여 후보 중 가장 적합한 것을 고르세요.
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

def call_llm(tool_name: str, candidates: list, categories: str, sub_categories: str) -> dict:
    prompt = PROMPT_TEMPLATE.format(
        categories=categories,
        sub_categories=sub_categories,
        k=len(candidates),
        standard_name_candidates='\n'.join(f'  - {c}' for c in candidates),
        brand_list=', '.join(BRANDS),
        power_source_list=', '.join(POWER_SOURCES),
        tool_name=str(tool_name).strip()
    )
    try:
        if IS_QWEN3:
            resp = ollama.generate(
                model=MODEL_NAME, prompt=prompt,
                stream=False, options={"temperature": 0, "num_predict": 3000, "num_gpu": 99}
            )
            text = resp.get('response', '{}')
            text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()
            m = re.search(r'\{[^{}]*\}', text, re.DOTALL)
            text = m.group(0) if m else '{}'
        else:
            resp = ollama.generate(
                model=MODEL_NAME, prompt=prompt,
                format='json', stream=False,
                options={"temperature": 0, "num_predict": 800, "num_gpu": 99}
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

# ===== 실행 =====
total = len(tool_names)
categories_list     = df_run['Categories'].fillna('미분류').astype(str).tolist()
sub_categories_list = df_run['SubCategories'].fillna('미분류').astype(str).tolist()

CHECKPOINT_FILE = OUTPUT_DIR + f'checkpoint_improved_{MODEL_SAVE_NAME}.csv'
CHECKPOINT_INTERVAL = 50  # 50건마다 체크포인트 저장

# 재개 모드: 기존 체크포인트 로드
START_FROM = 0
results = []
if RESUME and os.path.exists(CHECKPOINT_FILE):
    df_cp = pd.read_csv(CHECKPOINT_FILE)
    results = df_cp.to_dict('records')
    START_FROM = len(results)
    print(f"[재개] 체크포인트 로드: {START_FROM}건 이미 처리됨, {START_FROM}번부터 재개")
else:
    if RESUME:
        print(f"[재개] 체크포인트 없음 — 처음부터 시작")

t_llm_start    = time.time()
report_interval = 50  # 50개마다 진행 상황 출력

print(f"--- LLM 처리 시작 ({MODEL_NAME}) ---")
print(f"    총 {total:,}개 | 시작위치: {START_FROM:,}번 | 진행표시: {report_interval}개마다\n")

for i, (tool_name, cat, subcat) in enumerate(
        zip(tool_names, categories_list, sub_categories_list)):

    if i < START_FROM:
        continue

    candidates = hybrid_search(tool_name, i)
    r = call_llm(tool_name, candidates, cat, subcat)

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

    # 체크포인트 저장 (CHECKPOINT_INTERVAL마다)
    if len(results) % CHECKPOINT_INTERVAL == 0:
        pd.DataFrame(results).to_csv(CHECKPOINT_FILE, index=False, encoding='utf-8-sig')

    done = i + 1
    if done % report_interval == 0 or done == total:
        elapsed = time.time() - t_llm_start
        pct     = done / total * 100
        processed_this_session = done - START_FROM
        speed   = processed_this_session / elapsed if elapsed > 0 else 0
        eta     = str(timedelta(seconds=int((total - done) / speed))) if speed > 0 else "?"
        print(f"  ▶ [{pct:5.1f}%] {done:,}/{total:,}개 | "
              f"속도: {speed:.2f}개/초 | "
              f"경과: {str(timedelta(seconds=int(elapsed)))} | "
              f"ETA: {eta}")

t_llm_total = time.time() - t_llm_start
df_results = pd.DataFrame(results)

# ===== 속도 요약 =====
print(f"\n{'='*60}")
print(f"  모델           : {MODEL_NAME}")
print(f"  임베딩 모델     : {EMBED_MODEL_NAME}")
print(f"  처리 건수       : {total}개")
print(f"  임베딩 시간     : {t_embed:.1f}초 (BGE-m3-ko GPU 배치)")
print(f"  LLM 추론 시간   : {str(timedelta(seconds=int(t_llm_total)))}")
print(f"  평균 속도       : {total/t_llm_total:.2f}건/초")
print(f"  총 소요 시간    : {str(timedelta(seconds=int(t_embed + t_llm_total)))}")
print(f"{'='*60}\n")

# ===== 평가 =====
gt_map = df_gt.set_index('original_name')['standard_name'].to_dict()
df_results['gt_standard_name'] = df_results['Input_Name'].map(gt_map)

def check_correct(row):
    if pd.isna(row.get('gt_standard_name')):
        return None
    return str(row.get('standard_name', '')).strip() == str(row['gt_standard_name']).strip()

df_results['is_correct'] = df_results.apply(check_correct, axis=1)
evaluatable = df_results[df_results['gt_standard_name'].notna()]

print(f"=== 평가 결과 ({MODEL_NAME} + improved) ===")
print(f"전체 처리: {len(df_results)}개 | 정답 존재: {len(evaluatable)}개")
correct  = 0
fallback = 0
if len(evaluatable) > 0:
    correct  = int((evaluatable['is_correct'] == True).sum())
    fallback = int(df_results.get('fallback_used', pd.Series([False]*len(df_results))).sum())
    print(f"정확도  : {correct}/{len(evaluatable)} = {correct/len(evaluatable):.2%}")
    print(f"Fallback: {fallback}건 ({fallback/len(df_results)*100:.1f}%)")

# ===== 저장 =====
n_label = len(df_results)
df_results.insert(0, 'model_name', MODEL_NAME)
save_path = OUTPUT_DIR + f'New_RAG_v2_improved_{MODEL_SAVE_NAME}_{n_label}.csv'
df_results.to_csv(save_path, index=False, encoding='utf-8-sig')

stats = {
    'model_name':    MODEL_NAME,
    'embed_model':   EMBED_MODEL_NAME,
    'variant':       'improved',
    'k_value':       K_VALUE,
    'bm25_alpha':    BM25_ALPHA,
    'total':         n_label,
    'embed_sec':     round(t_embed, 1),
    'llm_sec':       round(t_llm_total, 1),
    'total_sec':     round(t_embed + t_llm_total, 1),
    'speed_per_sec': round(total / t_llm_total, 2),
    'eval_count':    int(len(evaluatable)),
    'correct':       correct,
    'accuracy':      round(correct / len(evaluatable), 4) if len(evaluatable) > 0 else 0,
    'fallback_rate': round(fallback / n_label, 4),
    'error_rate':    round((df_results['status'] == 'error').mean(), 4)
                     if 'status' in df_results.columns else 0,
}
stats_path = OUTPUT_DIR + f'New_RAG_v2_improved_{MODEL_SAVE_NAME}_stats.json'
with open(stats_path, 'w', encoding='utf-8') as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)

print(f"\n결과 저장: {save_path}")
print(f"Stats 저장: {stats_path}")
print("완료.")
