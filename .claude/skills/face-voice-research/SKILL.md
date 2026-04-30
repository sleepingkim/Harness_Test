---
name: face-voice-research
description: "얼굴(피부·눈·표정·주름·여드름) 영상/이미지와 음성 데이터를 이용한 AI 질병 예측 연구 파이프라인 오케스트레이터. 문헌 탐색(얼굴+음성 병렬) → 합성 보고서 + Excel 논문 정리표 작성까지 에이전트 팀으로 실행. '얼굴 바이오마커 연구', '음성 바이오마커 연구', '얼굴 음성 질병 예측', 'face voice biomarker' 요청 시 이 스킬을 사용할 것."
---

# Face Voice Research — 파이프라인 오케스트레이터

얼굴 영상과 음성 데이터 기반 질병 예측 연구의 전체 워크플로우를 조율한다.

## 팀 구성

| 에이전트 | 역할 | 실행 Phase |
|---------|------|-----------|
| face-biomarker-reviewer | 얼굴 시각 특징 기반 질병 예측 문헌 탐색 | Phase 1a (병렬) |
| voice-biomarker-reviewer | 음성 기반 질병 예측 문헌 탐색 (한국어 논문 포함) | Phase 1b (병렬) |
| face-voice-synthesizer | 탐색 결과 합성, .md + .xlsx 저장 | Phase 2 |

**아키텍처**: Phase 1a와 1b는 **병렬 실행**, Phase 2는 두 결과 취합 후 실행
`Phase 1a || Phase 1b` → `Phase 2`

모든 에이전트는 `model: "opus"` 사용.

---

## Phase 0: 컨텍스트 확인

```bash
# 디렉토리 준비
mkdir -p _workspace3
```

실행 전 `_workspace3/` 존재 여부 확인:
- **없음**: 초기 실행 → 전체 실행
- **있음 + 특정 단계 재실행 요청**:
  - "음성 리뷰만 다시 해줘" → Phase 1b + Phase 2 재실행
  - "얼굴 리뷰만 다시 해줘" → Phase 1a + Phase 2 재실행
  - "합성만 다시 해줘" → Phase 2만 재실행 (기존 01, 02 파일 활용)
- **있음 + 완전 새 실행 요청**: 기존 `_workspace3/`를 `_workspace3_prev/`로 이동 후 새 실행

---

## Phase 1: 병렬 문헌 탐색

Phase 1a와 Phase 1b를 **동시에** 실행한다.

### Phase 1a: 얼굴 바이오마커 문헌 탐색 (face-biomarker-reviewer)

```
Agent(
  subagent_type: "face-biomarker-reviewer",
  model: "opus",
  prompt: "
    연구 주제: 얼굴(피부, 눈, 표정, 주름, 여드름 등 시각적 외형 특징)의 이미지·영상 데이터를
    AI로 분석하여 특정 질환을 예측하는 연구를 체계적으로 탐색한다.
    
    중요 제외 사항:
    - rPPG (원격 광혈류측정) 기반 심박수/HRV 측정 연구는 제외
    - 피부 색상 변화가 아닌 혈류 신호 기반 연구는 제외
    - 순수 시각적 외형 특징 (여드름, 주름, 피부색, 눈 상태, 표정) 기반 연구만 포함
    
    특히 주목할 질환:
    - PCOS: 여드름(안드로겐성), 다모증, 호르몬성 피부 변화
    - 자궁내막증: 연관 피부 변화 (있다면)
    - 갑상선 질환: 눈 돌출, 눈꺼풀 부종, 피부 변화
    - 빈혈: 결막 창백, 안검 색상
    - 황달: 공막 황달, 피부 황달
    - 당뇨: 얼굴 피부 변화
    - 파킨슨/신경계: 표정 감소, 얼굴 비대칭
    
    각 논문에 대해 구체적으로 추출:
    - 어떤 얼굴 바이오마커를 사용했는가
    - 어떤 카메라/장비로 어떻게 수집했는가
    - 전처리 및 모델 아키텍처
    - 학습 방법 (optimizer, lr, augmentation)
    - 실험 설계 (분할, cross-validation)
    - 성능 지표 (AUC, accuracy, sensitivity/specificity)
    
    출력: _workspace3/01_face_biomarker_literature.md
  "
)
```

완료 조건: `_workspace3/01_face_biomarker_literature.md` 생성 확인

---

### Phase 1b: 음성 바이오마커 문헌 탐색 (voice-biomarker-reviewer)

