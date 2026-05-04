"""
소형 우선 모델 6개 (deepseek-r1:1.5b, exaone3.5:2.4b, granite4.1:3b, gemma3:4b, exaone3.5:7.8b, gemma4:e2b) 비교 리포트
기존 완료 모델(deepseek-r1:8b, granite4.1:8b baseline/improved)과 함께 비교
실행: /home/neohc/miniconda3/bin/python generate_small_report.py
출력: small_models_report.md  +  small_models_chart.png
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

SMALL_MODEL_SAVE_NAMES = {
    'deepseek-r1_1_5b',
    'exaone3_5_2_4b',
    'granite4_1_3b',
    'gemma3_4b',
    'exaone3_5_7_8b',
    'gemma4_e2b',
}

SMALL_MODEL_DISPLAY = {
    'deepseek-r1_1_5b': 'deepseek-r1:1.5b',
    'exaone3_5_2_4b':   'exaone3.5:2.4b',
    'granite4_1_3b':    'granite4.1:3b',
    'gemma3_4b':        'gemma3:4b',
    'exaone3_5_7_8b':   'exaone3.5:7.8b',
    'gemma4_e2b':       'gemma4:e2b',
}

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
            return prop
    return None

set_korean_font()

result_files = sorted([
    f for f in os.listdir(BASE)
    if f.startswith('New_RAG_v2_') and f.endswith('_3352.csv')
])

if not result_files:
    print("[오류] 완료된 결과 파일 없음.")
    exit()

df_gt  = pd.read_csv(GT_PATH)
gt_map = df_gt.set_index('original_name')['standard_name'].to_dict()

def extract_save_name(fname):
    name = fname.replace('New_RAG_v2_', '').replace('_3352.csv', '')
    # 접두사 방식: improved_MODEL 또는 baseline_MODEL
    if name.startswith('improved_'):
        name = name[len('improved_'):]
    elif name.startswith('baseline_'):
        name = name[len('baseline_'):]
    # 접미사 방식: MODEL_improved 또는 MODEL_baseline
    name = name.replace('_improved', '').replace('_baseline', '')
    return name

def load_record(fname):
    df    = pd.read_csv(BASE + fname)
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
    else:
        df['gt'] = df['Input_Name'].map(gt_map)
        ev = df[df['gt'].notna()].copy()
        n_eval = len(ev)
        ev['correct'] = ev.apply(
            lambda r: str(r.get('standard_name', '')).strip() == str(r['gt']).strip(), axis=1)
        n_correct     = int(ev['correct'].sum())
        accuracy      = n_correct / n_eval if n_eval > 0 else 0.0
        fallback_rate = df.get('fallback_used', pd.Series([False]*total)).fillna(False).astype(bool).mean()
        error_rate    = (df['status'] == 'error').mean() if 'status' in df.columns else 0.0
        speed = llm_sec = None

    save_name = extract_save_name(fname)
    variant   = 'improved' if 'improved' in fname else 'baseline'
    is_small  = save_name in SMALL_MODEL_SAVE_NAMES

    return {
        'model':         model_display,
        'variant':       variant,
        'label':         f"{model_display} [{variant}]",
        'total':         total,
        'eval_count':    int(n_eval),
        'correct':       int(n_correct),
        'accuracy':      accuracy,
        'fallback_rate': fallback_rate,
        'error_rate':    error_rate,
        'speed':         speed,
        'llm_sec':       llm_sec,
        'is_small':      is_small,
    }

all_records = [load_record(f) for f in result_files]
df_all = pd.DataFrame(all_records).sort_values('accuracy', ascending=False).reset_index(drop=True)
df_all['rank'] = df_all.index + 1

df_small  = df_all[df_all['is_small']].reset_index(drop=True)
df_others = df_all[~df_all['is_small']].reset_index(drop=True)

print(f"소형 모델 결과: {len(df_small)}개")
for _, r in df_small.sort_values('accuracy', ascending=False).iterrows():
    print(f"  {r['label']}: {r['accuracy']:.2%}")

if df_small.empty:
    print("\n[경고] 소형 모델 결과 없음.")
    exit()

# ===== 차트 =====
COLOR_SMALL = '#E91E63'
COLOR_IMP   = '#FF9800'
COLOR_BASE  = '#2196F3'

def row_color(row):
    if row['is_small']:   return COLOR_SMALL
    if row['variant'] == 'improved': return COLOR_IMP
    return COLOR_BASE

fig, axes = plt.subplots(1, 2, figsize=(max(16, (len(df_small) + len(df_others)) * 1.2), 8))
fig.suptitle('소형 우선 모델 4개 vs 기존 모델 — 정확도 비교', fontsize=14, fontweight='bold')

for ax_idx, (df_sub, title) in enumerate([
    (df_small,                           '소형 우선 4개 모델'),
    (df_all.sort_values('accuracy', ascending=False).reset_index(drop=True), '전체 비교'),
]):
    ax = axes[ax_idx]
    lbls   = df_sub['label'].tolist()
    accs   = [a * 100 for a in df_sub['accuracy'].tolist()]
    colors = [row_color(r) for _, r in df_sub.iterrows()]

    bars = ax.barh(range(len(lbls)), accs, color=colors)
    ax.set_yticks(range(len(lbls)))
    ax.set_yticklabels(lbls, fontsize=8)
    ax.set_xlabel('정확도 (%)')
    ax.set_title(title)
    ax.set_xlim(0, 110)

    for bar, acc in zip(bars, accs):
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
                f'{acc:.1f}%', va='center', fontsize=7, fontweight='bold')

    ax.legend(handles=[
        Patch(color=COLOR_SMALL, label='소형 우선 모델 (improved)'),
        Patch(color=COLOR_IMP,   label='기존 improved'),
        Patch(color=COLOR_BASE,  label='기존 baseline'),
    ], loc='lower right', fontsize=8)

plt.tight_layout()
chart_path = BASE + 'small_models_chart.png'
plt.savefig(chart_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"차트 저장: {chart_path}")

# ===== Markdown 리포트 =====
now = datetime.now().strftime('%Y-%m-%d %H:%M')

tbl_header = [
    "| 순위 | 모델 (variant) | 정확도 | 평가 건수 | 정답 건수 | Fallback율 | 에러율 | 처리속도 | LLM 소요시간 |",
    "|:----:|---------------|-------:|--------:|--------:|---------:|------:|-------:|----------:|",
]

def fmt_row(row, show_rank=True):
    speed_str = f"{row['speed']:.2f}건/초" if row.get('speed') else "-"
    llm_str   = str(timedelta(seconds=int(row['llm_sec']))) if row.get('llm_sec') else "-"
    tag = '🔹' if row['is_small'] else ('✅' if row['variant'] == 'improved' else '▪️')
    rank_part = f"{int(row['rank'])} | " if show_rank else ""
    return (f"| {rank_part}{tag} `{row['model']}` ({row['variant']}) "
            f"| **{row['accuracy']:.2%}** "
            f"| {int(row['eval_count'])} "
            f"| {int(row['correct'])} "
            f"| {row['fallback_rate']:.2%} "
            f"| {row['error_rate']:.2%} "
            f"| {speed_str} "
            f"| {llm_str} |")

md_lines = [
    f"# 소형 우선 모델 6개 vs 기존 완료 모델 — 중간 성능 비교 리포트",
    f"",
    f"> 생성: {now}  ",
    f"> 소형 우선 모델: deepseek-r1:1.5b · exaone3.5:2.4b · granite4.1:3b · gemma3:4b · exaone3.5:7.8b · gemma4:e2b (improved only)  ",
    f"> 기존 완료 모델: deepseek-r1:8b · granite4.1:8b (baseline + improved)  ",
    f"> 정제 대상: 3,352개 | 평가 기준: ground_truth_v2.csv ({len(gt_map)}개)  ",
    f"",
    f"---",
    f"",
    f"## 소형 우선 모델 성능 (🔹) — 6개",
    f"",
] + tbl_header

for _, row in df_small.sort_values('accuracy', ascending=False).iterrows():
    md_lines.append(fmt_row(row, show_rank=False))

# 요약 비교
best_small = df_small['accuracy'].max() if not df_small.empty else 0
best_imp   = df_others[df_others['variant'] == 'improved']['accuracy'].max() \
             if (df_others['variant'] == 'improved').any() else 0

md_lines += [
    f"",
    f"---",
    f"",
    f"## 요약",
    f"",
    f"| 구분 | 최고 정확도 |",
    f"|------|----------:|",
    f"| 🔹 소형 우선 4개 (improved) | **{best_small:.2%}** |",
    f"| ✅ 기존 improved best | **{best_imp:.2%}** |",
    f"",
]

diff = (best_small - best_imp) * 100
if diff >= 0:
    md_lines.append(f"> 소형 모델 최고 정확도가 기존 improved best 대비 **+{diff:.1f}%p** 높거나 동등합니다.")
else:
    md_lines.append(f"> 소형 모델 최고 정확도가 기존 improved best 대비 **{diff:.1f}%p** 낮습니다.")

md_lines += [
    f"",
    f"---",
    f"",
    f"## 전체 순위 (소형 🔹 포함)",
    f"",
] + tbl_header

for _, row in df_all.iterrows():
    md_lines.append(fmt_row(row))

md_lines += [
    f"",
    f"---",
    f"",
    f"## 성능 차트",
    f"",
    f"![소형 모델 비교 차트](small_models_chart.png)",
    f"> 🔹 핑크 = 소형 우선 모델 | 주황 = 기존 improved | 파랑 = 기존 baseline",
    f"",
]

report_path = BASE + 'small_models_report.md'
with open(report_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))

print(f"리포트 저장: {report_path}")
print("완료.")
