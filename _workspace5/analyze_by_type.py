#!/usr/bin/env python3
"""
더티데이터 유형별 정제 성능 분석 — RAG v2 (improved, 상위 모델 기준)
- ground_truth_v2.csv (457쌍) × 각 모델 checkpoint 파일 매핑
- 13개 세부 유형별 정확도 계산 + 차트 생성
pip install pandas matplotlib seaborn openpyxl
"""

import re, os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
from matplotlib import font_manager

# 한글 폰트 설정 (Windows: Malgun Gothic)
_KO_FONTS = ["Malgun Gothic", "NanumGothic", "AppleGothic", "DejaVu Sans"]
for _fn in _KO_FONTS:
    if any(f.name == _fn for f in font_manager.fontManager.ttflist):
        matplotlib.rcParams["font.family"] = _fn
        break
matplotlib.rcParams["axes.unicode_minus"] = False

# ─── 경로 ──────────────────────────────────────────────────────────
DIR = os.path.dirname(os.path.abspath(__file__))
GT_PATH  = os.path.join(DIR, "standard_tool_names_ground_truth_v2.csv")

# 분석 대상 모델: (표시명, checkpoint 파일명)
MODELS = [
    ("gemma4:e4b",        "checkpoint_improved_gemma4_e4b.csv"),
    ("gemma3:4b",         "checkpoint_improved_gemma3_4b.csv"),
    ("granite4.1:8b",     "New_RAG_v2_improved_granite4_1_8b_3352.csv"),
    ("gemma4:e2b",        "checkpoint_improved_gemma4_e2b.csv"),
    ("exaone3.5:7.8b",   "checkpoint_improved_exaone3_5_7_8b.csv"),
    ("deepseek-r1:8b",   "New_RAG_v2_improved_deepseek-r1_8b_3352.csv"),
    ("deepseek-r1:1.5b", "checkpoint_improved_deepseek-r1_1_5b.csv"),
    ("exaone3.5:2.4b",   "checkpoint_improved_exaone3_5_2_4b.csv"),
    ("granite4.1:3b",    "checkpoint_improved_granite4_1_3b.csv"),
]

# ─── 더티데이터 유형 분류 휴리스틱 ────────────────────────────────────

BRANDS = [
    "보쉬", "BOSCH", "디월트", "DEWALT", "아임삭", "AIMSAK", "마끼다", "MAKITA",
    "계양", "KEYANG", "밀워키", "MILWAUKEE", "히타치", "HIKOKI", "히코키",
    "메보", "MEBO", "세신", "TAJIMA", "KNIPEX", "TOOLSTAR",
    "LS", "현대", "삼성", "LG", "파나소닉", "BOSCH",
]
JAPANESE = ["기리", "뺀치", "빤치", "함마", "빠루", "구루마", "니빠", "오함마",
            "겐나와", "사시가네", "란마"]
POWER    = ["유선", "충전", "무선", "에어", "배터리", "전동", "충전식", "코드리스",
            "gas", "가스", "engine", "엔진"]
SPECIAL  = [".", "&", "+", "/", "?", '"', "!", "@", "#", "%"]
ENG_ABR  = ["L렌치", "T렌치", "HSS", "SDS", "PCS", "PC", "SET", "mm", "cm",
             "inch", "V ", "W ", "rpm", "Ah", "LED", "USB", "AC", "DC"]
META_PAT = re.compile(r"^\([^)]*\)|^\d+[\)\.]\s|^\(?\d+,?\d*\)")

def classify(name: str) -> str:
    n = str(name)

    # 1. 인코딩 오류
    if "?" in n or "▯" in n:
        return "인코딩 오류"

    # 2. 운영용 텍스트 (가격, 전화번호, 예약 등)
    if any(k in n for k in ["원)", "원/", "예약", "전화", "문의", "추가 시", "개당"]):
        return "운영용 텍스트"

    # 3. 메타데이터 (숫자 태그, 분류불가, 상태 주석)
    if META_PAT.match(n) or any(k in n for k in ["(불가)", "(상자)", "(수리)", "(고장)"]):
        return "메타데이터"

    # 4. 일본어 잔재
    if any(j in n for j in JAPANESE):
        return "일본어 잔재"

    # 5. 브랜드 혼입
    if any(b.lower() in n.lower() for b in BRANDS):
        return "브랜드 혼입"

    # 6. 동력원 명시
    if any(p in n for p in POWER):
        return "동력원 명시"

    # 7. 영문/약어
    if any(e.lower() in n.lower() for e in ENG_ABR) or re.search(r"[A-Za-z]{3,}", n):
        return "영문/약어"

    # 8. 특수기호
    if any(s in n for s in SPECIAL):
        return "특수기호"

    # 9. 세트/구성품
    if any(k in n for k in ["세트", "set", "SET", "&", "＆", "구성", "키트"]):
        return "세트/구성품"

    # 10. 속성 기입 (숫자+단위, 규격, 크기 등)
    if re.search(r"\d+\s*(mm|cm|m|인치|V|W|A|T|kg|g|호|날|단|개|pc|pcs)", n, re.I):
        return "속성 기입"

    # 11. 복합명사 (두 가지 이상 공구 결합)
    if "/" in n or ("+" in n and len(n) > 5):
        return "복합명사"

    # 12. 오탈자 (특별한 패턴 없으나 비표준 — 나머지)
    # 간단한 어절 구조 이탈 확인
    if re.search(r"[가-힣]{2,}[가-힣ㄱ-ㅎㅏ-ㅣ]", n) and len(n) <= 15:
        return "오탈자"

    return "기타"


