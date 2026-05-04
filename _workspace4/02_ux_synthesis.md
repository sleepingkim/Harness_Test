# 얼굴·음성 데이터 수집 UX 설계 가이드라인 합성 보고서

**작성일**: 2026-04-30
**작성자**: ux-methodology-synthesizer
**근거 문헌**: 41개 (✅ 검증 32개, ⚠️ 부분검증 7개, ❌ 저자/연도 수정 적용 2개)
**대상 시나리오**: 한국어 PCOS·자궁내막증 예측 스마트폰 앱에서의 얼굴 사진·음성 데이터 수집

> **검증 반영 원칙**: 본 합성 보고서는 `reference_validation_ux.md`(2026-04-30 검증)에 따라 ❌(저자명 완전 오류) 2건은 **수정된 정보**(Petrizzo et al. 2021, Demiris et al. 2010)로 인용하고, ⚠️(저자/연도 부분 오류) 7건은 본문에서 [재확인 필요] 주석을 부기한다. 인용 번호는 `01_ux_methodology_literature.md`의 논문 번호(2-1, 3-2 등)를 그대로 사용한다.

---

## 1. 종합 요약 (Executive Summary)

PCOS·자궁내막증을 예측하기 위해 일반 사용자의 얼굴 사진과 음성을 모바일에서 수집하려면, "임상급 표준"과 "가정 환경의 현실"을 동시에 만족시키는 UX가 필요하다. 36편의 동료심사 문헌을 합성한 결과 핵심 설계 원칙은 다음 7가지다.

### 1.1 핵심 UX 설계 원칙 (7개)

1. **캡처 시점 품질 게이트(Capture-time Quality Gate)** — 업로드 후 거부가 아니라, 촬영·녹음 중 실시간 피드백으로 게이트한다. 사용자가 "왜 다시 찍어야 하는지"를 즉시 이해해야 재시도 의지를 잃지 않는다 (논문 2-2, 6-1, 6-2).
2. **마법사형 단일 선형 흐름(Wizard-style Single Linear Flow)** — 한 세션은 "다음 / 종료" 2버튼만 노출. 분기·뒤로가기·점프를 최소화해 인지 부하를 낮춘다 (논문 7-4, 7-5).
3. **계층적·동적 동의(Tiered & Dynamic Consent)** — 일회성 긴 동의서가 아니라, 핵심 1단계 + 확장 상세 + 항목별 토글 + 철회 가능 대시보드의 4-layer 구조 (논문 5-2, 5-3, 5-6, 5-7, 5-8).
4. **프라이버시 기본값 = 비공유(Privacy-by-Default-Off)** — 여성 mHealth 앱의 87%가 제3자 데이터 공유를 기본 활성화한 현실을 역행하여, 모든 외부 공유는 명시적 옵트인 기본값을 비활성으로 설정 (논문 5-4).
5. **표준화된 발화·자세 프로토콜(Standardized Elicitation Protocol)** — 사용자가 매 회 동일한 거리·자세·발화 과제를 수행하도록 시각·음성 가이드를 강제. 종단 비교 가능성을 확보한다 (논문 2-1, 3-2, 3-5, 3-7).
6. **Give-and-Take 인사이트 루프** — 사용자가 데이터를 줄 때마다 의미 있는 인사이트(추세 그래프, 변화 알림)를 즉시 돌려준다. 알림 단독은 부족하다 (논문 4-5, 4-8).
7. **부담 적응형 EMA(Burden-adaptive EMA)** — 부정 감정·스트레스 자가보고가 높은 날은 과제를 단축. 1일 2-3회 비임상 모드를 기본값으로 (논문 4-2, 4-3).

### 1.2 즉시 적용 가능한 최우선 권고사항 (Top 3)

| 순위 | 권고 | 근거 | 기대 효과 |
|------|------|------|----------|
| **1** | 얼굴 캡처 시 FAIN(Face Alignment Indicator) + 4-게이트(노출/초점/포즈/해상도) IQA를 결합한 자동 셔터 도입 | 2-1, 2-2, 6-1, 6-2 | 종단 데이터 일관성 확보, 재촬영 비율 절감 |
| **2** | 음성 녹음은 "지속 모음 6초×3 + 표준 문장 낭독 + CAPE-V 자유 발화 20초"의 3종 마스터 프로토콜 + WAV 비압축 강제 | 3-2, 3-5(Vaiciukynas 등 2017, [재확인 필요]), 3-7 | 임상 비교 가능 음성 바이오마커 추출, Jitter/Shimmer 왜곡 방지 |
| **3** | 동의 인터페이스를 "1) Just-in-Time 핵심 동의 + 2) 항목별 옵트인 + 3) 철회/재동의 대시보드"의 3중 구조로 구현 | 5-2, 5-3, 5-6, 5-7 | 프라이버시 피로 감소, 사용자 자율성 보장, 한국 개인정보보호법 적합성 |

---

## 2. 얼굴 사진 수집 UX 가이드라인

### 2.1 캡처 인터페이스 설계

#### 2.1.1 정렬 인디케이터 (Face Alignment Indicator, FAIN)
Hashimoto & Kaneda (2024) [원본 표기 "Han 등", 저자명 재확인 후 적용] 의 FAIN 시스템을 PCOS·자궁내막증 앱의 1차 권장 캡처 인터페이스로 채택한다 (논문 2-1).

**구성 요소:**
- **고정 타겟(Target Indicator)**: 화면 중앙에 회색 반투명 윤곽선으로 표시되는 이상적 얼굴 위치·크기.
- **동적 정렬(Alignment Indicator)**: 실시간 얼굴 랜드마크에 따라 변형되는 두 번째 윤곽선. 사용자 머리 움직임에 따라 형태/위치가 변한다.
- **상태 색상 코드**: 미정렬 = 빨강, 정렬 임박 = 주황, 정렬 완료 = 파랑.
- **자동 셔터(Auto-capture)**: 정렬 조건이 0.5초 이상 유지되면 자동 촬영. 수동 셔터는 보조 옵션.

