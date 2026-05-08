# mHealth_biomarker_research — 폴더 맥락 설명

> 이 파일은 Claude 대화 재시작 시 빠른 맥락 복원을 위해 작성되었습니다.  
> 최종 업데이트: 2026-05-08

---

## 연구 목표

스마트폰 카메라·마이크로 수집한 **얼굴 영상 / 음성 데이터**를 활용하여  
**PCOS(다낭성난소증후군)·자궁내막증(Endometriosis)**을 AI로 예측하기 위한  
**디지털 바이오마커**를 발굴·검증하고, 공동연구 데이터 제안서 및 IEEE 논문을 작성하는 전체 연구 파이프라인.

---

## 폴더 구조 및 각 workspace 요약

### _workspace1 — 초기 바이오마커 탐색 + 카메라 바이오마커 연구
| 파일 | 내용 |
|------|------|
| `01_literature_review.md` | 자궁내막증/PCOS 디지털 바이오마커 체계적 문헌 탐색 (HRV, 수면, 월경주기 앱, 자가보고 등) |
| `02_biomarker_catalog.md` | Known 바이오마커 분류·평가 카탈로그 |
| `03_novel_proposals.md` | 병태생리학 기반 신규 바이오마커 제안 |
| `04_data_proposal.md` | 공동연구 데이터 제안서 (한국어) |
| `05_visual_biomarker_literature.md` | 시각(영상) 바이오마커 추가 문헌 탐색 |
| `06_novel_visual_proposals.md` | 신규 시각 바이오마커 제안 |
| `07_visual_biomarker_report.md` | 시각 바이오마커 종합 보고서 |
| `camera/01_camera_literature_review.md` | 스마트폰 카메라 기반 바이오마커 문헌 탐색 (rPPG, 안구 추적, 피부 분석 등) |
| `camera/02_camera_synthesis.md` | 카메라 바이오마커 합성 보고서 + .docx |
| `camera/reference_validation_report.md` | 참고문헌 할루시네이션 검증 결과 |
| `camera/ieee_paper/` | IEEE LaTeX 논문 초안 (main.tex, references.bib) |

**핵심 바이오마커**: HRV(심박변이도), 수면 패턴, 월경주기 변동성, rPPG, 안구 혈관 분석, 피부 색조

---

### _workspace2 — PCOS·자궁내막증 특화 스마트폰 카메라 바이오마커 연구
| 파일 | 내용 |
|------|------|
| `01_literature_review.md` | PCOS·자궁내막증에 특화된 카메라 기반 바이오마커 문헌 탐색 (K-Dense API 활용, PubMed/OpenAlex) |
| `02_research_design.md` | 연구 설계서 (RQ, 가설, 변수 정의, 실험 계획) |
| `03_biomarker_synthesis.md` | 바이오마커 합성 보고서 |
| `paper_summary.md` | 주요 논문 요약 |
| `reference_validation_report.md` | 참고문헌 검증 |
| `ieee_paper/` | IEEE LaTeX 논문 |
| `glossary.md` | 핵심 용어 정의 |

**핵심 내용**: PCOS Rotterdam 기준 vs. 카메라 바이오마커 매핑, 자율신경계(HRV) → PCOS 연계, 얼굴 피부 분석(안드로겐 지표)

---

### _workspace3 — 얼굴·음성 바이오마커 문헌 탐색 및 합성 (핵심 workspace)
| 파일 | 내용 |
|------|------|
| `01_face_biomarker_literature.md` | **얼굴 영상 기반 질병 예측 문헌 50편** (피부/여드름, 황달, 노화, 결막/빈혈, 갑상선, 표정/PD/우울, 뇌졸중, 내분비 등) |
| `02_voice_biomarker_literature.md` | **음성 기반 질병 예측 문헌 43편** (신경계, 정신건강, 호흡기, 호르몬, 음성질환 등, 한국어 7편 포함) |
| `03_synthesis.md` | 얼굴+음성 통합 합성 보고서 |
| `reference_validation_face.md` | 얼굴 바이오마커 참고문헌 검증 (✅ 74%, ⚠️ 10%, ❓ 16%, ❌ 0%) |
| `reference_validation_voice.md` | 음성 바이오마커 참고문헌 검증 (✅ 72%, ⚠️ 23%, ❌ 0%) |