```
Agent(
  subagent_type: "voice-biomarker-reviewer",
  model: "opus",
  prompt: "
    연구 주제: 목소리(음성) 데이터의 음향학적 특징을 AI로 분석하여 특정 질환을 예측하는
    연구를 체계적으로 탐색한다.
    
    중요 포함 사항:
    - 한국어 논문을 적극적으로 포함 (RISS, KISS, DBpia 탐색)
    - 기침 소리, 호흡음 등 음성 외 음향 데이터도 포함
    - 자유 발화, 지속 모음, 읽기 과제 등 다양한 발화 과제 포함
    
    특히 주목할 질환:
    - 파킨슨병: 음성 떨림, 발음 왜곡 (가장 많이 연구됨)
    - 우울증/불안: 발화 리듬, 음성 에너지 변화
    - COVID-19/호흡기: 기침 소리, 호흡 패턴
    - PCOS/갑상선: 성호르몬에 의한 음성 주파수/성대 특성 변화
    - 치매/알츠하이머: 언어적 특징, 유창성
    
    각 논문에 대해 구체적으로 추출:
    - 어떤 음향 특징을 바이오마커로 사용했는가 (MFCC, F0, 지터, 시머, HNR 등)
    - 어떤 장비로 어떤 발화 과제를 통해 수집했는가
    - 녹음 환경 (실험실 vs. 실생활)
    - 피험자 수 및 환자군/대조군 구성
    - 전처리 및 특징 추출 방법 (librosa, openSMILE, praat 등)
    - 모델 아키텍처 및 학습 방법
    - 실험 설계 및 성능 지표
    
    한국 논문에서는:
    - 음성 질환 예측 관련 한국 임상 데이터 활용 연구 포함
    - 한국어 발화 특성을 고려한 연구 포함
    
    출력: _workspace3/02_voice_biomarker_literature.md
  "
)
```

완료 조건: `_workspace3/02_voice_biomarker_literature.md` 생성 확인

---

## Phase 2: 합성 및 Excel 생성 (face-voice-synthesizer)

Phase 1a와 Phase 1b 모두 완료 후 실행.

```
Agent(
  subagent_type: "face-voice-synthesizer",
  model: "opus",
  prompt: "
    입력 파일:
    - _workspace3/01_face_biomarker_literature.md (얼굴 바이오마커 탐색 결과)
    - _workspace3/02_voice_biomarker_literature.md (음성 바이오마커 탐색 결과)
    
    작업:
    1. 두 파일의 모든 논문 항목 추출 및 통합
    2. 합성 보고서 작성: _workspace3/03_synthesis.md
    3. Excel 논문 정리표 생성: _workspace3/face_voice_biomarker_papers.xlsx
       - 시트1: 얼굴 바이오마커 논문 (상세 정보)
       - 시트2: 음성 바이오마커 논문 (상세 정보)
       - 시트3: 통합 요약 (질환별 최적 바이오마커)
       - 시트4: 공개 데이터셋 목록
    4. Python create_excel.py 스크립트 저장: _workspace3/create_excel.py
    
    Excel 각 논문 행에 포함할 정보:
    - 제목, 저자, 연도, 게재지
    - 바이오마커 유형 및 구체적 바이오마커명
    - 탐지 질환
    - 데이터 수집 방법 (장비, 환경, 발화/촬영 과제)
    - 데이터셋 규모 (피험자 수, 환자군/대조군)
    - 특징 추출 방법
    - 모델 아키텍처
    - 학습 방법 요약
    - 주요 성능 (AUC, Acc, F1, Sensitivity, Specificity)
    - 코드/데이터 공개 여부
    - 증거 수준
    - 주요 한계점
    
    Excel 생성은 Python openpyxl 라이브러리 사용.
    openpyxl 미설치 시 pip install openpyxl 실행.
    
    PCOS/자궁내막증 적용 가능성도 합성 보고서에 포함.
  "
)
```

완료 조건:
- `_workspace3/03_synthesis.md` 생성 확인
- `_workspace3/face_voice_biomarker_papers.xlsx` 생성 확인
- `_workspace3/create_excel.py` 생성 확인

---

## 최종 산출물 구조

```
_workspace3/
├── 01_face_biomarker_literature.md     — 얼굴 바이오마커 문헌 탐색 결과
├── 02_voice_biomarker_literature.md    — 음성 바이오마커 문헌 탐색 결과 (한국 포함)
├── 03_synthesis.md                     — 통합 합성 보고서
├── face_voice_biomarker_papers.xlsx    — 논문 정리 Excel (4개 시트)
└── create_excel.py                     — Excel 생성 Python 스크립트
```

---

## 에러 핸들링

| 상황 | 처리 |
|------|------|
| Phase 1a 산출물 미생성 | face-biomarker-reviewer 1회 재실행 |
| Phase 1b 산출물 미생성 | voice-biomarker-reviewer 1회 재실행 |
| openpyxl 미설치 | pip install openpyxl 실행 후 재시도 |
| Excel 저장 실패 | .csv 형식으로 대체 저장 후 보고 |
| 한국어 논문 탐색 실패 | 영문 논문만으로 진행 후 한계 명시 |