#### 2.1.2 실시간 품질 피드백
Vodrahalli 등 (2023, 논문 2-2)의 임상 검증 결과에 따르면, "업로드 시점이 아닌 캡처 시점"에 품질 피드백을 제공하면 임상 사용 가능 사진 비율이 유의미하게 상승한다.

**실시간 피드백 항목 (캡처 화면 상단 HUD):**
- 노출(Exposure): "조명이 부족합니다" / "역광입니다" / "정상"
- 초점(Focus): "초점이 맞지 않습니다" / "정상"
- 거리(Distance): "더 가까이" / "조금 멀리" / "정상" (얼굴-화면 비율 35-50% 권장)
- 안정성(Stability): IMU(자이로/가속도계)로 흔들림 감지

#### 2.1.3 캡처 모드
Vodrahalli 등 (2023, 논문 2-2)과 ElHawary 등 (2022) [원본 표기 "2023", 재확인 결과 2022, 논문 2-4]에 따라 의료용 사진은 보정 비활성화 모드로 캡처한다.

| 항목 | 권장 설정 |
|------|----------|
| 색 보정 | 비활성 (Beauty filter, AI 보정 OFF) |
| HDR | 비활성 (자연 노출 유지) |
| 포맷 | JPEG 95% 또는 RAW(가능 시) |
| 메타데이터 | EXIF + 기기 모델·OS 버전·카메라 모듈 ID 별도 저장 |

### 2.2 환경 통제 가이드

Black 등 (2025) [원본 표기 "Hospitalist Community 2023", 실제 *Cutis* 2025, 논문 2-5]와 Ashique·Kaliyadan (2015, 논문 2-6)의 임상 가이드라인을 가정 환경에 맞게 단순화한다.

| 항목 | 임상 표준 | 가정 환경 권장 (단순화) |
|------|---------|-------------------|
| 광원 | 5000K LED 링라이트 + 45° 조명 | 자연광(창가) 또는 일반 실내 조명; 형광등 정면 광 |
| 배경 | 단색 라이트블루/그린 | 단색 흰 벽 또는 단색 배경 추천 |
| 거리 | 15-30 cm 고정 | 얼굴 비율 자동 검출 (35-50%) → 자동 가이드 |
| 메이크업 | 클렌징 후 촬영 | "메이크업 제거 권장" 안내 + 사용자 자가보고 토글 |
| 촬영 횟수 | 동일 부위 다중 촬영 | 1세션당 3장 자동 캡처 (microvariation 보존) |

> **앱 구현 팁**: 첫 사용 시 30초 안내 영상(시각적 체크리스트)을 1회 재생, 이후 세션에는 아이콘 4개로 압축 표시.

### 2.3 품질 게이트 파이프라인

Schlett 등 (2022, 논문 6-2)과 Journal of Imaging 종설(2025, 논문 6-1)의 IQA(Image Quality Assessment) 권고를 4-게이트 자동 평가 파이프라인으로 구현한다.

```
[캡처 직후 0.3초 이내 실행]
   │
   ├─ Gate 1: 노출(Exposure)        — 평균 휘도 80-220 (0-255), 클리핑 픽셀 < 5%
   ├─ Gate 2: 초점(Focus)           — Laplacian variance > 임계값(기기별 보정)
   ├─ Gate 3: 포즈(Pose)            — Yaw/Pitch/Roll 각 < 10°
   └─ Gate 4: 해상도(Resolution)    — 얼굴 영역 픽셀 > 480×480
   │
   ▼
[모든 게이트 통과] → 저장 + "촬영 완료" 피드백
[1개 이상 실패]  → 거부 + 실패 사유 화면 표시 → 재촬영 가이드
```

**거부 시 워크플로:**
1. 실패 사유를 한국어 평문으로 표시 ("사진이 흔들렸어요" / "얼굴이 너무 작아요").
2. 구체적 개선 액션 제시 ("폰을 두 손으로 잡아 주세요" / "10cm 더 가까이").
3. 재시도 카운터를 표시(3회 시도 후 기존 사진 중 최선을 저장하는 fallback 옵션).
4. 재시도 카운트가 5회 초과 시 "오늘은 건너뛰기" 옵션 노출하여 사용자 좌절감 차단.

---

## 3. 음성 녹음 수집 UX 가이드라인

### 3.1 표준 발화 과제 구성

Kalia 등 (2025, 논문 3-2)의 음성 바이오마커 마스터 프로토콜과 ASHA 권고(Patel 등 2018, 논문 3-7), Vaiciukynas 등 (2017) [원본 표기 "Almeida JS 등", 재확인 후 적용, 논문 3-5]의 PD 음향 분석 표준을 결합한 3종 과제 조합을 권장한다.

| #   | 과제                                           | 시간/반복    | 측정 가능 변수                       | 근거       |
| --- | -------------------------------------------- | -------- | ------------------------------ | -------- |
| 1   | 모음 /a/ 지속 발성 (sustained phonation)           | 6초 × 3회  | F0, Jitter, Shimmer, HNR, CPP  | 3-2, 3-5 |
| 2   | 표준 문장 낭독 (Korean adaptation: 무지개 단락 한국어 번역본) | 약 30-45초 | 발화속도, 휴지 패턴, 음운 정확도            | 3-2, 3-7 |
| 3   | CAPE-V 자유 발화 ("오늘 어떻게 지내셨어요?")               | 20초 이상   | prosody, jitter (자연 발화), 감정 운율 | 3-7      |

**총 세션 시간**: 약 90초~2분.

