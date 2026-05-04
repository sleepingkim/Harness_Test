"""
RAG v2 LLM 추론 결과 오류 유형화 분석
- 대상: 모든 improved 모델 결과 CSV + 통합 분석
- 출력: error_analysis_result.csv, error_analysis_result.xlsx
"""

import os
import re
import pandas as pd
import glob
from collections import defaultdict

# ─────────────────────────────────────────
# 1. 데이터 로드
# ─────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_FILES = {
    "deepseek-r1:1.5b":  "New_RAG_v2_improved_deepseek-r1_1_5b_3352.csv",
    "deepseek-r1:8b":    "New_RAG_v2_improved_deepseek-r1_8b_3352.csv",
    "exaone3.5:2.4b":    "New_RAG_v2_improved_exaone3_5_2_4b_3352.csv",
    "exaone3.5:7.8b":    "New_RAG_v2_improved_exaone3_5_7_8b_3352.csv",
    "gemma3:4b":         "New_RAG_v2_improved_gemma3_4b_3352.csv",
    "gemma4:e2b":        "New_RAG_v2_improved_gemma4_e2b_3352.csv",
    "gemma4:e4b":        "New_RAG_v2_improved_gemma4_e4b_3352.csv",
    "granite4.1:3b":     "New_RAG_v2_improved_granite4_1_3b_3352.csv",
    "granite4.1:8b":     "New_RAG_v2_improved_granite4_1_8b_3352.csv",
}

# ─────────────────────────────────────────
# 2. 오류 유형 분류 함수
# ─────────────────────────────────────────

# 일본어 잔재 패턴
JAPANESE_REMNANT = re.compile(
    r'기리|뺀치|빤치|빼앙치|뻰치|함마|오함마|빠루|구루마|겐나와|니빠|니빠|'
    r'야스리|삼빠이|하구리|노기스|사이즈|빽|빽비트|뽀루|짱꼬|카나루|'
    r'바이스|바에스|베이스', re.IGNORECASE
)

# 오탈자 패턴 (실제 확인된 예시 기반)
TYPO_PATTERN = re.compile(
    r'경랑|궁창|마끼다(?!.*마끼다)|롤러(?=.*비)\b|핸드카드|'
    r'수평게|레이저수준기|뺑기|빵기|드라이바|그라인다|'
    r'커터칼|커트기|절단기\s*\(원형\)|바이스플라이어|'
    r'오실레이팅|오시레이팅', re.IGNORECASE
)

# 브랜드 패턴
BRAND_PATTERN = re.compile(
    r'보쉬|BOSCH|디월트|DEWALT|마끼다|MAKITA|아임삭|AIMSAK|'
    r'계양|KAIYANG|밀워키|MILWAUKEE|히타치|HITACHI|스탠리|STANLEY|'
    r'블랙앤데커|BLACK|DECKER|타지마|TAJIMA|마르텐스|MARTENS|'
    r'볼더|BOLDER|세신|SESHIN|대우|DAEWOO|삼성|SAMSUNG|'
    r'LG|FESTOOL|FEIN|BOSCH|METABO|FLEX|RIDGID|RYOBI|'
    r'pushdrive|push\s*drive', re.IGNORECASE
)

# 규격/크기 패턴
SPEC_PATTERN = re.compile(
    r'\d+\s*(mm|cm|m|인치|inch|V|W|Ah|A|kg|t|L|PCS|pc|개입|입|호|'
    r'oz|lb|ft|갈론|피트|마력|hp|rpm|Hz|kN|N|J|kJ)\b|'
    r'\d+[\-×x]\d+|'\
    r'[\d]+인치|[0-9]+[Vv]|'
    r'1/[0-9]+|[0-9]+/[0-9]+',
    re.IGNORECASE
)

# 동력원 명시 패턴
POWER_PATTERN = re.compile(
    r'충전|무선|유선|전기|에어|공압|배터리|battery|가스|수동|'
    r'전동(?!\s*[드줄톱])|\(무선\)|\(유선\)|\(충전\)|\(에어\)',
    re.IGNORECASE
)

# 세트/복합 패턴
SET_PATTERN = re.compile(
    r'[&＆+／/]|세트|셋트|키트|kit|조합|패키지|set\b|'
    r'[가-힣]+[&]|[가-힣]+\/[가-힣]+',
    re.IGNORECASE
)

