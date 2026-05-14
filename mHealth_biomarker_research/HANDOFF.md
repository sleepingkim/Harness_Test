# mHealth Biomarker Research — Handoff Document

**마지막 업데이트**: 2026-05-14  
**프로젝트**: PCOS 예측을 위한 스마트폰 카메라 기반 바이오마커 자가수집 임상 연구 설계

---

## 1. 프로젝트 목표

사용자가 **자신의 스마트폰 카메라**로 일상 환경에서 직접 얼굴·피부·기타 바이오마커를 촬영하여, **PCOS(다낭성난소증후군)** 를 예측하는 mHealth 임상 연구를 설계한다.

핵심 질문:
- 어떤 바이오마커를 자가수집할 수 있는가?
- 사용자에게 어떤 행위·지시사항을 요구해야 하는가?
- 통제 불가 일상 환경에서 어떻게 데이터 신뢰성을 확보하는가?

---

## 2. 워크스페이스 구조

```
mHealth_biomarker_research/
├── HANDOFF.md                          ← 이 파일
├── CONTEXT.md                          ← 프로젝트 초기 컨텍스트 (있으면 참조)
│
├── _workspace1/                        ← 초기 바이오마커 탐색 (레거시)
├── _workspace2/                        ← PCOS·자궁내막증 카메라 바이오마커 (IEEE 논문 포함)
├── _workspace3/                        ← 얼굴·음성 바이오마커 문헌 + Excel
├── _workspace4/                        ← 얼굴·음성 수집 UX 방법론 (일반)
│
└── _workspace5/                        ← ★ 현재 주요 작업 (2026-05-13~14)
    ├── 01_pcos_selfcollection_literature.md
    ├── 02_user_protocol_ux_literature.md
    ├── 03_synthesis_protocol.md
    ├── 04_wildenv_disease_prediction_literature.md
    ├── PCOS_smartphone_protocol.md
    ├── PCOS_wildenv_protocol.md
    ├── reference_validation_01.md
    ├── reference_validation_02.md
    └── reference_validation_04.md
```

---

## 3. _workspace5 파일별 요약

### 📄 01_pcos_selfcollection_literature.md
- **내용**: PCOS 자가수집 스마트폰 바이오마커 문헌 탐색 (26편)
- **에이전트**: pcos-endo-camera-reviewer
- **핵심 논문**: ANcam(흑색가시세포증 자가촬영, AUC 0.854), Oliveira 2023(mFG 다모증), AcneDet(여드름 3각도 셀피), Cao 2025(PCOS 얼굴 형태 딥러닝)
- **검증**: reference_validation_01.md (73% ✅, 1건 ❌ 제거됨)

### 📄 02_user_protocol_ux_literature.md
- **내용**: 사용자 자가수집 실험 프로토콜 UX 방법론 (32편)
- **에이전트**: ux-methodology-reviewer
- **핵심**: SkinTracker 6개월 종단 프로토콜, Vodrahalli AI quality gate, FAIN 자동정렬, Mole Mapper 참조물, e-Consent 설계
- **검증**: reference_validation_02.md (81% ✅, 1건 ❌ 제거됨)

### 📄 03_synthesis_protocol.md
- **내용**: 바이오마커 카탈로그(9종 A/B/C 등급) + 6개 촬영 프로토콜 + 연구 설계서
- **에이전트**: pcos-endo-synthesizer
- **핵심**: A등급 3종(AN·여드름·다모증), 표본 240명, 6개월 retention ≥60%

### 📄 04_wildenv_disease_prediction_literature.md
- **내용**: 통제 불가 일상 환경(In-the-Wild) 스마트폰 촬영 질병 예측 연구 (28편)
- **에이전트**: pcos-endo-camera-reviewer (4개 스테이지 병렬)
- **핵심 논문**: eBRAVE-AF(5,551명 siteless RCT), MoodCapture CHI 2024(passive burst), Hauer 2026(0회 사이트 방문 DCT), Apple Heart Study(419K명)
- **검증**: reference_validation_04.md (80% ✅, 0건 ❌)

### 📄 PCOS_smartphone_protocol.md  ← v1.0 통제 환경
- **내용**: 엄격한 사전 통제 환경 프로토콜. 노이즈 변수 목록 + 행동 수칙 + 환경 규약 + 품질 검사 기준. 인용 링크 포함(31편).
- **용도**: 이상적 통제 조건 연구 또는 서브그룹 비교용

### 📄 PCOS_wildenv_protocol.md  ← v2.0 In-the-Wild ★ 현재 방향
- **내용**: 통제 불가 일상 환경 대상 프로토콜. 노이즈를 측정·기록·보정하는 패러다임. 인용 링크 포함(16편).
- **핵심 설계**: 절대 거부 조건 5개만 / 품질 등급 A/B/C 자동 부여 / 메타데이터 자동 수집 / 참여자 지시사항 3개만
- **근거**: Ali 2026(지시 없는 자가촬영 94.6% 임상 활용 가능)