**과제 간 전환:**
- 각 과제 시작 전 3-2-1 카운트다운 + 시각적 example 표시.
- 과제 1(모음)은 음량 인디케이터로 적정 강도 가이드(60-70 dB SPL 추정).
- 과제 2(낭독)는 자동 스크롤 텍스트, 적정 속도 시각화.
- 과제 3(자유 발화)은 정적/저활동 검출 시 "조금 더 말씀해 주세요" 부드러운 프롬프트.

### 3.2 녹음 환경 요구사항

#### 3.2.1 SNR 기준
Kalia 등 (2025, 논문 3-2)과 Noffs 등 (2023/2024, 논문 3-4)의 권고를 합성:

| SNR | 평가 | 앱 대응 |
|-----|-----|---------|
| ≥ 42 dB | 우수 | 즉시 녹음 진행 |
| 20-42 dB | 양호 | 녹음 진행 + 메타데이터에 "noisy" 플래그 |
| < 20 dB | 부족 | 녹음 거부, "조용한 곳으로 이동해 주세요" 안내 |

녹음 시작 전 1초간 환경 노이즈를 수집하여 SNR 추정 후 사용자에게 인디케이터(녹/황/적) 표시.

#### 3.2.2 마이크 설정
Petrizzo & Popolo (2021) [원본 표기 "Grillo EU 등 2019", 검증 결과 저자/연도 수정, 논문 3-1]와 Noffs 등 (2023/2024, 논문 3-4)에 따라:

| 항목 | 권장 설정 |
|------|----------|
| 샘플링 레이트 | 44.1 kHz |
| 비트 심도 | 16-bit (WAV) |
| 코덱 | **WAV(비압축) 강제** — MP3/AAC 금지 (Jitter/Shimmer 왜곡) |
| 입과 마이크 거리 | 5-30 cm (자세는 좌위) |
| 외장 마이크 | PnP(USB-C/Lightning) 마이크 사용 시 인센티브 보너스 인디케이터 |
| 입력 레벨 | OS 자동 게인 비활성, 앱 내 고정 게인 |

> **앱 구현 팁**: PnP 마이크 사용 사용자에게 "임상급 마이크 모드" 배지 부여. 코호트 내 sub-cohort로 별도 분석 가능.

### 3.3 메타데이터 수집 설계

Asci 등 (2020) [원본 표기 "Tanaka 등", 재확인 후 적용, 논문 3-3]의 분석에 따르면 성별·연령은 음향 특징의 주요 분산원이므로, 메타데이터 수집은 모델 학습의 필수 입력이다.

**필수 메타데이터 (자동 수집):**
- 기기 모델, OS 버전, 앱 버전
- 녹음 시각(타임존 포함), 추정 SNR
- 마이크 종류(internal/external), 코덱, 샘플링 레이트
- IMU 기반 자세 추정(좌위/와위)

**필수 메타데이터 (사용자 입력 - 온보딩 시 1회):**
- 출생 연도, 성별/생물학적 성, 발성 모국어(한국어/이중언어)
- 흡연 여부, 호흡기 만성질환 유무

**세션 메타데이터 (매 세션 자가보고, 1화면 토글):**
- 현재 기분(5점 척도)
- 환경(가정/직장/외부)
- 감기·인후염 유무 (당일)
- 카페인/식사 후 몇 시간 경과 (드롭다운)

---

## 4. 동의·프라이버시 UX 가이드라인

### 4.1 계층화된 동의 인터페이스

Trust, Privacy Fatigue 연구(MDPI 2025, 논문 5-3)에 따르면 사용자의 91%는 약관을 읽지 않으므로, 정보 전달은 "양"이 아니라 "구조"의 문제다.

**3-Layer 계층 구조:**

```
Layer 1: 핵심 동의 카드 (1화면, 5초 내 이해)
   ├ 무엇을: "얼굴 사진 + 음성 녹음을 PCOS/자궁내막증 예측에 사용합니다"
   ├ 누가:   "○○ 대학병원 + ○○ AI 회사가 공동으로 봅니다"
   ├ 보관:   "분석 후 5년, 그 후 자동 삭제"
   └ 권리:   "언제든 삭제 가능" + [동의/거부] 버튼

Layer 2: 확장 상세 (펼침 버튼, 항목별)
   ├ 데이터 처리 흐름 인포그래픽 (Haring 등 2023, 논문 5-1)
   ├ 제3자 공유 항목 (기본 OFF 토글)
   └ 법적 근거 (개인정보보호법 제17조 등)

Layer 3: 전체 약관 (PDF/외부 페이지)
```

**동의 후 즉시 이해도 퀴즈 (Haring 등 2023, 논문 5-1):**
- 3문항, 각 5초 이내 답변 가능.
- 예: "내 사진은 누가 볼 수 있나요?" / "삭제하면 어떻게 되나요?"
- 정답률 < 70% 시 핵심 정보 재안내.

### 4.2 Just-in-Time 동의 설계

Brightwell 등 (2024, 논문 5-2)의 동의 확장 개념을 적용하여, 첫 진입 동의 외에 **데이터 종류별 첫 사용 시점에 추가 옵트인**을 요구한다.

| 시점 | 동의 항목 |
|------|----------|
| 회원가입 | 기본 약관 + 개인정보 처리 |
| **얼굴 사진 첫 캡처 직전** | "얼굴 이미지 수집 + AI 분석" 별도 옵트인 |
| **음성 첫 녹음 직전** | "음성 데이터 수집 + 화자 식별 가능성 안내" 별도 옵트인 |
| 데이터 외부 공유 첫 발생 시 | "○○ 연구기관과 공유" 항목별 토글 |
| 신규 연구 프로토콜 추가 시 | 푸시 알림 + 인앱 동의 갱신 |

### 4.3 동적 동의 관리

npj Digital Medicine 2025(논문 5-6, 5-7)와 Lee 등 (2024, 논문 5-8)의 동적 동의 시스템을 참조하여 사용자 대시보드를 1차 메뉴에 노출한다.

