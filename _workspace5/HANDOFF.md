# 공구 이름 표준화 LLM 프로젝트 — 핸드오프 문서

> 최종 업데이트: 2026-05-05
> "HANDOFF.md를 읽고 이어서 진행해줘" 라고 말하면 됩니다.

---

## 현재 상태 (한눈에)

**모든 실험 완료. 보고서·발표초안·PPT까지 산출물 생성 완료.**
다음 세션에서 할 수 있는 작업은 맨 아래 "추천 후속 작업" 참고.

---

## 1. 완료된 작업 전체 요약

### 1-1. RAG v2 실험 (9개 모델, 전부 완료)

| 모델 | 방식 | 정확도 | 속도 |
|------|------|------:|----:|
| gemma4:e4b | improved | **88.47%** | 1.58개/초 |
| gemma3:4b | improved | 84.48% | 1.77개/초 |
| granite4.1:8b | improved | 82.48% | 1.21개/초 |
| gemma4:e2b | improved | 80.93% | 1.93개/초 |
| exaone3.5:7.8b | improved | 79.16% | 1.23개/초 |
| deepseek-r1:1.5b | improved | 78.05% | 1.49개/초 |
| deepseek-r1:8b | improved | 77.83% | 1.40개/초 |
| exaone3.5:2.4b | improved | 74.06% | 1.58개/초 |
| granite4.1:3b | improved | 67.85% | 1.53개/초 |
| deepseek-r1:8b | baseline | 55.21% | 기준선 |
| granite4.1:8b | baseline | 55.21% | 기준선 |

> Baseline 55% → Improved 88.47% (+33.26%p)
> VRAM 17.1GB 초과 대형 모델(32b, 30b)은 CPU 오프로드로 0.03개/초 → 실험 제외

### 1-2. 오류 유형 분석 (신규 — 이번 세션에서 완료)

- **분석 대상**: 9개 모델 전체 오답 842건
- **핵심 발견**:
  - RAG 후보 누락: ~25건 고정 (모든 모델 공통 → 구조적 문제)
  - LLM 오선택: 23건(gemma4:e4b) ~ 120건(granite4.1:3b) — 5배 차이
- **gemma4:e4b 오답 52건 세부 분류**:
  - RAG 검색 실패 46.2% / 완전 다른 공구 선택 23.1% / 세트·단품 혼동 13.5%
  - 동력원 분류 오류 7.7% / 본체·부속품 혼동 7.7%
- **자주 틀리는 패턴**: 몽키스패너→스패너, 노기스(RAG 누락), L렌치세트→T렌치세트

### 1-3. 생성된 보고서·문서

| 파일 | 내용 |
|------|------|
| `performance_report.md` | 전체 모델 성능 비교 보고서 |
| `practicum_report_update.md` | 프렉티컴 보고서 업데이트 (RAG v1 한계 + v2 결과) |
| `practicum_report_update.docx` | 위 문서의 Word 버전 |
| `presentation_draft.md` | 발표 초안 v1 (수치 위주, 근거 부족) |
| `presentation_draft_annotated.md` | 발표 초안 v2 (참고문헌 주석 포함, 🔵🔴🟡 마커) |
| `presentation_draft_v3.md` | **발표 초안 v3 (최신)** — 오류 분석 섹션 추가 + 인라인 인용 정리 |
| `발표초안_v1.pptx` | PPT 14장 자동 생성 (python-pptx) |
| `error_analysis_result.csv` | 전체 오답 842건 유형 분류 데이터 |
| `error_analysis_v2.xlsx` | 위 내용 Excel 9시트 (모델별 교차 분석 포함) |

---

## 2. 핵심 파일 경로

```
_workspace5/
├── ★ 발표초안_v1.pptx                         ← PPT 최신본 (14장)
├── ★ presentation_draft_v3.md                 ← 발표 원고 최신본 (7섹션)
├── ★ error_analysis_v2.xlsx                   ← 오류 분석 Excel (9시트)
├── error_analysis_result.csv                  ← 오답 842건 원본 데이터
├── practicum_report_update.docx               ← 프렉티컴 보고서 Word
├── New_RAG_v2_improved_gemma4_e4b_3352.csv    ← 최우수 모델 추론 결과
├── standard_tool_names_ground_truth_v2.csv    ← 정답지 (457개)
├── run_rag_v2_improved.py                     ← 실험 실행 스크립트
├── error_analysis.py                          ← 오류 분석 스크립트
├── generate_ppt.py                            ← PPT 생성 스크립트
├── generate_report.py                         ← 성능 보고서 생성
└── generate_practicum_update.py               ← 프렉티컴 보고서 생성
```

---

## 3. 기술 환경

| 항목 | 값 |
|------|-----|
| GPU | NVIDIA RTX 5080 (VRAM 17.1GB) |
| OS | Windows 11 + WSL2 (Ubuntu) |
| Python | `/home/neohc/miniconda3/bin/python` (conda base) |
| LLM 런타임 | Ollama (WSL2 내) |
| 임베딩 모델 | dragonkue/BGE-m3-ko (1024차원) |
| 검색 | FAISS(60%) + BM25(40%), k=15 |
| 평가 데이터 | 457개 정답지 (3,352건 중 13.6%) |

**WSL 실행 방법:**
```powershell
wsl -e bash -c "source /home/neohc/miniconda3/etc/profile.d/conda.sh && conda activate base && python /mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5/스크립트.py 2>&1"
```

---

## 4. 추천 후속 작업 (우선순위 순)

| 순위 | 작업 | 이유 |
|------|------|------|
| ⭐ 1 | **PPT 내용 검토 및 수정** | 발표초안_v1.pptx 열어서 텍스트·레이아웃 다듬기 |
| ⭐ 2 | **일본어 잔재 전처리 레이어 추가** | '노기스', '기리' 등 RAG 검색 실패 ~25건 구조 해결 |
| ⭐ 3 | **세트/단품 특화 프롬프트 실험** | 오답의 13.5%가 세트·단품 혼동 → 프롬프트로 개선 가능 |
| 4 | 정답지 확장 (457 → 전체) | 현재 평가 대표성 13.6%로 낮음 |
| 5 | 파인튜닝 vs RAG 비교 실험 | 더 높은 정확도 탐색 |
| 6 | presentation_draft_v3.md 기반 최종 발표 원고 다듬기 | 내용 확정 후 Word/PDF 출력 |

---

## 5. 발표 초안 v3 구성 (섹션별)

1. 데이터 정제는 왜 병목인가 (더티데이터 유형 + 수작업 한계)
2. LLM+RAG로 어떻게 해결하는가 (파이프라인 + v1 한계 극복)
3. 왜 로컬 LLM이어야 하는가 (보안·비용·안정성·커스터마이징)
4. 속도 vs 정확도 트레이드오프 (9개 모델 + MAUT α 분석)
5. **LLM은 어디서 실수하는가 — 오류 유형 분석** ← 이번 세션 신규 추가
6. 실제 업무에 적용한다면 (로드맵 + 기대 효과)
7. 결론 및 제언

---

*생성: 2026-05-05 | Claude Code 자동 업데이트*