# 모델/제품번호 패턴
MODEL_NUM_PATTERN = re.compile(
    r'[A-Z]{2,}[\-\s]?\d{2,}|'
    r'\d{2,}[A-Z]{1,3}|'
    r'GBH|GSB|GWS|DCD|DCF|DHR|DGA|XR\b',
    re.IGNORECASE
)

# 유사 공구명 그룹 (혼동 가능한 공구 군집)
SIMILAR_GROUPS = [
    {"전동드릴", "충전드릴", "임팩트드릴", "해머드릴", "충전해머드릴", "로터리해머드릴", "SDS드릴"},
    {"임팩트드라이버", "충전임팩트드라이버", "전동드라이버", "드라이버", "드라이버세트"},
    {"앵글그라인더", "그라인더", "디스크그라인더", "소형그라인더"},
    {"원형톱", "직소기", "왕복톱", "레시프로쏘", "고속절단기", "각도절단기"},
    {"샌더", "샌딩기", "벨트샌더", "진동샌더"},
    {"펜치", "플라이어", "워터펌프플라이어", "스냅링플라이어", "롱노즈플라이어",
     "다이아고날플라이어", "굽은노즈플라이어", "바이스그립플라이어", "플라이어세트"},
    {"스패너", "스패너세트", "편구스패너", "양구스패너", "콤비네이션스패너"},
    {"렌치", "토크렌치", "파이프렌치", "몽키렌치", "기어렌치", "기어렌치세트",
     "라쳇렌치", "라쳇렌치세트", "소켓렌치", "소켓렌치세트"},
    {"드릴비트", "드릴비트세트", "SDS드릴비트", "철공용드릴비트", "목공용드릴비트",
     "철공용드릴비트세트"},
    {"레이저수평기", "레이저거리측정기", "레이저레벨", "수평기", "수준기"},
    {"공구세트", "전동공구세트", "공구함세트", "공구함"},
]

def find_similar_group(name_a: str, name_b: str) -> bool:
    """두 공구명이 같은 유사 그룹에 속하는지 확인"""
    for group in SIMILAR_GROUPS:
        if name_a in group and name_b in group:
            return True
    return False

def classify_input_type(input_name: str) -> list:
    """입력명의 더티데이터 유형 분류 (복수 해당 가능)"""
    types = []
    if BRAND_PATTERN.search(input_name):
        types.append("브랜드명_혼입")
    if SPEC_PATTERN.search(input_name):
        types.append("규격_속성_혼입")
    if POWER_PATTERN.search(input_name):
        types.append("동력원_명시")
    if SET_PATTERN.search(input_name):
        types.append("세트_복합")
    if JAPANESE_REMNANT.search(input_name):
        types.append("일본어_잔재")
    if TYPO_PATTERN.search(input_name):
        types.append("오탈자_의심")
    if MODEL_NUM_PATTERN.search(input_name):
        types.append("모델번호_포함")
    if not types:
        types.append("단순명사형")
    return types

def classify_system_failure(row) -> str:
    """시스템 단계별 실패 원인 분류"""
    candidates = [c.strip() for c in str(row.get('rag_candidates', '')).split(',')]
    gt = str(row.get('gt_standard_name', '')).strip()
    pred = str(row.get('standard_name', '')).strip()

    if not gt:
        return "정답없음"

    gt_in_candidates = gt in candidates

    if not gt_in_candidates:
        return "RAG_후보_누락"
    else:
        # LLM이 후보 안에서 잘못 선택
        if find_similar_group(pred, gt):
            return "LLM_유사공구_오선택"
        elif pred in candidates:
            return "LLM_후보내_오선택"
        else:
            return "LLM_비후보_출력"

