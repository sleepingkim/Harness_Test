# 공구 이름 표준화 LLM 프로젝트 — 핸드오프 문서

> 최종 업데이트: 2026-05-09  
> "HANDOFF.md를 읽고 이어서 진행해줘" 라고 말하면 됩니다.

---

## 현재 상태 (한눈에)

**신규 실험 2종 완료 + 논문 서술 방식 발표·포스터 파일 3종 신규 생성.**  
- RAG v2 12개 모델 실험 (GT v2 기준, 데이터 누수 없음) — 완료
- LLM-only Zero-shot 4개 모델 실험 — 완료
- 더티데이터 유형별 성능 분석 (9모델 × 10유형 교차) — 완료
- 발표 초안 + 한국어·영어 포스터 (논문 서술 방식) — 완료

> ⚠️ **프렉티컴 보고서 주의**: 기존 보고서(`프렉티컴보고서_최종본.pdf`)의 정확도 수치에 데이터 누수 가능성이 있음. 이번 세션에서 생성한 GT v2 기반 신규 실험 결과(`presentation_draft_clean.md`)를 사용할 것.

---

## 1. 실험 전체 결과 요약

### 1-1. RAG v2 — 12개 모델 (GT v2 기준, 451건 유효 평가)

| 순위 | 모델 | 버전 | 정확도 | Fallback |
|:---:|------|:---:|:------:|:--------:|
| 1 | gemma4:e4b | improved | **88.47%** | 8.14% |
| 2 | gemma3:4b | improved | 84.48% | 6.50% |
| 3 | granite4.1:8b | improved | 82.48% | 5.01% |
| 4 | gemma4:e2b | improved | 80.93% | 6.38% |
| 5 | exaone3.5:7.8b | improved | 79.16% | 9.19% |
| 6 | deepseek-r1:1.5b | improved | 78.05% | **85.20%** |
| 7 | deepseek-r1:8b | improved | 77.83% | 2.60% |
| 8 | exaone3.5:2.4b | improved | 74.06% | 13.63% |
| 9 | granite4.1:3b | improved | 67.85% | 20.76% |
| 10 | granite4.1:8b | baseline | 55.21% | 14.91% |
| 11 | deepseek-r1:8b | baseline | 55.21% | 3.76% |
| 12 | qwen3.5:9b | baseline | 0.00% | — (에러율 100%) |

> **improved**: BGE-m3-ko (1024-dim) + BM25(40%)/FAISS(60%) 하이브리드 + k=15 + 카테고리 주입  
> **baseline**: paraphrase-multilingual-MiniLM-L12-v2 (384-dim) + FAISS + k=5

### 1-2. LLM-only Zero-shot (RAG 없음, GT v2 기준, 457건)

| 모델 | exact_match | nearest_match | RAG 정확도 | RAG 기여 |
|------|:-----------:|:-------------:|:---------:|:--------:|
| gemma4:e4b | 27.4% | 63.2% | 88.5% | **+61.1pp** |
| gemma3:4b | 23.0% | 60.8% | 84.5% | **+61.5pp** |
| exaone3.5:7.8b | 9.4% | 60.4% | 79.2% | **+69.7pp** |
| deepseek-r1:1.5b | 0.0% ⚠️ | 0.7% | 78.4% | — |

> ⚠️ deepseek-r1:1.5b 0%: API 오류 아님. 한국어 자유 생성 능력 자체 부재 (중국어 출력). num_predict 조정·think:false·chat API 전환 등 모든 방법 시도 후 확인된 모델 한계.

### 1-3. 더티데이터 유형별 성능 (gemma4:e4b 기준)

| 유형 | 건수 | 비율 | RAG 정확도 | LLM-only | RAG 기여 |
|------|:---:|:---:|:----------:|:--------:|:--------:|
| 동력원 명시 | 50 | 10.9% | 96.4% | 8.0% | +88.4pp |
| 메타데이터 | 22 | 4.8% | 95.5% | 45.5% | +50.0pp |
| 속성 기입 | 40 | 8.8% | 95.0% | 55.0% | +40.0pp |
| **오탈자** | **155** | **33.9%** | **93.8%** | 21.9% | +71.9pp |
| 브랜드 혼입 | 71 | 15.5% | 87.5% | 28.2% | +59.3pp |
| 세트/구성품 | 23 | 5.0% | 84.6% | 34.8% | +49.8pp |
| 영문/약어 | 41 | 9.0% | 82.5% | 24.4% | +58.1pp |
| 기타 | 27 | 5.9% | 66.7% | 29.6% | +37.0pp |
| **일본어 잔재** | **21** | **4.6%** | **47.1%** | 19.0% | +28.0pp |

