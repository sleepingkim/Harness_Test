"""
New_RAG v2 - Ground Truth 기반 공구명 표준화 테스트 스크립트
실행: /home/neohc/miniconda3/bin/python run_rag_v2_test.py
"""

import ollama
import json
import pandas as pd
import re
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')

try:
    import faiss
    from sentence_transformers import SentenceTransformer
    print("모든 라이브러리 로드 완료.")
except ImportError as e:
    print(f"[오류] {e}")
    exit(1)

# ===== 설정 =====
BASE = '/mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5/'
TOOL_DATA_PATH    = BASE + 'ToolNameData.csv'
GROUND_TRUTH_PATH = BASE + 'standard_tool_names_ground_truth_v2.csv'
OUTPUT_DIR        = BASE

MODEL_NAME      = 'deepseek-r1:8b'
MODEL_SAVE_NAME = 'deepseek-r1_8b'
K_VALUE = 5
TEST_N  = 10

print(f"\n모델: {MODEL_NAME} | 테스트 행: {TEST_N}개\n")

# ===== 설치 모델 확인 =====
try:
    models = ollama.list()
    model_list = sorted(
        [(m.model, getattr(m, 'size', 0)) for m in models.models],
        key=lambda x: x[1]
    )
    print("=== 설치된 모델 (크기 오름차순) ===")
    for name, size in model_list:
        print(f"  {name:55s} {size/1e9:.1f}GB")
    print()
except Exception as e:
    print(f"ollama 연결 실패: {e}\n'ollama serve' 실행 여부 확인\n")
    exit(1)

# ===== 데이터 로드 =====
df_tool = pd.read_csv(TOOL_DATA_PATH)
df_gt   = pd.read_csv(GROUND_TRUTH_PATH)
print(f"ToolNameData: {df_tool.shape} | Ground Truth: {df_gt.shape}")

# RAG 지식 베이스: original_name 참조 금지
STANDARD_NAMES = df_gt['standard_name'].dropna().unique().tolist()
BRANDS         = df_gt['brand'].dropna().unique().tolist()
POWER_SOURCES  = df_gt['power_source'].dropna().unique().tolist()

print(f"표준 공구명: {len(STANDARD_NAMES)}종 | 브랜드: {len(BRANDS)}종 | 전원방식: {len(POWER_SOURCES)}종\n")

# ===== FAISS Vector DB 구축 =====
print("Vector DB 구축 중 (standard_name 목록 임베딩)...")
embed_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
vectors = embed_model.encode(STANDARD_NAMES, show_progress_bar=True)
dim = vectors.shape[1]
faiss_index = faiss.IndexFlatL2(dim)
faiss_index.add(vectors.astype('float32'))
print(f"FAISS DB 완료 (d={dim}, {len(STANDARD_NAMES)}개)\n")

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

# ===== RAG 함수 =====
def run_rag_v2(tool_name):
    # Retrieve
    query_vec = embed_model.encode([str(tool_name).strip()]).astype('float32')
    _, indices = faiss_index.search(query_vec, K_VALUE)
    candidates = [STANDARD_NAMES[i] for i in indices[0]]

    # Augment
    prompt = PROMPT_TEMPLATE.format(
        k=K_VALUE,
        standard_name_candidates='\n'.join(f'  - {c}' for c in candidates),
        brand_list=', '.join(BRANDS),
        power_source_list=', '.join(POWER_SOURCES),
        tool_name=str(tool_name).strip()
    )

    # Generate
    try:
        resp = ollama.generate(
            model=MODEL_NAME, prompt=prompt,
            format='json', stream=False,
            options={"temperature": 0}
        )
        text = resp.get('response', '{}')
        # think 태그 제거 (deepseek-r1 등)
        text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()
        parsed = json.loads(text)

        # standard_name이 후보 밖이면 top-1으로 fallback
        if parsed.get('standard_name') not in STANDARD_NAMES:
            parsed['standard_name'] = candidates[0]
            parsed['fallback_used'] = True
        else:
            parsed['fallback_used'] = False

        return {'status': 'success', 'data': parsed, 'candidates': candidates}
    except Exception as e:
        return {'status': 'error', 'message': str(e), 'candidates': candidates}

# ===== 실행 =====
df_test = df_tool.head(TEST_N).copy()
print(f"--- 처리 시작: {len(df_test)}개 ({MODEL_NAME}) ---")

results = []
for tool_name in tqdm(df_test['Original_Name'], desc="RAG 처리"):
    r = run_rag_v2(tool_name)
    entry = {
        'Input_Name':   tool_name,
        'status':       r['status'],
        'rag_top1':     r['candidates'][0] if r.get('candidates') else None,
        'rag_candidates': ', '.join(r.get('candidates', []))
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

df_results = pd.DataFrame(results)

# ===== 평가 =====
gt_map = df_gt.set_index('original_name')['standard_name'].to_dict()
df_results['gt_standard_name'] = df_results['Input_Name'].map(gt_map)

def check_correct(row):
    if pd.isna(row.get('gt_standard_name')):
        return None
    return str(row.get('standard_name', '')).strip() == str(row['gt_standard_name']).strip()

df_results['is_correct'] = df_results.apply(check_correct, axis=1)

evaluatable = df_results[df_results['gt_standard_name'].notna()]
print(f"\n=== 평가 결과 ===")
print(f"처리: {len(df_results)}개 | 정답 존재: {len(evaluatable)}개")
if len(evaluatable) > 0:
    correct = (evaluatable['is_correct'] == True).sum()
    print(f"정확도: {correct}/{len(evaluatable)} = {correct/len(evaluatable):.2%}")
    print()
    print(evaluatable[['Input_Name', 'standard_name', 'gt_standard_name', 'is_correct']].to_string())
else:
    print("테스트 10개 중 ground_truth_v2 일치 항목 없음 → 전체 실행 시 457개 비교 가능")

print("\n=== 전체 결과 ===")
cols = ['Input_Name', 'standard_name', 'brand', 'power_source',
        'specification', 'rag_top1', 'fallback_used', 'gt_standard_name', 'is_correct']
print(df_results[[c for c in cols if c in df_results.columns]].to_string())

# ===== 저장 =====
save_path = OUTPUT_DIR + f'New_RAG_v2_{MODEL_SAVE_NAME}_test{TEST_N}.csv'
df_results.to_csv(save_path, index=False, encoding='utf-8-sig')
print(f"\n결과 저장: {save_path}")