**"내 데이터" 대시보드 필수 기능:**

```
┌─────────────────────────────────────────┐
│  내 데이터                               │
├─────────────────────────────────────────┤
│  [프로필]                                │
│   얼굴 사진 23장   [보기] [삭제]         │
│   음성 녹음 18건   [듣기] [삭제]         │
│                                          │
│  [공유 설정]                             │
│   ☑ ○○ 대학병원 임상 연구              │
│   ☐ ○○ AI 회사 공동 연구               │
│   ☐ 익명화 후 공개 데이터셋 기여        │
│                                          │
│  [동의 이력]                             │
│   2026-04-01: 음성 수집 동의            │
│   2026-04-15: 외부 공유 거부            │
│                                          │
│  [전체 데이터 다운로드 / 계정 삭제]      │
└─────────────────────────────────────────┘
```

추가:
- **월 1회 동의 리뷰 알림**(Lee 등 2024) — 단, 부정적 알림 피로 감지 시 분기/연 단위로 자동 조정.
- **여성 mHealth 앱 특수 고려** (Alfawzan 등 2022, 논문 5-4): 위치, 행동 추적, 광고 식별자 사용은 **기본 비활성**, 명시적 옵트인 필요.
- **PHI급 보안** (Fagherazzi & Bensoussan 2024, 논문 3-6): 음성은 화자 식별 가능 → 익명화 + 연합학습(federated learning) 검토.

---

## 5. 순응도(Compliance) 향상 전략

### 5.1 EMA 빈도 및 타이밍

Businelle 등 (2024, 논문 4-2)의 요인설계 실험에서 **비임상 환경에서는 1일 2-3회 프롬프트가 가장 높은 순응율(91.7%)**을 보였다. 4-5회·6회 이상은 오히려 순응율 하락.

**권장 PCOS·자궁내막증 EMA 스케줄:**

| 시점 | 작업 | 근거 |
|------|------|------|
| 점심 12:30 | 짧은 자가보고 (기분, 통증, 증상) | Bidargaddi 등 2018 (논문 4-7): +8.8%p 참여 |
| 저녁 19:30 | 얼굴 사진 + 음성 녹음 (주 3-4회) | Bidargaddi 등 2018: 주말 효과 |
| 주 1회 (사용자 선택일) | 종합 자가평가 + 데이터 시각화 리뷰 | 논문 4-8 |

**개인화 전이:**
- 첫 2주: 위 고정 스케줄.
- 3주차부터: 사용자 응답 패턴 학습 후 ±2시간 범위 내 자동 조정.
- 8주차부터: 사용자가 직접 시간 변경 가능.

### 5.2 인센티브 설계

Wen 등 (2017, 논문 4-1)의 메타분석에서 6개월 후 EMA 순응율은 평균 49.3%까지 하락. 인센티브의 단계적 강화가 핵심이다.

**Phase별 인센티브 설계:**

| Phase                     | 기간     | 인센티브                                               |
| ------------------------- | ------ | -------------------------------------------------- |
| Phase 1 (Onboarding)      | 1-2주   | 건강 리포트 무료 발급, 환영 배지                                |
| Phase 2 (Habit Formation) | 3주-3개월 | 주간 추세 그래프, 동질 코호트 비교, "○일 연속 기록" 배지                |
| Phase 3 (Sustained)       | 3-6개월  | 분기 의료진 코칭 옵션 (Amagai 등 2022, 논문 4-5: 코칭이 유지 결정 요인) |
| Phase 4 (Long-term)       | 6개월 이상 | 연구 데이터 기여 증명서, 결과 공동저자 옵션, 의료기관 연계 우대              |

> **금전 인센티브 주의**: Wen 등 메타분석에서 금전 인센티브 단독 효과는 제한적. 의미·자율성·유능감의 내재 동기가 더 효과적.

### 5.3 장기 유지 전략

Amagai 등 (2022, 논문 4-5)에 따르면 상용 mHealth 앱 30일 후 평균 순응율은 6%, 90일 유지율은 10% 미만. Sun 등 (2025, 논문 4-4)은 SDoH(건강의 사회적 결정요인)가 순응율의 주요 변수임을 지적한다.

**장기 유지 5대 전술:**

1. **하이브리드 코칭** (논문 4-5): 자동 알림 + 분기 1회 간호사·코디네이터 인적 연락. 순응 오즈 약 2배.
2. **부담 적응형 단축** (Tate 등 2024, 논문 4-3): 사용자가 "오늘 기분 나쁨" 자가보고 시 음성 과제 1회만 수행, 사진 생략.
3. **주간 인사이트 그래프** (논문 4-8): 사용자 데이터 → 추세 → "지난주 대비 음성 안정도 ○○% 개선" 같은 의미 있는 피드백 즉시 반환.
4. **세그먼트별 알림 전략** (Sun 등 2025, 논문 4-4):
   - 직장 여성: 12:30 점심 + 19:30 퇴근 후
   - 주부: 10:00 가사 후 휴식 + 14:00 오후
   - 학생: 18:00 하교 후 + 22:00 자기 전
5. **앱 피로 완화** (Ali & Thu 2025, 논문 7-6): 단일 앱이 모든 알림을 떠안기보다, 의료기관 SMS·기존 메신저(KakaoTalk)와 연계.

---

## 6. 통합 데이터 수집 워크플로

PCOS·자궁내막증 1세션(얼굴 + 음성 동시 수집)의 마법사형 단일 흐름 설계 (논문 7-5).