# ─── 분석 메인 ─────────────────────────────────────────────────────

def load_gt():
    gt = pd.read_csv(GT_PATH, encoding="utf-8-sig")
    gt.columns = gt.columns.str.strip()
    gt = gt[["original_name", "standard_name"]].dropna()
    gt["dirty_type"] = gt["original_name"].apply(classify)
    return gt


def load_checkpoint(fpath):
    try:
        df = pd.read_csv(fpath, encoding="utf-8-sig", low_memory=False)
    except UnicodeDecodeError:
        df = pd.read_csv(fpath, encoding="cp949", low_memory=False)
    df.columns = df.columns.str.strip()
    # 칼럼 이름 표준화
    if "Input_Name" in df.columns:
        df = df.rename(columns={"Input_Name": "input_name"})
    if "standard_name" not in df.columns and "Preprocessed_Name" in df.columns:
        df = df.rename(columns={"Preprocessed_Name": "standard_name"})
    return df[["input_name", "standard_name"]].dropna()


def analyze(gt, ck):
    merged = gt.merge(ck, left_on="original_name", right_on="input_name", how="inner",
                      suffixes=("_gt", "_pred"))
    if merged.empty:
        return None
    merged["correct"] = (
        merged["standard_name_gt"].str.strip() == merged["standard_name_pred"].str.strip()
    )
    return merged


# 유형 순서 고정 (빈도 높은 순)
TYPE_ORDER = [
    "속성 기입", "브랜드 혼입", "동력원 명시", "세트/구성품",
    "오탈자", "복합명사", "메타데이터", "일본어 잔재",
    "영문/약어", "특수기호", "운영용 텍스트", "인코딩 오류", "기타",
]

def compute_type_accuracy(merged):
    grp = merged.groupby("dirty_type").agg(
        correct=("correct", "sum"),
        total=("correct", "count"),
    ).reset_index()
    grp["accuracy"] = grp["correct"] / grp["total"] * 100
    # 순서 맞추기
    grp["order"] = grp["dirty_type"].map(
        {t: i for i, t in enumerate(TYPE_ORDER)}
    ).fillna(99)
    return grp.sort_values("order").reset_index(drop=True)


