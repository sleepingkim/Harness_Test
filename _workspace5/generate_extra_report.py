"""
추가 4개 모델 (gemma3:4b, exaone3.5:7.8b, gemma3:27b, exaone3.5:32b) 비교 리포트 생성
실행: /home/neohc/miniconda3/bin/python generate_extra_report.py
출력: extra_models_comparison_report.md  +  extra_models_chart.png
"""

import os
import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import datetime, timedelta
from matplotlib.patches import Patch

BASE    = '/mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5/'
GT_PATH = BASE + 'standard_tool_names_ground_truth_v2.csv'

EXTRA_MODEL_SAVE_NAMES = {
    'gemma3_4b',
    'exaone3_5_7_8b',
    'gemma3_27b',
    'exaone3_5_32b',
}

# ===== 한글 폰트 =====
def set_korean_font():
    candidates = [
        '/usr/share/fonts/truetype/nanum/NanumGothic.ttf',
        '/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc',
        '/mnt/c/Windows/Fonts/malgun.ttf',
        '/mnt/c/Windows/Fonts/NanumGothic.ttf',
    ]
    for path in candidates:
        if os.path.exists(path):
            fm.fontManager.addfont(path)
            prop = fm.FontProperties(fname=path)
            matplotlib.rcParams['font.family'] = prop.get_name()
            matplotlib.rcParams['axes.unicode_minus'] = False
            print(f"한글 폰트: {path}")
            return prop
    print("한글 폰트 없음 - 기본 폰트 사용")
    return None

set_korean_font()

# ===== 결과 CSV 탐색 =====
result_files = sorted([
    f for f in os.listdir(BASE)
    if f.startswith('New_RAG_v2_') and f.endswith('_3352.csv')
])
print(f"\n발견된 결과 파일: {len(result_files)}개")

if not result_files:
    print("[오류] 완료된 결과 파일 없음. 스크립트 종료.")
    exit()

df_gt  = pd.read_csv(GT_PATH)
gt_map = df_gt.set_index('original_name')['standard_name'].to_dict()

# ===== 모델 save name 추출 헬퍼 =====
def extract_save_name(fname):
    name = fname.replace('New_RAG_v2_', '').replace('_3352.csv', '')
    if name.startswith('improved_'):
        name = name[len('improved_'):]
    elif name.startswith('baseline_'):
        name = name[len('baseline_'):]
    name = name.replace('_improved', '').replace('_baseline', '')
    return name

# ===== 성능 계산 =====
all_records = []

for fname in result_files:
    df = pd.read_csv(BASE + fname)
    total = len(df)

    stats_fname = fname.replace('_3352.csv', '_stats.json')
    stats = {}
    if os.path.exists(BASE + stats_fname):
        with open(BASE + stats_fname, 'r', encoding='utf-8') as f:
            stats = json.load(f)

    if 'model_name' in df.columns:
        model_display = str(df['model_name'].iloc[0])
    elif stats.get('model_name'):
        model_display = stats['model_name']
    else:
        raw = fname.replace('New_RAG_v2_', '').replace('_3352.csv', '')
        model_display = raw.replace('_', '-')

    if stats.get('accuracy') is not None:
        accuracy      = stats['accuracy']
        n_eval        = stats['eval_count']
        n_correct     = stats['correct']
        fallback_rate = stats['fallback_rate']
        error_rate    = stats['error_rate']
        speed         = stats.get('speed_per_sec')
        llm_sec       = stats.get('llm_sec')
        embed_sec     = stats.get('embed_sec')
    else:
        df['gt'] = df['Input_Name'].map(gt_map)
        evaluatable = df[df['gt'].notna()].copy()
        n_eval = len(evaluatable)
        evaluatable['correct'] = evaluatable.apply(
            lambda r: str(r.get('standard_name', '')).strip() == str(r['gt']).strip(), axis=1)
        n_correct     = int(evaluatable['correct'].sum())
        accuracy      = n_correct / n_eval if n_eval > 0 else 0.0
        fallback_rate = df.get('fallback_used', pd.Series([False]*total)).fillna(False).astype(bool).mean()
        error_rate    = (df['status'] == 'error').mean() if 'status' in df.columns else 0.0
        speed = llm_sec = embed_sec = None

    variant   = 'improved' if 'improved' in fname else 'baseline'
    save_name = extract_save_name(fname)
    is_extra  = save_name in EXTRA_MODEL_SAVE_NAMES

    all_records.append({
        'model':         model_display,
        'variant':       variant,
        'label':         f"{model_display} [{variant}]",
        'embed_model':   stats.get('embed_model', 'paraphrase-multilingual-MiniLM-L12-v2').split('/')[-1],
        'k_value':       stats.get('k_value', 5),
        'total':         total,
        'eval_count':    int(n_eval),
        'correct':       int(n_correct),
        'accuracy':      accuracy,
        'fallback_rate': fallback_rate,
        'error_rate':    error_rate,
        'speed':         speed,
        'llm_sec':       llm_sec,
        'embed_sec':     embed_sec,
        'is_extra':      is_extra,
    })