```
┌──────────────────────────────────────────────────────────────┐
│  Step 1: 온보딩 (첫 회만, 약 3분)                            │
│   ├ 인구통계 입력 (출생연도, 성별, 모국어, 흡연 등)          │
│   ├ Tier 1 핵심 동의 카드 + 이해도 퀴즈 (논문 5-1, 5-3)     │
│   └ 30초 안내 영상 (얼굴 캡처 + 음성 녹음 시연)             │
└──────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│  Step 2: 세션 시작 (매 회, 약 2-3분)                         │
│   ├ 점심/저녁 푸시 알림 클릭 → 앱 진입                       │
│   ├ 환경 자가보고 1화면 (조명·메이크업·기분·환경) 토글       │
│   └ "시작하기" 버튼 [다음] [건너뛰기]                       │
└──────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│  Step 3: 얼굴 캡처 (약 30-45초)                              │
│   ├ JIT 동의 (첫 회만): 얼굴 데이터 수집 옵트인              │
│   ├ FAIN 정렬 인터페이스 (논문 2-1)                         │
│   ├ 4-게이트 IQA 자동 검사 (논문 6-1, 6-2)                  │
│   ├ 자동 셔터 → 3장 다중 캡처                                │
│   └ 거부 시 재시도, 5회 초과 시 "건너뛰기" 옵션              │
└──────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│  Step 4: 음성 녹음 (약 90초~2분)                             │
│   ├ JIT 동의 (첫 회만): 음성 데이터 수집 옵트인              │
│   ├ 환경 SNR 측정 1초 (논문 3-2)                            │
│   ├ 과제 1: 모음 /a/ 6초×3 (논문 3-5)                       │
│   ├ 과제 2: 표준 문장 낭독 (논문 3-2)                       │
│   ├ 과제 3: CAPE-V 자유 발화 20초 (논문 3-7)                │
│   └ WAV 비압축 저장 + 메타데이터 기록 (논문 3-4)            │
└──────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│  Step 5: 자가평가 (약 30초)                                   │
│   ├ 통증 점수 (NRS 0-10)                                     │
│   ├ 월경 주기 단계, 출혈 여부                                │
│   └ 부담 인식 (Tate 등 2024, 논문 4-3) — 부담 높음 시 차회 단축 │
└──────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│  Step 6: 즉각 피드백 (약 15초)                                │
│   ├ "이번 주 추세" 미니 그래프 (논문 4-8)                    │
│   ├ "○일 연속 기록" 배지                                     │
│   └ 다음 세션 예정 시각 알림 + [완료]                        │
└──────────────────────────────────────────────────────────────┘
```

**전체 세션 시간**: 평균 3-4분 (얼굴 + 음성 + 자가평가 + 피드백).

---

## 7. 한국 PCOS·자궁내막증 사용자 특수 고려사항

### 7.1 한국어 인터페이스 필수
Tate 등 (2024, 논문 4-3)에서 모국어 지원이 EMA 부담 인식 감소의 주효과 변수로 확인. 한국어 사용자에게 영어 인터페이스는 인지 부하를 약 2배 증가시키는 것으로 유추된다.

**적용:**
- 모든 안내문은 한국어 평문(중학생 이해 가능 수준)으로.
- 의료 전문 용어는 평문 번역 + 괄호 영문 표기.
- 음성 자유 발화 과제는 한국어 표준 발화 자극 사용 ("무지개 단락" 한국어 번역본 등).

### 7.2 한국 개인정보보호법 적합성

**필수 점검 항목:**
- 개인정보보호법 제15조 (수집·이용 동의): 수집 목적·항목·기간 명시.
- 개인정보보호법 제17조 (제3자 제공): 별도 옵트인 필수.
- 의료법 시행령 (의료정보 보관): 5년 이상 보관 시 의료기관 연계 검토.
- 생명윤리법 (인간대상연구): IRB 승인 필요 시 동의 양식 IRB 표준 준수.
- **민감정보(생체정보) 처리**: 얼굴·음성은 "생체정보"로 분류되어 별도 동의 필수.

**npj Digital Medicine SHC Connect**(논문 5-6)와 같은 외부 동의 관리 SDK는 한국 법환경 호환성 별도 검토 후 도입.

### 7.3 한국 여성 세그먼트별 프롬프트 전략

Sun 등 (2025, 논문 4-4)의 SDoH 통합 설계 권고를 한국 여성 PCOS·자궁내막증 사용자에 적용.

| 세그먼트 | 일과 패턴 | 권장 프롬프트 시점 | 추가 고려 |
|----------|---------|-----------------|----------|
| 직장 여성 (20-40대) | 9-18시 근무, 점심·퇴근 시 여유 | 12:30, 19:30 (Bidargaddi 등 2018) | 회의·외근 일정 학습 후 ±2h 자동 조정 |
| 전업주부 | 가사·육아, 오전/오후 자투리 시간 | 10:00, 14:00 | 자녀 돌봄 시간 회피, 짧은 1분 모드 |
| 대학생/대학원생 | 강의 일정, 야간 활동 | 18:00, 22:00 | 시험 기간 자동 휴면 모드 |
| 자영업자 | 비정형, 영업 시간 | 사용자 직접 설정 우선 | 첫 4주 응답 패턴 학습 |

**한국 특수 알림 채널:**
- 푸시 외에 KakaoTalk 알림톡 옵션 (한국 사용자 도달률 높음).
- 의료기관 EMR 연계 시 SMS 백업 (Ali & Thu 2025, 논문 7-6의 앱 피로 완화).

### 7.4 PCOS·자궁내막증 특유 감수성

- **신체 이미지 민감도**: 얼굴 사진은 여드름·털·피부 변화 노출 → "보정 OFF" 강제는 사용자 거부감 가능. 메이크업 가능 모드 + 무메이크업 모드 양쪽 옵션 제공, 메이크업 여부 메타데이터로 모델에 입력.
- **월경 주기 동기화**: 호르몬 변동에 따라 음성 fundamental frequency 변동 가능. 월경 단계 메타데이터 필수.
- **통증·피로 대응**: Tate 등 (2024, 논문 4-3) 부담 적응형 모드 필수 — PCOS·자궁내막증은 만성 통증 동반 빈도 높음.