---

## 4. 핵심 발견 요약

### 자가수집 가능 PCOS 바이오마커 (검증된 순)

| 등급 | 바이오마커 | 부위 | 성능 | 근거 논문 |
|------|-----------|------|------|---------|
| A | 흑색가시세포증(AN) | 목 뒷부분 | AUC 0.854 | ANcam (Dhanoo 2024) |
| A | 여드름 IGA | 얼굴 | IGA 0.85 | AcneDet (Huynh 2022) |
| A | 다모증 mFG | 9부위 | BA 0.89 | Oliveira 2023 |
| B | rPPG HRV | 얼굴 영상 30초 | — | MobilePhys (Liu 2022) |
| B | 얼굴 BMI | 얼굴 셀피 | — | 복수 논문 |
| B | 두피 탈모 | 정수리 | 94% 일치 | MDhair (2025) |

### In-the-Wild 노이즈 대응 6가지 전략

1. **실시간 AI quality gate** — blur/lighting/zoom 즉시 판정 (Vodrahalli 2023)
2. **다중 측정 + 통계 평균** — 14일 집중 측정 (eBRAVE-AF)
3. **메타데이터 ML feature화** — 조명·자세·시각을 보조 변수로 (MoodCapture)
4. **알고리즘 ROI 보정** — 모션 아티팩트 소프트웨어 제거 (MobilePhys)
5. **참조물·캘리브레이션** — 색표 스티커, 동전 (Mole Mapper, Vouri 2021)
6. **대규모 분산 데이터** — 노이즈 평균화 (Flament 1.1M selfies)

### 연구 공백 (본 연구의 차별점)

- PCOS + 카메라 자가수집 + In-the-Wild = **사실상 백지 상태**
- Apple Women's Health Study(100K+)도 카메라 미활용
- PCOS 다중 표현형(여드름+다모증+AN+탈모+rPPG) 통합 자가수집 연구 없음

---

## 5. 현재까지 작업 완료 현황

```
[완료] Phase 1a  — PCOS 자가수집 바이오마커 문헌 탐색 (26편)
[완료] Phase 1b  — 사용자 프로토콜 UX 방법론 탐색 (32편)
[완료] Phase 1c  — In-the-Wild 질병 예측 연구 탐색 (28편)
[완료] Phase 1.5 — 참고문헌 할루시네이션 검증 (3개 파일)
[완료] Phase 2   — 통합 바이오마커 + 실험 프로토콜 합성 보고서
[완료] 프로토콜  — v1.0 통제 환경 / v2.0 In-the-Wild (인용 포함)
```

---

## 6. 다음 단계 옵션

아래 중 선택하거나 새 방향 지시:

| 옵션 | 내용 | 관련 에이전트 |
|------|------|-------------|
| A | **IRB/윤리심의 관련 mHealth 연구 사례 탐색** | pcos-endo-camera-reviewer |
| B | **앱 개발 스펙 문서 작성** (촬영 UI, 품질 검사 알고리즘 스펙) | 직접 작성 가능 |
| C | **연구 설계서 고도화** — 표본 크기 계산, 통계 분석 계획 | pcos-endo-synthesizer |
| D | **비교 논문 작성** — In-the-Wild vs. 통제 환경 비교 리뷰 논문 | pcos-endo-latex-writer |
| E | **참여자 모집 전략 탐색** — 소셜미디어 모집, 임상의 의뢰 등 | ux-methodology-reviewer |
| F | **한국 맥락 특화 탐색** — 한국 PCOS 유병률, 국내 mHealth 규제 | 별도 탐색 |

---

## 7. 재개 시 핵심 컨텍스트 로드 순서

새 대화에서 이 프로젝트를 이어받을 때:

```
1. 이 파일(HANDOFF.md) 읽기
2. _workspace5/PCOS_wildenv_protocol.md 읽기 (현재 프로토콜 방향)
3. _workspace5/03_synthesis_protocol.md 읽기 (바이오마커 카탈로그)
4. 필요 시 개별 문헌 파일 참조
```

---

## 8. 주요 에이전트 재실행 명령어

```
# 추가 문헌 탐색
subagent_type: pcos-endo-camera-reviewer
출력 디렉토리: mHealth_biomarker_research/_workspace5/

# 참고문헌 검증
skill: reference-hallucination-guard
대상 파일: _workspace5/{파일명}.md

# 합성 보고서 업데이트
subagent_type: pcos-endo-synthesizer
입력: _workspace5/ 전체

# 프로토콜 문서 추가 작성
직접 Write 도구 사용 (에이전트 불필요)
```

---

*이 문서는 대화 간 컨텍스트 전달용입니다. 상세 내용은 각 _workspace5/ 파일을 참조하세요.*