**가장 풍부한 데이터 소스** — 얼굴 영상/음성 기반 질병 예측 논문 상세 정보 수록

---

### _workspace4 — 얼굴·음성 데이터 수집 UX 방법론 연구
| 파일 | 내용 |
|------|------|
| `01_ux_methodology_literature.md` | HCI·mHealth·산업공학 UX 문헌 탐색 (41편) — 얼굴 사진·음성 수집 UX, 동의, 품질 관리 |
| `02_ux_synthesis.md` | UX 설계 가이드라인 합성 보고서 (7개 핵심 원칙) |
| `04_korean_voice_literature.md` | 한국어 음성 바이오마커 추가 문헌 탐색 |
| `04_korean_voice_synthesis.md` | 한국어 음성 탐색 결과 합성 |
| `05_ux_synthesis_ko_integrated.md` | 한국어 통합 UX 합성 보고서 |
| `06_voice_feature_extraction.md` | 음성 특징 추출 방법론 (GeMAPS, MFCCs, jitter, shimmer 등) |
| `07_GeMAPS_paper_summary.md` | GeMAPS 표준 음성 특징셋 논문 요약 |
| `reference_validation_ux.md` | UX 문헌 참고문헌 검증 |

**핵심 내용**: 캡처-시점 품질 게이트, 계층적 동의 설계, 표준화된 발화 프로토콜, 부담 적응형 EMA

---

## 연구 파이프라인 전체 흐름

```
1. 디지털 바이오마커 문헌 탐색 (_workspace1, _workspace2)
   → PCOS·자궁내막증 예측 Known 바이오마커 목록

2. 얼굴·음성 바이오마커 상세 탐색 (_workspace3)
   → 얼굴 50편 + 음성 43편 논문 상세 분석

3. 데이터 수집 UX 설계 방법론 탐색 (_workspace4)
   → 스마트폰 앱에서 실제 데이터 수집 프로토콜 설계

4. 통합 산출물
   → 공동연구 데이터 제안서 (_workspace1/04_data_proposal.md)
   → IEEE LaTeX 논문 (_workspace1/camera/ieee_paper/, _workspace2/ieee_paper/)
```

---

## 주요 디지털 바이오마커 목록

| 데이터 모달리티 | 바이오마커                                           | 관련 질환        |
| -------- | ----------------------------------------------- | ------------ |
| 얼굴 영상    | 피부 안드로겐 지표(여드름, 모공, 피지), rPPG(HRV, 맥박)          | PCOS         |
| 얼굴 영상    | 결막 색상(빈혈), 황달 지표, 눈 충혈 패턴                       | 전신 질환        |
| 얼굴 영상    | 표정 변화, 운동 미세 떨림, 비대칭성                           | 신경계          |
| 음성       | 포먼트(F0, F1-F3), jitter, shimmer, HNR, GeMAPS 특징 | 파킨슨, 우울, 호흡기 |
| 음성       | 호흡 패턴, 음량 변동성, 발화 속도                            | 호르몬 장애, 갑상선  |
| 웨어러블     | HRV, 수면 패턴, 체온 변화                               | PCOS·자궁내막증   |
| 앱 로그     | 월경주기 패턴, 증상 자가보고                                | PCOS·자궁내막증   |
|          |                                                 |              |

---

## Claude 재시작 시 빠른 작업 재개 방법

1. 이 파일(`CONTEXT.md`) 먼저 읽기
2. 작업하려는 workspace의 핵심 파일만 선택적으로 읽기
3. `_workspace3/01_face_biomarker_literature.md`와 `_workspace3/02_voice_biomarker_literature.md`가 **가장 풍부한 논문 데이터 소스**

---

*생성: 2026-05-08 | Claude Sonnet 4.6*
