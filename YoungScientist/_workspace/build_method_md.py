"""
Phase 2 기법 분석 데이터를 Markdown 표로도 저장 (엑셀과 쌍)
출력: 04_method_analysis_table.md
"""
import sys, io, importlib.util
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

spec = importlib.util.spec_from_file_location(
    "bm", r"C:\Users\neohc\Desktop\ClaudeCode\YoungScientist\_workspace\build_method_excel.py"
)
bm = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(bm)
except Exception:
    pass

methods = bm.methods
combinations = bm.combinations
gaps = bm.gaps

lines = []
lines.append("# Phase 2 기법 심층 분석 정리표")
lines.append("")
lines.append(f"**작성일:** 2026-04-16  ")
lines.append(f"**선별 기법:** {len(methods)}개  ")
lines.append(f"**조합 파이프라인:** {len(combinations)}개  ")
lines.append(f"**연구 공백 매핑:** {len(gaps)}개  ")
lines.append("")
lines.append("> 본 문서는 `03_method_analysis.md` 본문의 데이터를 표로 재정리한 것. 엑셀 버전은 `04_method_analysis_table.xlsx`.")
lines.append("")
lines.append("---")
lines.append("")

# ---- Sheet 1 ----
lines.append("## 1. 선별 기법 20개 (5차원 평가)")
lines.append("")
lines.append("| ID | 기법명 | 카테고리 | 원논문 | 핵심 아이디어 | 축구 전이성 | 정확도 | 가림 | 실시간 | 단일카메라 | 조합성 | **총점** |")
lines.append("|----|--------|---------|-------|--------------|-----------|--------|------|-------|-----------|--------|---------|")
for m in methods:
    score_mark = f"**{m[12]}**" if m[12] >= 24 else str(m[12])
    row = f"| {m[0]} | {m[1]} | {m[2]} | {m[3]} | {m[4]} | {m[6]} | {m[7]} | {m[8]} | {m[9]} | {m[10]} | {m[11]} | {score_mark} |"
    lines.append(row)
lines.append("")
lines.append("**총점 24+ 기법:** M4 OC-SORT (25), M7 ByteTrack (25), M1 Repulsion Loss (24), M12 Deep OC-SORT (24), M18 StrongSORT+AFLink (24), M19 GTA-Link (24)")
lines.append("")
lines.append("### 1.1 축구 전이 도전과제 (상세)")
lines.append("")
lines.append("| ID | 기법명 | 축구 전이 도전과제 | 예상 성능 |")
lines.append("|----|--------|-------------------|----------|")
for m in methods:
    lines.append(f"| {m[0]} | {m[1]} | {m[13]} | {m[14]} |")
lines.append("")
lines.append("---")
lines.append("")

# ---- Sheet 2 ----
lines.append("## 2. 조합 파이프라인 4개")
lines.append("")
lines.append("| 조합명 | 파이프라인 구성 | 기대 시너지 | 예상 성능 | 난이도 | 필요 자원 |")
lines.append("|--------|----------------|------------|----------|--------|----------|")
for c in combinations:
    lines.append(f"| {c[0]} | {c[1]} | {c[2]} | {c[3]} | {c[4]} | {c[5]} |")
lines.append("")
lines.append("---")
lines.append("")

# ---- Sheet 3 ----
lines.append("## 3. 연구 공백 × 기법 매핑")
lines.append("")
lines.append("| 연구 공백 | 상세 설명 | 적용 가능 기법 | 결합 전략 |")
lines.append("|----------|----------|--------------|----------|")
for g in gaps:
    lines.append(f"| {g[0]} | {g[1]} | {g[2]} | {g[3]} |")
lines.append("")
lines.append("---")
lines.append("")

# ---- 권장 방향 ----
lines.append("## 4. Phase 3 권장 연구 방향")
lines.append("")
lines.append("| 순위 | 방향 | 조합 기반 | 해결 공백 |")
lines.append("|------|------|----------|----------|")
lines.append("| 1순위 | **Amodal + Uniform-aware Soccer Tracker** | 조합 3 | ①②③ 동시 |")
lines.append("| 보조 | Occlusion-Aware Tracklet Uncertainty Propagation | 조합 3 흡수 | ③ |")
lines.append("| 대안 | Long-term Identity Consistency via Multi-modal Gallery | 조합 4 | ④ |")
lines.append("")

out = r"C:\Users\neohc\Desktop\ClaudeCode\YoungScientist\_workspace\04_method_analysis_table.md"
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Saved: {out}")