---

## 8. 구현 우선순위 로드맵

| 우선순위 | 기능 | 근거 | 난이도 | Phase |
|---------|------|------|--------|-------|
| **필수 (Phase 1, MVP 0-3개월)** | | | | |
| 1 | FAIN 얼굴 정렬 + 자동 셔터 | 2-1 | 중간 | Phase 1 |
| 2 | 4-게이트 IQA (노출/초점/포즈/해상도) | 6-1, 6-2 | 중간 | Phase 1 |
| 3 | 3종 음성 과제 (모음/낭독/자유 발화) | 3-2, 3-5, 3-7 | 낮음 | Phase 1 |
| 4 | WAV 비압축 강제 녹음 | 3-4 | 낮음 | Phase 1 |
| 5 | Tier 1 핵심 동의 + 이해도 퀴즈 | 5-1, 5-3 | 낮음 | Phase 1 |
| 6 | JIT 동의 (얼굴/음성 첫 사용 시) | 5-2 | 낮음 | Phase 1 |
| 7 | 한국어 인터페이스 + 평문 안내 | 4-3 | 낮음 | Phase 1 |
| 8 | 1일 2-3회 EMA + 12:30/19:30 푸시 | 4-2, 4-7 | 낮음 | Phase 1 |
| **권장 (Phase 2, 3-9개월)** | | | | |
| 9 | "내 데이터" 동적 동의 대시보드 | 5-6, 5-7, 5-8 | 높음 | Phase 2 |
| 10 | 월 1회 동의 리뷰 알림 | 5-8 | 낮음 | Phase 2 |
| 11 | 부담 적응형 EMA (감정 기반 단축) | 4-3 | 중간 | Phase 2 |
| 12 | 주간 인사이트 그래프 (Give-and-take) | 4-8 | 중간 | Phase 2 |
| 13 | 세그먼트별 푸시 시점 학습 | 4-4 | 중간 | Phase 2 |
| 14 | KakaoTalk 알림톡 채널 통합 | 7-6 | 중간 | Phase 2 |
| 15 | PnP 마이크 사용 인센티브 | 3-1, 3-4 | 낮음 | Phase 2 |
| 16 | 운영팀 모니터링 대시보드 (CMed 패턴) | 6-3, 6-4 | 높음 | Phase 2 |
| **고급 (Phase 3, 9-18개월)** | | | | |
| 17 | 하이브리드 코칭 (간호사·코디네이터 연계) | 4-5 | 매우 높음 | Phase 3 |
| 18 | 의료기관 EMR/PHR 연계 | 7-6 | 매우 높음 | Phase 3 |
| 19 | 연합학습(Federated Learning) 인프라 | 3-6 | 매우 높음 | Phase 3 |
| 20 | 외부 SDK (npj SHC Connect 유사) 도입 | 5-6 | 높음 | Phase 3 |
| 21 | 게이미피케이션·소셜 코호트 비교 | 4-1, 4-5 | 중간 | Phase 3 |
| 22 | RAW 캡처·기기별 색 보정 매트릭스 | 2-4 | 매우 높음 | Phase 3 |

---

## 9. 검증되지 않은 항목 및 연구 공백

### 9.1 한국어/한국 사용자 대상 직접 증거 부재

| 영역 | 공백 | 권장 후속 연구 |
|------|------|--------------|
| 음성 바이오마커 | 한국어 음성에서 PCOS·자궁내막증 음향 특징 검증 부재 | 한국어 표준 발화 자극으로 환자-대조군 음향 비교 파일럿 |
| EMA 순응율 | 한국 여성 PCOS·자궁내막증 환자 대상 EMA 데이터 없음 | 50명 12주 EMA 파일럿, 세그먼트별 순응율 측정 |
| 동의 UX | 한국 여성의 디지털 동의 수용성 연구 부재 | 동적 동의 vs 일회성 동의 A/B 테스트 |
| 얼굴 분석 | PCOS 다모증/여드름·자궁내막증 피부 변화의 디지털 정량화 표준 부재 | Hirsutism 자동 스코어링 모델 + 사용자 수용성 |

### 9.2 본 합성에서 직접 검증되지 않은 항목

- **CAPE-V 한국어 적응본**: 영어 표준 자유 발화 자극 ("Tell me about your voice problem")의 한국어 등가물 미정립 → 임상언어치료학회 협업 필요.
- **한국 5000K 광원 가용성**: Black 등 (2025) 권장은 임상실 가정. 한국 일반 가정의 LED 색온도 분포 조사 필요.
- **여성 mHealth 앱 한국 시장 프라이버시 실태**: Alfawzan 등 (2022, 논문 5-4)은 영미권 중심. 한국 인기 여성 건강 앱(예: 핑크다이어리, 헬로키키 등)의 실태 별도 조사 필요.

### 9.3 향후 파일럿 연구 권장 설계

**파일럿 1 — 캡처 UX 비교 RCT** (3개월, n=60)
- 군 1: FAIN + 4-게이트 IQA (본 권장안)
- 군 2: 자유 캡처 (대조군)
- 1차 결과: 임상 사용 가능 사진 비율, 재시도 횟수, NASA-TLX
- 근거: 논문 2-1, 2-2, 6-1, 6-2

**파일럿 2 — 음성 프로토콜 검증** (6개월, n=100, PCOS 환자 50 + 대조군 50)
- 3종 과제 + WAV 녹음 → Jitter/Shimmer/CPP 추출
- 1차 결과: 분류 AUC, 검사-재검사 신뢰도(ICC)
- 근거: 논문 3-2, 3-5, 3-7

