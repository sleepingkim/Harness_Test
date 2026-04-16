"""
동일한 51편 논문 데이터를 Markdown 표 형식으로 저장
출력: 02_literature_table.md
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# build_excel.py의 papers 리스트를 그대로 import
import importlib.util
spec = importlib.util.spec_from_file_location(
    "build_excel",
    r"C:\Users\neohc\Desktop\ClaudeCode\YoungScientist\_workspace\build_excel.py"
)
mod = importlib.util.module_from_spec(spec)
# execute only data section
# Alternative: just copy paste... but simpler to re-import
try:
    spec.loader.exec_module(mod)
except Exception:
    pass

papers = mod.papers

# 섹션별 그룹핑
from collections import defaultdict
grouped = defaultdict(list)
for p in papers:
    grouped[p[1]].append(p)

lines = []
lines.append("# 축구 영상 선수 식별 + 가림 처리 문헌 정리표")
lines.append("")
lines.append(f"**총 논문 수:** {len(papers)}편  ")
lines.append("**작성일:** 2026-04-16  ")
lines.append(f"**Stage별 분포:** " + ", ".join([f"{k} ({len(v)}편)" for k, v in sorted(grouped.items())]))
lines.append("")
lines.append("> 이 문서는 `01_literature_review.md`의 48편(실제 51 entry)을 주제별 표로 재정리한 것입니다. 엑셀 버전은 `02_literature_table.xlsx`.")
lines.append("")
lines.append("---")
lines.append("")

# 각 Stage별 테이블
stage_order = ["1. 축구 MOT", "2. 가림 처리", "3. 등번호 인식", "4. Re-ID + 통합"]
for stage in stage_order:
    if stage not in grouped:
        continue
    lines.append(f"## {stage}")
    lines.append("")
    lines.append("| ID | 저자 | 제목 | 연도 | 학회/저널 | 문제 정의 | 가설/접근법 | 모델/아키텍처 | 데이터셋 | 핵심 성능 | 실험 방법 | 결론/기여점 | 가림 관련성 | URL |")
    lines.append("|----|------|------|------|----------|----------|------------|--------------|---------|----------|----------|-----------|-----------|-----|")
    for p in grouped[stage]:
        # 파이프 문자는 escape
        row = [str(x).replace("|", "\\|").replace("\n", " ") for x in p]
        # stage 컬럼 제거 (p[1]), URL은 링크로
        url = row[14]
        if url and url != "-":
            url_md = f"[link]({url})"
        else:
            url_md = "-"
        line = f"| {row[0]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} | {row[7]} | {row[8]} | {row[9]} | {row[10]} | {row[11]} | {row[12]} | {row[13]} | {url_md} |"
        lines.append(line)
    lines.append("")
    lines.append("---")
    lines.append("")

# 통계 요약
from collections import Counter
lines.append("## 통계 요약")
lines.append("")
lines.append("### Stage별 분포")
lines.append("")
lines.append("| Stage | 편수 |")
lines.append("|-------|------|")
for k, v in sorted(grouped.items()):
    lines.append(f"| {k} | {len(v)} |")
lines.append("")

year_cnt = Counter([p[4] for p in papers])
lines.append("### 연도별 분포")
lines.append("")
lines.append("| 연도 | 편수 |")
lines.append("|------|------|")
for y in sorted(year_cnt.keys()):
    lines.append(f"| {y} | {year_cnt[y]} |")
lines.append("")

occ_cnt = Counter([p[13] for p in papers])
lines.append("### 가림(Occlusion) 관련성")
lines.append("")
lines.append("| 관련성 | 편수 |")
lines.append("|--------|------|")
for k, v in occ_cnt.items():
    lines.append(f"| {k} | {v} |")
lines.append("")

out_path = r"C:\Users\neohc\Desktop\ClaudeCode\YoungScientist\_workspace\02_literature_table.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Saved: {out_path}")
print(f"Total papers: {len(papers)}")