def classify_error_detail(row) -> str:
    """더 세밀한 오류 분류 (GT vs Pred 관계 기반)"""
    gt = str(row.get('gt_standard_name', '')).strip()
    pred = str(row.get('standard_name', '')).strip()

    if not gt or not pred:
        return "데이터_없음"

    # 정답이 후보에 없었던 경우
    candidates = [c.strip() for c in str(row.get('rag_candidates', '')).split(',')]
    if gt not in candidates:
        return "RAG_검색_실패"

    # 동일 카테고리 내 세부 분류 혼동
    if find_similar_group(pred, gt):
        # 동력원 차이?
        pred_has_charge = any(kw in pred for kw in ["충전", "무선", "배터리"])
        gt_has_charge = any(kw in gt for kw in ["충전", "무선", "배터리"])
        pred_has_wire = any(kw in pred for kw in ["전동", "유선", "전기"])
        gt_has_wire = any(kw in gt for kw in ["전동", "유선", "전기"])
        if pred_has_charge != gt_has_charge or pred_has_wire != gt_has_wire:
            return "동력원_분류_오류"
        # 드릴/드라이버 계열 혼동
        if any(kw in pred for kw in ["드릴", "드라이버"]) and \
           any(kw in gt for kw in ["드릴", "드라이버"]):
            return "드릴_드라이버_계열_혼동"
        return "동일계열_공구_혼동"

    # 상위/하위 개념 오류 (세트 vs 단품)
    pred_is_set = "세트" in pred or "키트" in pred
    gt_is_set = "세트" in gt or "키트" in gt
    if pred_is_set != gt_is_set:
        return "세트_단품_혼동"

    # 비트/부속품 vs 본체 혼동
    accessory_kw = ["비트", "날", "블레이드", "배터리", "충전기", "소켓"]
    pred_is_accessory = any(kw in pred for kw in accessory_kw)
    gt_is_accessory = any(kw in gt for kw in accessory_kw)
    if pred_is_accessory != gt_is_accessory:
        return "본체_부속품_혼동"

    return "완전_다른_공구_선택"

# ─────────────────────────────────────────
# 3. 전체 모델 분석
# ─────────────────────────────────────────

all_errors = []
model_summaries = []

for model_key, csv_file in CSV_FILES.items():
    fpath = os.path.join(BASE_DIR, csv_file)
    if not os.path.exists(fpath):
        print(f"[SKIP] {csv_file} 없음")
        continue

    df = pd.read_csv(fpath)
    total = len(df)
    has_gt = df['gt_standard_name'].notna() & (df['gt_standard_name'] != '')
    df_eval = df[has_gt].copy()
    n_eval = len(df_eval)
    n_correct = df_eval['is_correct'].sum()
    n_wrong = n_eval - n_correct
    accuracy = n_correct / n_eval * 100 if n_eval > 0 else 0

    print(f"\n[{model_key}] 전체:{total} | 평가가능:{n_eval} | "
          f"정답:{n_correct} | 오답:{n_wrong} | 정확도:{accuracy:.2f}%")

    # 오답 행만 추출
    df_wrong = df_eval[df_eval['is_correct'] == False].copy()

    for _, row in df_wrong.iterrows():
        input_name = str(row['Input_Name'])
        input_types = classify_input_type(input_name)
        sys_fail = classify_system_failure(row)
        err_detail = classify_error_detail(row)

        candidates = [c.strip() for c in str(row.get('rag_candidates', '')).split(',')]
        gt = str(row.get('gt_standard_name', '')).strip()
        gt_rank = candidates.index(gt) + 1 if gt in candidates else -1

        all_errors.append({
            "model": model_key,
            "input_name": input_name,
            "predicted": str(row.get('standard_name', '')).strip(),
            "ground_truth": gt,
            "rag_top1": str(row.get('rag_top1', '')).strip(),
            "gt_in_candidates": gt in candidates,
            "gt_rank_in_candidates": gt_rank,
            "fallback_used": row.get('fallback_used', False),
            "input_dirty_types": " | ".join(input_types),
            "system_failure_type": sys_fail,
            "error_detail_type": err_detail,
        })

    model_summaries.append({
        "model": model_key,
        "total_rows": total,
        "eval_rows": n_eval,
        "correct": int(n_correct),
        "wrong": n_wrong,
        "accuracy_pct": round(accuracy, 2),
    })

# ─────────────────────────────────────────
# 4. 결과 데이터프레임 생성
# ─────────────────────────────────────────

df_errors = pd.DataFrame(all_errors)
df_summary = pd.DataFrame(model_summaries)

print(f"\n\n{'='*60}")
print(f"총 오답 레코드: {len(df_errors)}개 (모든 모델 합산)")
print(f"{'='*60}")

# ─────────────────────────────────────────
# 5. 유형별 집계 (gemma4:e4b 기준 상세 분석)
# ─────────────────────────────────────────

BEST_MODEL = "gemma4:e4b"
BEST_MODEL_SAFE = BEST_MODEL.replace(":", "_")
df_best = df_errors[df_errors['model'] == BEST_MODEL].copy()
n_best_wrong = len(df_best)

