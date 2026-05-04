"""
모델별 정제 결과 성능 비교 리포트 생성
실행: /home/neohc/miniconda3/bin/python generate_report.py
출력: performance_report.md  +  performance_chart.png
"""

import os
import json
import re
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import datetime, timedelta

BASE   = '/mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5/'
GT_PATH = BASE + 'standard_tool_names_ground_truth_v2.csv'

# ===== 한글 폰트 설정 =====
KOREAN_FONT = None

def set_korean_font():
    global KOREAN_FONT
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
            name = prop.get_name()
            matplotlib.rcParams['font.family'] = name
            matplotlib.rcParams['axes.unicode_minus'] = False
            KOREAN_FONT = prop
            print(f"한글 폰트: {path} ({name})")
            return prop
    print("한글 폰트 없음 - 기본 폰트 사용")
    return None

set_korean_font()

# ===== 결과 CSV 자동 탐색 (기본 + 개선 버전 모두) =====
result_files = sorted([
    f for f in os.listdir(BASE)
    if f.startswith('New_RAG_v2_') and f.endswith('_3352.csv')
])
print(f"\n발견된 결과 파일: {len(result_files)}개")
for f in result_files:
    tag = '[improved]' if 'improved' in f else '[baseline]'
    print(f"  {tag} {f}")

if not result_files:
    print("[오류] 완료된 결과 파일 없음. 스크립트 종료.")
    exit()

# ===== ground truth 로드 =====
df_gt  = pd.read_csv(GT_PATH)
gt_map = df_gt.set_index('original_name')['standard_name'].to_dict()

# ===== 모델별 성능 계산 =====
records = []

for fname in result_files:
    df = pd.read_csv(BASE + fname)
    total = len(df)

    # stats JSON 우선 로드
    stats_fname = fname.replace('_3352.csv', '_stats.json')
    stats = {}
    if os.path.exists(BASE + stats_fname):
        with open(BASE + stats_fname, 'r', encoding='utf-8') as f:
            stats = json.load(f)

    # 모델명: model_name 컬럼 > stats JSON > 파일명 파싱
    if 'model_name' in df.columns:
        model_display = str(df['model_name'].iloc[0])
    elif stats.get('model_name'):
        model_display = stats['model_name']
    else:
        model_raw = fname.replace('New_RAG_v2_', '').replace('_3352.csv', '')
        model_display = model_raw.replace('_', '-').replace('hf-co-', 'hf.co/')

    # stats JSON 있으면 바로 사용
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
        fallback_col  = df.get('fallback_used', pd.Series([False] * total))
        fallback_rate = fallback_col.fillna(False).astype(bool).mean()
        error_rate    = (df['status'] == 'error').mean() if 'status' in df.columns else 0.0
        speed         = None
        llm_sec       = None
        embed_sec     = None

    variant = 'improved' if 'improved' in fname else 'baseline'
    embed_model_name = stats.get('embed_model', 'paraphrase-multilingual-MiniLM-L12-v2')
    k_value = stats.get('k_value', 5)

    records.append({
        'model':            model_display,
        'variant':          variant,
        'label':            f"{model_display} [{variant}]",
        'embed_model':      embed_model_name.split('/')[-1],
        'k_value':          k_value,
        'total':            total,
        'eval_count':       int(n_eval),
        'correct':          int(n_correct),
        'accuracy':         accuracy,
        'fallback_rate':    fallback_rate,
        'error_rate':       error_rate,
        'speed':            speed,
        'llm_sec':          llm_sec,
        'embed_sec':        embed_sec,
    })

df_report = pd.DataFrame(records).sort_values('accuracy', ascending=False).reset_index(drop=True)
df_report['rank'] = df_report.index + 1

print("\n=== 성능 비교 ===")
print(df_report[['rank', 'label', 'accuracy', 'fallback_rate', 'error_rate']].to_string(index=False))

# ===== 차트 생성 (baseline=파랑, improved=주황) =====
labels    = df_report['label'].tolist()
accs      = df_report['accuracy'].tolist()
fallbacks = df_report['fallback_rate'].tolist()
bar_colors = ['#2196F3' if v == 'baseline' else '#FF9800'
              for v in df_report['variant'].tolist()]

fig, axes = plt.subplots(1, 2, figsize=(max(14, len(labels) * 1.8), 7))
fig.suptitle('RAG v2 공구명 정제 성능 비교 (baseline vs improved)', fontsize=14, fontweight='bold')

# (왼쪽) 정확도
ax1 = axes[0]
bars1 = ax1.barh(range(len(labels)), [a * 100 for a in accs], color=bar_colors)
ax1.set_yticks(range(len(labels)))
ax1.set_yticklabels(labels, fontsize=8)
ax1.set_xlabel('정확도 (%)')
ax1.set_title('정확도 (Accuracy)')
ax1.set_xlim(0, 105)
for bar, acc in zip(bars1, accs):
    ax1.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
             f'{acc:.1%}', va='center', fontsize=8, fontweight='bold')

# 범례
from matplotlib.patches import Patch
ax1.legend(handles=[Patch(color='#2196F3', label='baseline'),
                     Patch(color='#FF9800', label='improved')],
           loc='lower right', fontsize=8)

# (오른쪽) Fallback 비율
ax2 = axes[1]
bars2 = ax2.barh(range(len(labels)), [f * 100 for f in fallbacks],
                  color=bar_colors, alpha=0.85)