df_all = pd.DataFrame(all_records).sort_values('accuracy', ascending=False).reset_index(drop=True)
df_all['rank'] = df_all.index + 1

df_extra  = df_all[df_all['is_extra']].reset_index(drop=True)
df_others = df_all[~df_all['is_extra']].reset_index(drop=True)

print(f"\n추가 4개 모델 결과: {len(df_extra)}개")
for _, r in df_extra.iterrows():
    print(f"  {r['label']}: {r['accuracy']:.2%}")

print(f"\n기존 모델 결과: {len(df_others)}개")
for _, r in df_others.iterrows():
    print(f"  {r['label']}: {r['accuracy']:.2%}")

if df_extra.empty:
    print("\n[경고] 추가 4개 모델 결과 없음. 리포트를 생성하지 않습니다.")
    exit()

# ===== 차트 생성 =====
fig, axes = plt.subplots(1, 2, figsize=(max(16, (len(df_extra) + len(df_others)) * 1.2), 8))
fig.suptitle('추가 4개 모델 vs 기존 모델 — 정확도 비교', fontsize=14, fontweight='bold')

COLOR_EXTRA_IMP   = '#E91E63'   # 핑크 — 추가 improved
COLOR_EXTRA_BASE  = '#F48FB1'   # 연핑크 — 추가 baseline (혹시 있다면)
COLOR_OTHER_IMP   = '#FF9800'   # 주황 — 기존 improved
COLOR_OTHER_BASE  = '#2196F3'   # 파랑 — 기존 baseline

def row_color(row):
    if row['is_extra']:
        return COLOR_EXTRA_IMP if row['variant'] == 'improved' else COLOR_EXTRA_BASE
    return COLOR_OTHER_IMP if row['variant'] == 'improved' else COLOR_OTHER_BASE

for ax_idx, (df_sub, title_suffix) in enumerate([(df_extra, '추가 4개 모델'), (df_all, '전체 비교')]):
    ax = axes[ax_idx]
    labels_sub  = df_sub['label'].tolist()
    accs_sub    = [a * 100 for a in df_sub['accuracy'].tolist()]
    colors_sub  = [row_color(r) for _, r in df_sub.iterrows()]

    bars = ax.barh(range(len(labels_sub)), accs_sub, color=colors_sub)
    ax.set_yticks(range(len(labels_sub)))
    ax.set_yticklabels(labels_sub, fontsize=8)
    ax.set_xlabel('정확도 (%)')
    ax.set_title(title_suffix)
    ax.set_xlim(0, 108)

    for bar, acc in zip(bars, accs_sub):
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
                f'{acc:.1f}%', va='center', fontsize=7, fontweight='bold')

    ax.legend(handles=[
        Patch(color=COLOR_EXTRA_IMP,  label='추가 모델 (improved)'),
        Patch(color=COLOR_OTHER_IMP,  label='기존 모델 (improved)'),
        Patch(color=COLOR_OTHER_BASE, label='기존 모델 (baseline)'),
    ], loc='lower right', fontsize=8)