def run():
    gt = load_gt()
    print(f"Ground Truth: {len(gt)}쌍 | 유형 분포:")
    print(gt["dirty_type"].value_counts().to_string())
    print()

    all_results = {}   # model_name → type accuracy df
    overall_acc = {}

    for model_name, ck_file in MODELS:
        ck_path = os.path.join(DIR, ck_file)
        if not os.path.exists(ck_path):
            print(f"  [SKIP] {model_name}: {ck_file} 없음")
            continue
        ck   = load_checkpoint(ck_path)
        mrgd = analyze(gt, ck)
        if mrgd is None or mrgd.empty:
            print(f"  [SKIP] {model_name}: 매핑 데이터 없음")
            continue

        acc = mrgd["correct"].mean() * 100
        overall_acc[model_name] = acc
        all_results[model_name] = compute_type_accuracy(mrgd)
        print(f"  {model_name:20s}  전체 정확도 {acc:.2f}%  ({mrgd['correct'].sum()}/{len(mrgd)}건 매핑)")

    if not all_results:
        print("\n분석 가능한 checkpoint 파일이 없습니다.")
        print("파일명을 확인하세요:")
        for m, f in MODELS:
            print(f"  {f}")
        return

    # ── 메인 모델 유형별 분석 테이블 ────────────────────────────────
    best_model = max(overall_acc, key=overall_acc.get)
    best_df    = all_results[best_model]

    print(f"\n{'='*60}")
    print(f"[유형별 정확도] 최고 모델: {best_model} ({overall_acc[best_model]:.2f}%)")
    print(f"{'='*60}")
    print(f"{'유형':<15} {'정답':>5} {'전체':>5} {'정확도':>8}")
    print("-" * 40)
    for _, row in best_df.iterrows():
        print(f"{row['dirty_type']:<15} {int(row['correct']):>5} "
              f"{int(row['total']):>5} {row['accuracy']:>7.1f}%")

    # ── 차트 1: 유형별 정확도 (상위 모델 기준) ───────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(18, 7))
    fig.suptitle("RAG v2 (Improved) — Dirty Data Type Analysis", fontsize=15, fontweight="bold")

    ax1 = axes[0]
    colors = ["#2E70BF" if acc >= 80 else "#E67E22" if acc >= 60 else "#C0392B"
              for acc in best_df["accuracy"]]
    bars = ax1.barh(best_df["dirty_type"], best_df["accuracy"], color=colors)
    ax1.set_xlabel("Accuracy (%)", fontsize=12)
    ax1.set_title(f"Accuracy by Dirty Data Type\n({best_model} — improved RAG)", fontsize=12)
    ax1.set_xlim(0, 110)
    ax1.axvline(80, color="#888888", linestyle="--", linewidth=1, alpha=0.7, label="80% threshold")
    ax1.legend(fontsize=10)
    for bar, acc, n in zip(bars, best_df["accuracy"], best_df["total"]):
        ax1.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                 f"{acc:.1f}% (n={int(n)})", va="center", fontsize=9)

    # ── 차트 2: 모델별 × 유형별 히트맵 ─────────────────────────────
    ax2 = axes[1]
    # 공통 유형만
    common_types = TYPE_ORDER[:10]
    heatmap_data = {}
    for model_name, df in all_results.items():
        row = {r["dirty_type"]: r["accuracy"] for _, r in df.iterrows()}
        heatmap_data[model_name] = [row.get(t, float("nan")) for t in common_types]

    if len(heatmap_data) >= 2:
        hm_df = pd.DataFrame(heatmap_data, index=common_types)
        im = ax2.imshow(hm_df.values, cmap="RdYlGn", aspect="auto",
                        vmin=0, vmax=100)
        ax2.set_xticks(range(len(hm_df.columns)))
        ax2.set_xticklabels(hm_df.columns, rotation=30, ha="right", fontsize=9)
        ax2.set_yticks(range(len(common_types)))
        ax2.set_yticklabels(common_types, fontsize=9)
        ax2.set_title("Accuracy Heatmap by Type × Model", fontsize=12)
        plt.colorbar(im, ax=ax2, label="Accuracy (%)")
        for i in range(len(common_types)):
            for j, col in enumerate(hm_df.columns):
                val = hm_df.values[i, j]
                if not np.isnan(val):
                    ax2.text(j, i, f"{val:.0f}", ha="center", va="center",
                             fontsize=8, color="white" if val < 50 else "black")
    else:
        ax2.text(0.5, 0.5, "모델 2개 이상 필요 (히트맵)", ha="center", va="center",
                 transform=ax2.transAxes, fontsize=12)
        ax2.set_title("Accuracy Heatmap (모델 부족)", fontsize=12)

    plt.tight_layout()
    out_chart = os.path.join(DIR, "type_accuracy_chart.png")
    plt.savefig(out_chart, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"\n  차트 저장: {out_chart}")

    # ── 차트 3: 전체 모델 전체 정확도 막대 ──────────────────────────
    fig2, ax3 = plt.subplots(figsize=(10, 5))
    models_sorted = sorted(overall_acc.items(), key=lambda x: x[1], reverse=True)
    names, accs = zip(*models_sorted)
    bar_colors = ["#1A3A6B" if a >= 80 else "#E67E22" for a in accs]
    bars3 = ax3.bar(names, accs, color=bar_colors)
    ax3.set_ylabel("Overall Accuracy (%)", fontsize=12)
    ax3.set_title("RAG v2 Improved — Overall Accuracy by Model", fontsize=13, fontweight="bold")
    ax3.set_ylim(0, 100)
    ax3.axhline(80, color="#888888", linestyle="--", linewidth=1, label="80% threshold")
    ax3.legend()
    for bar, acc in zip(bars3, accs):
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f"{acc:.1f}%", ha="center", fontsize=10, fontweight="bold")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    out_chart2 = os.path.join(DIR, "overall_accuracy_chart.png")
    plt.savefig(out_chart2, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  차트 저장: {out_chart2}")

    # ── Excel 저장 ─────────────────────────────────────────────────
    out_xlsx = os.path.join(DIR, "type_accuracy_analysis.xlsx")
    safe_name = best_model.replace(":", "-")  # Excel 시트명에 ':' 불가
    with pd.ExcelWriter(out_xlsx, engine="openpyxl") as writer:
        # 유형별 분석 (최고 모델)
        best_df.to_excel(writer, sheet_name=f"{safe_name}_유형별", index=False)
        # 전체 모델 정확도
        ov_df = pd.DataFrame([{"model": k, "overall_accuracy": v}
                               for k, v in overall_acc.items()])
        ov_df.to_excel(writer, sheet_name="전체_모델_정확도", index=False)
        # 유형×모델 매트릭스
        if len(heatmap_data) >= 1:
            hm_out = pd.DataFrame(heatmap_data, index=common_types)
            hm_out.to_excel(writer, sheet_name="유형×모델_히트맵")
    print(f"  Excel 저장: {out_xlsx}")
    print("\n완료.")


if __name__ == "__main__":
    run()