**핵심 인사이트:**
- RAG 기여도 전 모델 +61~70pp — LLM 단독으로는 실무 적용 불가
- RAG 역할 = 표기 앵커링 (지식 보완이 아님) — nearest_match 60~63% vs exact_match 9~27%
- 일본어 잔재: 전 모델·전 파이프라인에서 47% 이하 — 구조적 한계, 동의어 사전 필요

---

## 2. 이번 세션(2026-05-09)에서 생성된 파일

### 신규 분석 문서

| 파일 | 내용 |
|------|------|
| `llm_only_vs_rag_comparison.md` | LLM-only vs RAG 성능 비교 (6개 결론 포함) |
| `dirty_type_analysis_report.md` | 더티데이터 유형별 심층 분석 (9모델 × 10유형 히트맵) |
| `improvement_roadmap.md` | 성능 개선 로드맵 및 실무 적용 방안 |
| `llm_only_evaluation_rationale.md` | LLM-only 실험 필요성 근거 |
| `run_llm_only_zeroshot.py` | LLM-only 실험 실행 스크립트 |
| `analyze_llm_only.py` | LLM-only 결과 분석 스크립트 |

### LLM-only 실험 결과 CSV

| 파일 | 모델 | 비고 |
|------|------|------|
| `llm_only_zeroshot_gemma4_e4b.csv` | gemma4:e4b | 464행 (중복 7행 포함, 분석 시 GT join으로 필터) |
| `llm_only_zeroshot_exaone3_5_7_8b.csv` | exaone3.5:7.8b | 468행 |
| `llm_only_zeroshot_gemma3_4b.csv` | gemma3:4b | 457행 |
| `llm_only_zeroshot_deepseek-r1_1_5b.csv` | deepseek-r1:1.5b | 457행, llm_raw 전부 공백 |

### 발표·포스터 파일 (논문 서술 방식, 프렉티컴 독립형)

| 파일 | 내용 | 사용 권장 |
|------|------|:--------:|
| `presentation_draft_clean.md` | 13슬라이드 발표 초안, 논문 서술 | ⭐ **주력** |
| `poster_content_ko_clean.md` | 한국어 포스터 6섹션, 논문 서술 | ⭐ **주력** |
| `poster_content_en_clean.md` | 영어 포스터 6섹션, 논문 서술 | ⭐ **주력** |
| `presentation_new_analysis.md` | 유형분석+LLM-only 단독 발표 | 보조 참고 |
| `poster_new_analysis_ko.md` | 유형분석+LLM-only 단독 포스터 (KO) | 보조 참고 |
| `poster_new_analysis_en.md` | 유형분석+LLM-only 단독 포스터 (EN) | 보조 참고 |

> `*_clean.md` 파일들: 문제 정의는 프렉티컴 기반, 결과는 GT v2 신규 실험만 수록, 프렉티컴 보고서 수치와 비교 없음.

### 버전 업데이트된 기존 파일

| 파일 | 변경 내용 |
|------|---------|
| `presentation_draft_v5.md` | 섹션 6 LLM-only 추가 |
| `poster_content_ko_v3.md` | 섹션 3.3 LLM-only 추가 |
| `poster_content_v3.md` | 영문 섹션 3.3 LLM-only 추가 |
| `llm_comparison_conclusions.md` | 결론 8 추가, 종합표 확장 |
| `poster_QA.md` | Q8-1~Q8-4 추가 |

---

## 3. 핵심 파일 경로