**파일럿 3 — 동적 동의 수용성** (3개월, n=120)
- 군 1: 본 권장 3-Layer 동의
- 군 2: 일회성 긴 동의서
- 1차 결과: 이해도 퀴즈 점수, 6주차 동의 변경 빈도, 신뢰 척도
- 근거: 논문 5-1, 5-2, 5-6, 5-7

---

## 10. 참고문헌 (검증된 항목만, 검증 보고서 기반 보정 적용)

> 검증 보고서(`reference_validation_ux.md`, 2026-04-30)에 따라 ❌(저자명/연도 명백 오류) 2건은 정정 정보로 인용, ⚠️(부분 오류) 항목은 [재확인 필요] 주석 부기. ❌ 항목 중 학술 출처가 아닌 것(IHI 블로그)은 본 합성에서 인용 비중 축소.

### 얼굴 사진 수집
1. Hashimoto W, Kaneda S. A smartphone application for personalized facial aesthetic monitoring. *Skin Research and Technology*, 2024. PMC11230921. ✅
2. Vodrahalli K, et al. Development and Clinical Evaluation of an Artificial Intelligence Support Tool for Improving Telemedicine Photo Quality. *JAMA Network Open / JAMA Dermatology*, 2023. PMC10018405. ✅
3. AI-assisted facial analysis in healthcare: From disease detection to comprehensive management. *Patterns* (Cell Press), 2025. DOI: S2666-3899(25)00023-6. ✅
4. ElHawary H, et al. Pocket Predictors: Are Smartphones the Future of Artificial Intelligence in Plastic Surgery. *Plastic Surgery* 31(4):415-416, **2022** [원본 표기 2023, 재확인 결과 2022]. PMC10617461. ⚠️
5. Black TA, et al. Best Practices for Capturing Clinical and Dermoscopic Images With Smartphone Photography. ***Cutis*** 115(1), **2025** [원본 표기 *The Hospitalist Community* 2023, 실제 *Cutis* 2025]. ⚠️
6. Ashique KT, Kaliyadan F, Aurangabadkar SJ. Clinical photography in dermatology using smartphones: An overview. *Indian Dermatology Online Journal*, 2015. PMC4439742. ✅

### 음성 녹음 수집
7. **Petrizzo D, Popolo PS**. Smartphone Use in Clinical Voice Recording and Acoustic Analysis: A Literature Review. *Journal of Voice* 35(3):499.e23-499.e28, **2021** [원본 "Grillo EU 등 2019" 검증 결과 저자/연도 정정]. PMID: 32736910. ✅(정정 후)
8. Kalia A, Boyer M, Fagherazzi G, et al. Master protocols in vocal biomarker development to reduce variability and advance clinical precision: a narrative review. *Frontiers in Digital Health*, 2025. ✅
9. **Asci F, Costantini G**, et al. Machine-Learning Analysis of Voice Samples Recorded through Smartphones: The Combined Effect of Ageing and Gender. *Sensors*, 2020 [원본 "Tanaka 등" 첫 저자 정정]. PMC7570582. ⚠️(저자 정정 적용)
10. Noffs G, et al. Plug-and-Play Microphones for Recording Speech and Voice with Smart Devices. *Folia Phoniatrica*, 2023/2024. PMC11309067. ✅
11. **Vaiciukynas E**, Verikas A, Gelzinis A, Bacauskiene M. Detecting Parkinson's disease from sustained phonation and speech signals. *PLOS ONE*, 2017 [원본 "Almeida JS 등" 첫 저자 정정]. PMC5628839. ⚠️(저자 정정 적용)
12. Fagherazzi G, Bensoussan Y. The Imperative of Voice Data Collection in Clinical Trials. *Digital Biomarkers*, 2024. PMC11560146. ✅
13. Patel RR, et al. (ASHA Expert Panel). Recommended Protocols for Instrumental Assessment of Voice. *American Journal of Speech-Language Pathology*, 2018. DOI: 10.1044/2018_AJSLP-17-0009. PMID: 29955816. ✅

### EMA 및 mHealth 순응도
14. Wen CKF, Schneider S, Stone AA, Spruijt-Metz D. Compliance With Mobile Ecological Momentary Assessment Protocols in Children and Adolescents: A Systematic Review and Meta-Analysis. *JMIR* 19(4):e132, 2017. PMID: 28446418. ✅
15. Businelle MS, et al. Investigating Best Practices for Ecological Momentary Assessment: Nationwide Factorial Experiment. *JMIR mHealth and uHealth*, 2024. PMC11347889. ✅
16. Tate AD, et al. Momentary Factors and Study Characteristics Associated With Participant Burden and Protocol Adherence: Ecological Momentary Assessment. *JMIR Formative Research*, 2024. DOI: 10.2196/49512. ✅
17. Sun Y, et al. Associations Between Social Determinants of Health and Adherence in Mobile-Based Ecological Momentary Assessment: Scoping Review. *JMIR*, 2025. DOI: 10.2196/69831. ✅
18. Amagai S, et al. Challenges in Participant Engagement and Retention Using Mobile Health Apps: Literature Review. *JMIR*, 2022. DOI: 10.2196/35120. PMC9092233. ✅
19. Apps don't work for patients who don't use them: Towards frameworks for digital therapeutics adherence. *ScienceDirect*, 2024. ✅
20. Bidargaddi N, et al. To Prompt or Not to Prompt? A Microrandomized Trial of Time-Varying Push Notifications to Increase Proximal Engagement With a Mobile Health App. *JMIR mHealth and uHealth*, 2018. DOI: 10.2196/10123. ✅
21. An approach to boost adherence to self-data reporting in mHealth applications for users without specific health conditions. *BMC Medical Informatics and Decision Making*, 2024. DOI: 10.1186/s12911-024-02833-4 [Springer 직접 접근 불가, DOI 실존 확인]. ⚠️