print(f"\n[{BEST_MODEL}] 오답 {n_best_wrong}개 상세 분석")
print("-"*50)

# 5a. 시스템 실패 유형별
sys_fail_counts = df_best['system_failure_type'].value_counts().reset_index()
sys_fail_counts.columns = ['system_failure_type', 'count']
sys_fail_counts['비율(%)'] = (sys_fail_counts['count'] / n_best_wrong * 100).round(1)
print("\n[시스템 실패 유형]")
print(sys_fail_counts.to_string(index=False))

# 5b. 오류 세부 유형별
err_detail_counts = df_best['error_detail_type'].value_counts().reset_index()
err_detail_counts.columns = ['error_detail_type', 'count']
err_detail_counts['비율(%)'] = (err_detail_counts['count'] / n_best_wrong * 100).round(1)
print("\n[오류 세부 유형]")
print(err_detail_counts.to_string(index=False))

# 5c. 입력 더티데이터 유형별 (복수 가능 → explode)
dirty_series = df_best['input_dirty_types'].str.split(' | ').explode()
dirty_counts = dirty_series.value_counts().reset_index()
dirty_counts.columns = ['input_dirty_type', 'count']
dirty_counts['비율(오답_대비,%)'] = (dirty_counts['count'] / n_best_wrong * 100).round(1)
print("\n[입력 더티데이터 유형 (오답 행 기준)]")
print(dirty_counts.to_string(index=False))

# 5d. RAG 후보 내 GT 순위 분포 (GT가 후보에 있는 경우)
gt_in_cand = df_best[df_best['gt_in_candidates'] == True]
rank_dist = gt_in_cand['gt_rank_in_candidates'].value_counts().sort_index().reset_index()
rank_dist.columns = ['gt_rank', 'count']
print(f"\n[GT가 후보에 있었으나 오답 → GT 후보 순위 분포 (n={len(gt_in_cand)})]")
print(rank_dist.to_string(index=False))

# ─────────────────────────────────────────
# 6. 전체 모델 교차 유형 분석
# ─────────────────────────────────────────

print(f"\n\n{'='*60}")
print("전체 모델 교차 오류 유형 분포")
print("="*60)

cross_sys = df_errors.groupby(['model', 'system_failure_type']).size().unstack(fill_value=0)
print(cross_sys)

cross_detail = df_errors.groupby(['model', 'error_detail_type']).size().unstack(fill_value=0)
print("\n[세부 유형 × 모델]\n")
print(cross_detail)

# ─────────────────────────────────────────
# 7. 저장
# ─────────────────────────────────────────

OUT_CSV = os.path.join(BASE_DIR, "error_analysis_result.csv")
OUT_XLSX = os.path.join(BASE_DIR, "error_analysis_result.xlsx")

df_errors.to_csv(OUT_CSV, index=False, encoding='utf-8-sig')
print(f"\n\n[저장] {OUT_CSV}")

with pd.ExcelWriter(OUT_XLSX, engine='openpyxl') as writer:
    # 시트1: 전체 오답 목록
    df_errors.to_excel(writer, sheet_name='전체_오답_목록', index=False)

    # 시트2: 모델별 요약
    df_summary.to_excel(writer, sheet_name='모델별_정확도_요약', index=False)

    # 시트3: 시스템 실패 유형 (best model)
    sys_fail_counts.to_excel(writer, sheet_name=f'{BEST_MODEL_SAFE}_시스템실패유형', index=False)

    # 시트4: 오류 세부 유형 (best model)
    err_detail_counts.to_excel(writer, sheet_name=f'{BEST_MODEL_SAFE}_오류세부유형', index=False)

    # 시트5: 입력 더티 유형 (best model)
    dirty_counts.to_excel(writer, sheet_name=f'{BEST_MODEL_SAFE}_입력더티유형', index=False)

    # 시트6: 전체 모델 시스템 실패 유형 교차
    cross_sys.to_excel(writer, sheet_name='모델별_시스템실패유형_교차')

    # 시트7: 전체 모델 세부 오류 교차
    cross_detail.to_excel(writer, sheet_name='모델별_세부오류유형_교차')

    # 시트8: GT 후보 순위 분포 (best model)
    rank_dist.to_excel(writer, sheet_name=f'{BEST_MODEL_SAFE}_GT후보순위분포', index=False)

print(f"[저장] {OUT_XLSX}")
print("\n완료!")
