"""Excel 저장 전용 스크립트 - error_analysis_result.csv 읽어서 xlsx 생성"""
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IN_CSV  = os.path.join(BASE_DIR, "error_analysis_result.csv")
OUT_XLS = os.path.join(BASE_DIR, "error_analysis_v2.xlsx")

df = pd.read_csv(IN_CSV)
BEST_MODEL = "gemma4:e4b"
df_best = df[df['model'] == BEST_MODEL].copy()
n = len(df_best)

# 모델별 요약 재계산
model_stats_path = {
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
rows = []
for m, f in model_stats_path.items():
    fpath = os.path.join(BASE_DIR, f)
    if not os.path.exists(fpath): continue
    d = pd.read_csv(fpath)
    has_gt = d['gt_standard_name'].notna() & (d['gt_standard_name'] != '')
    de = d[has_gt]
    nc = de['is_correct'].sum()
    rows.append({"model": m, "total_rows": len(d), "eval_rows": len(de),
                 "correct": int(nc), "wrong": len(de)-nc,
                 "accuracy_pct": round(nc/len(de)*100, 2) if len(de)>0 else 0})
df_summary = pd.DataFrame(rows)

# 유형별 집계
sys_fail = df_best['system_failure_type'].value_counts().reset_index()
sys_fail.columns = ['system_failure_type', 'count']
sys_fail['비율(%)'] = (sys_fail['count']/n*100).round(1)

err_detail = df_best['error_detail_type'].value_counts().reset_index()
err_detail.columns = ['error_detail_type', 'count']
err_detail['비율(%)'] = (err_detail['count']/n*100).round(1)

dirty = df_best['input_dirty_types'].str.split(' | ').explode().value_counts().reset_index()
dirty.columns = ['input_dirty_type', 'count']
dirty['비율(오답_대비,%)'] = (dirty['count']/n*100).round(1)

gt_in = df_best[df_best['gt_in_candidates']==True]
rank_d = gt_in['gt_rank_in_candidates'].value_counts().sort_index().reset_index()
rank_d.columns = ['gt_rank', 'count']

cross_sys = df.groupby(['model','system_failure_type']).size().unstack(fill_value=0)
cross_det = df.groupby(['model','error_detail_type']).size().unstack(fill_value=0)

# 오류 코드 설명 테이블
error_legend = pd.DataFrame([
    # 시스템 실패 유형
    {"구분": "시스템실패유형", "코드": "RAG_후보_누락",        "설명": "RAG가 GT를 후보 15개 안에 포함시키지 못함 → 올바른 정답이 LLM에 전달조차 안 됨"},
    {"구분": "시스템실패유형", "코드": "LLM_후보내_오선택",    "설명": "GT가 후보에 있었지만 LLM이 다른 후보를 선택함 → LLM 추론 오류"},
    {"구분": "시스템실패유형", "코드": "LLM_유사공구_오선택",  "설명": "LLM이 GT와 동일 유사그룹의 공구를 선택함 (e.g. 전동드릴↔충전드릴)"},
    {"구분": "시스템실패유형", "코드": "LLM_비후보_출력",      "설명": "LLM이 후보 목록에 없는 이름을 출력함 (환각)"},
    # 오류 세부 유형
    {"구분": "오류세부유형", "코드": "RAG_검색_실패",          "설명": "RAG가 GT를 후보에 포함하지 못한 케이스"},
    {"구분": "오류세부유형", "코드": "동일계열_공구_혼동",      "설명": "같은 공구 계열 안에서 혼동 (e.g. 앵글그라인더↔그라인더)"},
    {"구분": "오류세부유형", "코드": "드릴_드라이버_계열_혼동", "설명": "드릴/드라이버 계열 내 세부 분류 혼동"},
    {"구분": "오류세부유형", "코드": "동력원_분류_오류",        "설명": "충전식/유선/무선 등 동력원 구분 실패"},
    {"구분": "오류세부유형", "코드": "세트_단품_혼동",          "설명": "공구 세트와 단품 공구를 혼동"},
    {"구분": "오류세부유형", "코드": "본체_부속품_혼동",        "설명": "드릴비트·블레이드 등 부속품과 본체 공구를 혼동"},
    {"구분": "오류세부유형", "코드": "완전_다른_공구_선택",     "설명": "예측값과 GT가 전혀 다른 공구 (동일 계열도 아님)"},
    # 입력 더티데이터 유형
    {"구분": "입력더티유형", "코드": "브랜드명_혼입",           "설명": "보쉬·디월트 등 브랜드명이 공구명에 포함된 입력"},
    {"구분": "입력더티유형", "코드": "규격_속성_혼입",          "설명": "180mm·8인치 등 규격/크기/전압이 공구명에 포함"},
    {"구분": "입력더티유형", "코드": "동력원_명시",             "설명": "충전식·유선 등 동력원이 이름에 명시된 입력"},
    {"구분": "입력더티유형", "코드": "세트_복합",               "설명": "&·/·세트 등 복합 공구명 또는 세트 표기"},
    {"구분": "입력더티유형", "코드": "일본어_잔재",             "설명": "기리·뺀치·함마 등 일본어 유래 현장 용어"},
    {"구분": "입력더티유형", "코드": "오탈자_의심",             "설명": "경랑→경량 등 오탈자가 의심되는 입력"},
    {"구분": "입력더티유형", "코드": "모델번호_포함",           "설명": "GBH5-38X 등 제품 모델번호가 포함된 입력"},
    {"구분": "입력더티유형", "코드": "단순명사형",              "설명": "수식어 없이 단순 명사만으로 구성된 공구명"},
])

with pd.ExcelWriter(OUT_XLS, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='전체_오답_목록', index=False)
    df_summary.to_excel(writer, sheet_name='모델별_정확도_요약', index=False)
    sys_fail.to_excel(writer, sheet_name='gemma4e4b_시스템실패유형', index=False)
    err_detail.to_excel(writer, sheet_name='gemma4e4b_오류세부유형', index=False)
    dirty.to_excel(writer, sheet_name='gemma4e4b_입력더티유형', index=False)
    rank_d.to_excel(writer, sheet_name='gemma4e4b_GT후보순위분포', index=False)
    cross_sys.to_excel(writer, sheet_name='모델별_시스템실패유형')
    cross_det.to_excel(writer, sheet_name='모델별_세부오류유형')
    error_legend.to_excel(writer, sheet_name='오류코드_범례', index=False)

print(f"저장 완료: {OUT_XLS}")