ax2.set_yticks(range(len(labels)))
ax2.set_yticklabels(labels, fontsize=8)
ax2.set_xlabel('Fallback 비율 (%)')
ax2.set_title('Fallback 비율 (낮을수록 좋음)')
ax2.set_xlim(0, 100)
for bar, fb in zip(bars2, fallbacks):
    ax2.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
             f'{fb:.1%}', va='center', fontsize=8)

plt.tight_layout()
chart_path = BASE + 'performance_chart.png'
plt.savefig(chart_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"\n차트 저장: {chart_path}")

# ===== Markdown 리포트 생성 =====
now = datetime.now().strftime('%Y-%m-%d %H:%M')

md_lines = [
    f"# RAG v2 공구명 정제 — 모델 성능 비교 리포트",
    f"",
    f"> 생성: {now}  ",
    f"> 정제 대상: ToolNameData.csv (3,352개)  ",
    f"> 평가 기준: standard_tool_names_ground_truth_v2.csv ({len(gt_map)}개 정답 쌍)  ",
    f"> RAG 지식베이스: standard_name {len(df_gt['standard_name'].unique())}종 목록 (original_name 매핑 제외)  ",
    f"",
    f"---",
    f"",
    f"## 성능 비교 표",
    f"",
    f"| 순위 | 모델 (variant) | 임베딩 모델 | K값 | 정확도 | 평가 건수 | 정답 건수 | Fallback율 | 에러율 | 처리속도 | LLM 소요시간 |",
    f"|:----:|---------------|-----------|:---:|-------:|--------:|--------:|---------:|------:|-------:|----------:|",
]

for _, row in df_report.iterrows():
    speed_str = f"{row['speed']:.2f}건/초" if row.get('speed') else "-"
    llm_str   = str(timedelta(seconds=int(row['llm_sec']))) if row.get('llm_sec') else "-"
    variant_icon = '✅' if row['variant'] == 'improved' else '▪️'
    md_lines.append(
        f"| {int(row['rank'])} | {variant_icon} `{row['model']}` ({row['variant']}) "
        f"| `{row['embed_model']}` "
        f"| {row.get('k_value', 5)} "
        f"| **{row['accuracy']:.2%}** "
        f"| {int(row['eval_count'])} "
        f"| {int(row['correct'])} "
        f"| {row['fallback_rate']:.2%} "
        f"| {row['error_rate']:.2%} "
        f"| {speed_str} "
        f"| {llm_str} |"
    )

md_lines += [
    f"",
    f"---",
    f"",
    f"## 성능 차트",
    f"",
    f"![성능 비교 차트](performance_chart.png)",
    f"> 파란 막대 = baseline | 주황 막대 = improved",
    f"",
    f"---",
    f"",
    f"## 모델별 상세",
    f"",
]

for _, row in df_report.iterrows():
    speed_str = f"{row['speed']:.2f}건/초" if row.get('speed') else "-"
    llm_str   = str(timedelta(seconds=int(row['llm_sec']))) if row.get('llm_sec') else "-"
    embed_str = f"{row['embed_sec']:.1f}초" if row.get('embed_sec') else "-"
    variant_icon = '✅ improved' if row['variant'] == 'improved' else '▪️ baseline'
    md_lines += [
        f"### {int(row['rank'])}위. `{row['model']}` — {variant_icon}",
        f"",
        f"- **임베딩 모델**: `{row['embed_model']}` | **K값**: {row.get('k_value', 5)}",
        f"- **정확도**: {row['accuracy']:.2%} ({int(row['correct'])}/{int(row['eval_count'])}건)",
        f"- **처리 속도**: {speed_str} | **LLM 추론 시간**: {llm_str} | **임베딩 시간**: {embed_str}",
        f"- **Fallback**: {row['fallback_rate']:.2%} | **에러율**: {row['error_rate']:.2%}",
        f"",
    ]

md_lines += [
    f"---",
    f"",
    f"## 개선 방법 설명 (improved 버전)",
    f"",
    f"| # | 개선 항목 | 내용 |",
    f"|---|-----------|------|",
    f"| 1 | **임베딩 모델 교체** | `paraphrase-multilingual-MiniLM-L12-v2` → `dragonkue/BGE-m3-ko` (한국어 KURE 리더보드 1위) |",
    f"| 2 | **BM25+FAISS 하이브리드** | 음절 bigram BM25(40%) + FAISS 시맨틱(60%) 혼합 검색 |",
    f"| 3 | **K값 확대** | 후보 5개 → 15개 |",
    f"| 4 | **카테고리 주입** | ToolNameData의 Categories / SubCategories 정보를 프롬프트에 포함 |",
    f"",
    f"---",
    f"",
    f"## 용어 설명",
    f"",
    f"- **정확도**: ground_truth_v2의 original_name 매핑 standard_name과 예측값 일치율",
    f"- **Fallback**: LLM이 후보 외 답변 → RAG top-1으로 강제 대체된 비율",
    f"- **RAG 지식베이스**: standard_name 160종 목록만 사용 (original_name→standard_name 매핑 미포함)",
    f"",
]

report_text = '\n'.join(md_lines)
report_path = BASE + 'performance_report.md'
with open(report_path, 'w', encoding='utf-8') as f:
    f.write(report_text)

print(f"리포트 저장: {report_path}")
print("\n완료.")