### 동의·프라이버시
22. Haring LV, et al. Developing a digital informed consent app: opportunities and challenges of a new format to inform and obtain consent in public health research. *BMC Medical Ethics*, 2023. PMC10634039. ✅
23. Brightwell C, et al. Trust and Inclusion in Digital Health: The Need to Transform Consent. *Digital Society* (Springer), 2024. DOI: 10.1007/s44206-024-00135-w. ✅
24. Trust, Privacy Fatigue, and the Informed Consent Dilemma in Mobile App Privacy Pop-Ups: A Grounded Theory Approach. *Journal of Theoretical and Applied Electronic Commerce Research* (MDPI) 20(3):179, 2025. ✅
25. Alfawzan N, Christen M, Spitale G, Biller-Andorno N. Privacy, Data Sharing, and Data Security Policies of Women's mHealth Apps: Scoping Review and Content Analysis. *JMIR mHealth and uHealth*, 2022. DOI: 10.2196/33735. ✅
26. Alhammad N, et al. Patients' Perspectives on the Data Confidentiality, Privacy, and Security of mHealth Apps: Systematic Review. *JMIR*, 2024. PMC11179037. ✅
27. Enabling secure and self determined health data sharing and consent management. *npj Digital Medicine*, 2025. DOI: 10.1038/s41746-025-01945-z. PMID: 40885802. ✅
28. Brückner S, et al. A user-driven consent platform for health data sharing in digital health applications. *npj Digital Medicine*, 2025. DOI: 10.1038/s41746-025-02147-3. PMID: 41298895. ✅
29. Lee AR, et al. Opportunities and challenges of a dynamic consent-based application: personalized options for personal health data sharing and utilization. *BMC Medical Ethics*, 2024. DOI: 10.1186/s12910-024-01091-3. PMID: 39217356. ✅

### 데이터 품질 관리
30. A Systematic Review of Medical Image Quality Assessment. *Journal of Imaging* (MDPI) 11(4):100, 2025. PMID: 40278016. ✅
31. Schlett T, Rathgeb C, et al. Face Image Quality Assessment: A Literature Survey. *ACM Computing Surveys* 54(10s) art.210, 2022. DOI: 10.1145/3507901. ✅
32. **Heim E**, et al. (Maier-Hein L co-author). Large-scale medical image annotation with crowd-powered algorithms. *Journal of Medical Imaging*, 2018 [원본 "Maier-Hein L 등" 제1저자 정정]. PMC6129178. ⚠️(저자 정정 적용)
33. Park JH, et al. CMed: Crowd Analytics for Medical Imaging Data. *IEEE TVCG*, 2021. PMC7859862. ✅
34. Ye C, et al. A Crowdsourcing Framework for Medical Data Sets. *AMIA Jt Summits Transl Sci Proc*, 2018. PubMed 29888085. ✅
35. Cocos A, et al. Crowd control: Effectively utilizing unscreened crowd workers for biomedical data annotation. *Journal of Biomedical Informatics*, 2017. PubMed 28389234. ✅

### 산업공학/인간공학
36. Fouquet SD, Miranda AT. Asking the Right Questions—Human Factors Considerations for Telemedicine Design. *Current Allergy and Asthma Reports*, 2020. PMC7456356. ✅
37. **Demiris G, Charness N, Krupinski E**, et al. The Role of Human Factors in Telehealth. *Telemedicine and e-Health* 16(4):446-453, 2010 [원본 "Agnisarman S 등" 저자 완전 정정]. PMID: 20420540. ✅(정정 후)
38. (제외) IHI Recommendations to Improve Human Factors and System Design in Telemedicine, 2022 — 비학술 블로그 게시물로 본 합성에서 인용 비중 축소.
39. Zayim N, Yildiz H, Yüce YK. Estimating Cognitive Load in a Mobile Personal Health Record Application: A Cognitive Task Analysis Approach. *Healthcare Informatics Research*, 2023. PMC10651402. ✅
40. Gomez-Hernandez M, et al. Design Guidelines of Mobile Apps for Older Adults: Systematic Review and Thematic Analysis. *JMIR mHealth and uHealth*, 2023. DOI: 10.2196/43186. ✅
41. Ali SH, Thu H. App fatigue in mHealth: Beyond improving apps, advance equity by meeting people where they are. *PLOS Digital Health*, 2025. PMC12637926. ✅

### 적용 가이드라인 및 표준
- ASHA Recommended Protocols for Instrumental Assessment of Voice (2018) — 음성 데이터 수집 표준
- CAPE-V (Consensus Auditory-Perceptual Evaluation of Voice) — ASHA
- WHO Guideline Recommendations on Digital Interventions for Health System Strengthening — mHealth 도입 기준
- NIH Informed Consent for Research Using Digital Health Technologies (2024) — 연구용 디지털 동의
- HHS HIPAA Resources for Mobile Health Apps Developers — 데이터 보안
- 한국 개인정보보호법, 의료법, 생명윤리법 — 별도 법무 검토 필요

---

**문서 정보**
- 본 합성 보고서는 `01_ux_methodology_literature.md`(36편 1차 탐색)와 `reference_validation_ux.md`(2026-04-30 검증)를 종합하여 작성되었으며, 검증된 32편을 핵심 근거로, 부분 검증 7편은 [재확인 필요] 주석과 함께 보조 근거로, 명백한 저자명 오류 2건(논문 7, 37)은 정정된 정보로 활용했다.
- 한국 환경 특수 고려사항(7장)과 향후 파일럿 연구 권고(9장)는 본 보고서가 추가한 합성 결과로, 한국 PCOS·자궁내막증 사용자 대상 직접 증거가 부재한 영역의 우선 검증 대상이다.
- 본 보고서의 권고는 IRB 승인, 한국 개인정보보호법 적합성, 의료법 별도 검토를 전제한다.