```
_workspace5/
├── ★ presentation_draft_clean.md              ← 발표 초안 (논문 서술, 13슬라이드) ← 최신·주력
├── ★ poster_content_ko_clean.md               ← 한국어 포스터 (논문 서술)         ← 최신·주력
├── ★ poster_content_en_clean.md               ← 영어 포스터 (논문 서술)           ← 최신·주력
├── ★ dirty_type_analysis_report.md            ← 유형별 심층 분석 보고서
├── ★ llm_only_vs_rag_comparison.md            ← LLM-only vs RAG 비교 보고서
│
├── standard_tool_names_ground_truth_v2.csv    ← 정답지 v2 (457쌍)
├── performance_report.md                      ← 12개 모델 성능 비교표
├── small_models_report.md                     ← 소형 모델 중간 보고서
├── improvement_roadmap.md                     ← 성능 개선 로드맵
├── llm_only_evaluation_rationale.md           ← LLM-only 실험 필요성
│
├── checkpoint_improved_gemma4_e4b.csv         ← 최우수 모델 RAG 추론 결과
├── llm_only_zeroshot_gemma4_e4b.csv           ← 최우수 모델 LLM-only 결과
│
├── run_rag_v2_improved.py                     ← RAG 실험 실행 스크립트
├── run_llm_only_zeroshot.py                   ← LLM-only 실험 실행 스크립트
├── analyze_by_type.py                         ← 유형별 분석 스크립트
└── analyze_llm_only.py                        ← LLM-only 분석 스크립트
```

---

## 4. 기술 환경

| 항목 | 값 |
|------|-----|
| GPU | NVIDIA RTX 5080 (VRAM 17.1GB) |
| OS | Windows 11 + WSL2 (Ubuntu) |
| Python | `/home/neohc/miniconda3/bin/python` (conda base) |
| LLM 런타임 | Ollama (WSL2 내, `/usr/local/bin/ollama`) |
| 임베딩 모델 | dragonkue/BGE-m3-ko (1024차원) |
| 검색 | BM25(40%) + FAISS(60%), k=15 |
| 평가 데이터 | GT v2 (457쌍, 유효 평가 451건) |

**WSL 실행 방법:**
```powershell
wsl -- bash -c "source /home/neohc/miniconda3/etc/profile.d/conda.sh && conda activate base && python /mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5/스크립트.py 2>&1"
```

---

## 5. 추천 후속 작업 (우선순위 순)

| 순위 | 작업 | 근거 |
|------|------|------|
| ⭐ 1 | **`presentation_draft_clean.md` 기반 PPT 제작** | 논문 서술 방식의 발표 초안이 완성됨. python-pptx로 슬라이드 생성 또는 직접 편집 |
| ⭐ 2 | **일본어 동의어 사전 구축 + RAG 추가** | 기리→드릴비트, 함마→해머, 뺀치→펜치 등 20~30쌍. 일본어 잔재 47.1% → +30~40pp 예상 |
| 3 | **BM25 영문 서브워드 보강** | PIPE↔파이프 등 교차언어 매칭 실패 해결 → 영문/약어 유형 82.5% 추가 개선 |
| 4 | **Word/PDF 최종 보고서 출력** | `presentation_draft_clean.md`를 docx로 변환하여 제출용 문서 생성 |
| 5 | **대형 모델(30b, 32b) 실험 재시도** | 체크포인트 미완성 (50~250행 수준). 시간·자원 여건 확인 후 결정 |

---

## 6. 주요 발견 요약 (다음 세션 참고용)

1. **RAG 필수성**: LLM-only 9~27% → RAG 79~88% (+61~70pp). 실무 불가 → 실용 수준.
2. **표기 앵커링**: RAG의 역할은 LLM 지식 보완이 아니라, LLM이 올바른 표기로 수렴하도록 후보 풀 제공.
3. **임베딩 모델 결정적**: BGE-m3-ko 교체만으로 +22~27pp. 오탈자(33.9%, 최다)에서 93.8%.
4. **일본어 잔재 구조적 한계**: 전 모델 47% 이하. 임베딩·BM25 모두 실패. 동의어 사전 필수.
5. **deepseek-r1:1.5b 역설**: 한국어 생성 불가(0%) → RAG 결합으로 78.4%. RAG가 언어 한계 우회 가능.

---

*생성: 2026-05-09 | Claude Code 자동 업데이트*