plt.tight_layout()
chart_path = BASE + 'extra_models_chart.png'
plt.savefig(chart_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"\n차트 저장: {chart_path}")

# ===== Markdown 리포트 =====
now = datetime.now().strftime('%Y-%m-%d %H:%M')

def fmt_row(row):
    speed_str = f"{row['speed']:.2f}건/초" if row.get('speed') else "-"
    llm_str   = str(timedelta(seconds=int(row['llm_sec']))) if row.get('llm_sec') else "-"
    tag = '🆕' if row['is_extra'] else ('✅' if row['variant'] == 'improved' else '▪️')
    return (f"| {int(row['rank'])} | {tag} `{row['model']}` ({row['variant']}) "
            f"| **{row['accuracy']:.2%}** "
            f"| {int(row['eval_count'])} "
            f"| {int(row['correct'])} "
            f"| {row['fallback_rate']:.2%} "
            f"| {row['error_rate']:.2%} "
            f"| {speed_str} "
            f"| {llm_str} |")

tbl_header = [
    "| 순위 | 모델 (variant) | 정확도 | 평가 건수 | 정답 건수 | Fallback율 | 에러율 | 처리속도 | LLM 소요시간 |",
    "|:----:|---------------|-------:|--------:|--------:|---------:|------:|-------:|----------:|",
]

md_lines = [
    f"# 추가 4개 모델 vs 기존 모델 — 성능 비교 리포트",
    f"",
    f"> 생성: {now}  ",
    f"> 추가 모델 (improved only): gemma3:4b · exaone3.5:7.8b · gemma3:27b · exaone3.5:32b  ",
    f"> 정제 대상: ToolNameData.csv (3,352개) | 평가 기준: ground_truth_v2.csv ({len(gt_map)}개)  ",
    f"",
    f"---",
    f"",
    f"## 추가 모델 성능 (🆕)",
    f"",
] + tbl_header

for _, row in df_extra.sort_values('accuracy', ascending=False).iterrows():
    md_lines.append(fmt_row(row))

md_lines += [
    f"",
    f"---",
    f"",
    f"## 전체 순위 (추가 🆕 + 기존 ✅▪️)",
    f"",
] + tbl_header

for _, row in df_all.iterrows():
    md_lines.append(fmt_row(row))

# 추가 모델 vs 기존 best improved 비교 요약
if not df_others.empty:
    best_other_imp = df_others[df_others['variant'] == 'improved']['accuracy'].max() if (df_others['variant'] == 'improved').any() else 0
    best_extra_acc = df_extra['accuracy'].max() if not df_extra.empty else 0

    md_lines += [
        f"",
        f"---",
        f"",
        f"## 요약",
        f"",
        f"| 구분 | 최고 정확도 |",
        f"|------|----------:|",
        f"| 🆕 추가 4개 모델 (improved) | **{best_extra_acc:.2%}** |",
        f"| ✅ 기존 모델 (improved) best | **{best_other_imp:.2%}** |",
        f"",
    ]

    if best_extra_acc >= best_other_imp:
        diff = (best_extra_acc - best_other_imp) * 100
        md_lines.append(f"> **추가 모델이 기존 best improved 대비 +{diff:.1f}%p 높거나 동등합니다.**")
    else:
        diff = (best_other_imp - best_extra_acc) * 100
        md_lines.append(f"> 추가 모델 최고 정확도가 기존 best improved 대비 -{diff:.1f}%p 낮습니다.")

    md_lines.append(f"")

md_lines += [
    f"---",
    f"",
    f"## 성능 차트",
    f"",
    f"![추가 모델 비교 차트](extra_models_chart.png)",
    f"> 🆕 핑크 = 추가 4개 모델 | 주황 = 기존 improved | 파랑 = 기존 baseline",
    f"",
]

report_text = '\n'.join(md_lines)
report_path = BASE + 'extra_models_comparison_report.md'
with open(report_path, 'w', encoding='utf-8') as f:
    f.write(report_text)

print(f"리포트 저장: {report_path}")
print("\n완료.")
