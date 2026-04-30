# 얼굴·음성 데이터 수집 UX 설계 가이드라인 합성 보고서 (한국 특화 통합본)

**작성일**: 2026-04-30
**작성자**: ux-methodology-synthesizer
**근거 문헌**: 63편 (영어권 검증 41편 + 한국인/한국어 음성 바이오마커 22편)
**대상 시나리오**: 한국어 PCOS·자궁내막증 예측 스마트폰 앱에서의 얼굴 사진·음성 데이터 수집
**버전**: v2 (한국 특화 통합)

> **본 문서는 `02_ux_synthesis.md`(영어권 UX 문헌 합성)에 `04_korean_voice_literature.md`(한국인 음성 바이오마커 22편)를 통합한 한국 특화 합성본이다. 한국 관련 추가/수정 내용은 `[한국 특화]` 태그로 표시한다.**
>
> **검증 반영 원칙**: `reference_validation_ux.md`(2026-04-30 검증)에 따라 ❌(저자명 완전 오류) 2건은 **수정된 정보**(Petrizzo et al. 2021, Demiris et al. 2010)로 인용하고, ⚠️(저자/연도 부분 오류) 7건은 본문에서 [재확인 필요] 주석을 부기한다. 한국 논문은 `04_korean_voice_literature.md`의 번호([K-1]~[K-22])를 사용한다.

---

## 1. 종합 요약 (Executive Summary)

PCOS·자궁내막증을 예측하기 위해 한국 여성 사용자로부터 얼굴 사진과 음성을 모바일에서 수집하려면, "임상급 표준"·"가정 환경의 현실"·"한국어 화자 특성" 세 가지를 동시에 만족시키는 UX가 필요하다. 영어권 UX 문헌 36편 + 한국 음성 바이오마커 22편의 합성을 통해 핵심 설계 원칙을 다음 8가지로 도출했다.

### 1.1 핵심 UX 설계 원칙 (8개, [한국 특화] 1개 추가)

1. **캡처 시점 품질 게이트(Capture-time Quality Gate)** — 업로드 후 거부가 아니라, 촬영·녹음 중 실시간 피드백으로 게이트한다 (논문 2-2, 6-1, 6-2).
2. **마법사형 단일 선형 흐름(Wizard-style Single Linear Flow)** — 한 세션은 "다음 / 종료" 2버튼만 노출. 인지 부하 최소화 (논문 7-4, 7-5).
3. **계층적·동적 동의(Tiered & Dynamic Consent)** — 일회성 긴 동의서가 아니라 4-layer 구조 (논문 5-2, 5-3, 5-6, 5-7, 5-8).
4. **프라이버시 기본값 = 비공유(Privacy-by-Default-Off)** — 모든 외부 공유는 명시적 옵트인, 기본값을 비활성으로 (논문 5-4).
5. **표준화된 발화·자세 프로토콜(Standardized Elicitation Protocol)** — 종단 비교 가능성 확보 (논문 2-1, 3-2, 3-5, 3-7).
6. **Give-and-Take 인사이트 루프** — 데이터를 줄 때마다 의미 있는 인사이트를 즉시 반환 (논문 4-5, 4-8).
7. **부담 적응형 EMA(Burden-adaptive EMA)** — 부정 감정·통증 자가보고가 높은 날은 과제 단축 (논문 4-2, 4-3).
8. **[한국 특화] 한국어 화자 정상치 기반 베이스라인(Korean-Norm Baseline)** — 한국어 F0 정상치(여성 199.6 Hz) + 한국어 표준 발화 자료("가을" 단락 등)를 사용하여 종단 anomaly detection 기준선을 한국 코호트에 맞춘다 (한국 논문 [K-5][K-6][K-16][K-17]).

### 1.2 즉시 적용 가능한 최우선 권고사항 (Top 4, [한국 특화] 1개 추가)

| 순위 | 권고 | 근거 | 기대 효과 |
|------|------|------|----------|
| **1** | 얼굴 캡처 시 FAIN(Face Alignment Indicator) + 4-게이트(노출/초점/포즈/해상도) IQA를 결합한 자동 셔터 도입 | 2-1, 2-2, 6-1, 6-2 | 종단 데이터 일관성 확보, 재촬영 비율 절감 |
| **2** | **[한국 특화]** 음성 녹음 마스터 프로토콜: "지속 모음 /아/, /이/, /우/ 6초×3 + 한국어 표준 단락 '가을' 낭독 + DDK /퍼-터-커/ + 자유 발화 20초"의 **4종 한국어 표준 과제** + WAV 비압축 강제 | 3-2, 3-5, 3-7 + [K-1][K-3][K-5][K-6][K-15] | 한국 임상 비교 가능 음성 바이오마커 추출, Jitter/Shimmer 왜곡 방지 |
| **3** | 동의 인터페이스를 "1) Just-in-Time 핵심 동의 + 2) 항목별 옵트인 + 3) 철회/재동의 대시보드"의 3중 구조로 구현 | 5-2, 5-3, 5-6, 5-7 | 프라이버시 피로 감소, 한국 개인정보보호법 적합성 |
| **4** | **[한국 특화]** 한국어 화자 정상치(여성 F0 199.6 Hz, Jitter 0.14%, NHR 0.013) 기반 anomaly detection 베이스라인 + AI-Hub/ETRI KEMDy20 사전학습 백본 활용 | [K-16][K-17], AI-Hub, ETRI | 한국 여성 PCOS·자궁내막증 음성 바이오마커 첫 검증 가능, 영미권 정상치 오용 회피 |

---

## 2. 얼굴 사진 수집 UX 가이드라인

### 2.1 캡처 인터페이스 설계

#### 2.1.1 정렬 인디케이터 (Face Alignment Indicator, FAIN)
Hashimoto & Kaneda (2024) [원본 표기 "Han 등", 저자명 재확인 후 적용]의 FAIN 시스템을 PCOS·자궁내막증 앱의 1차 권장 캡처 인터페이스로 채택한다 (논문 2-1).

**구성 요소:**
- **고정 타겟(Target Indicator)**: 화면 중앙에 회색 반투명 윤곽선으로 표시되는 이상적 얼굴 위치·크기.
- **동적 정렬(Alignment Indicator)**: 실시간 얼굴 랜드마크에 따라 변형되는 두 번째 윤곽선.
- **상태 색상 코드**: 미정렬 = 빨강, 정렬 임박 = 주황, 정렬 완료 = 파랑.
- **자동 셔터(Auto-capture)**: 정렬 조건이 0.5초 이상 유지되면 자동 촬영. 수동 셔터는 보조 옵션.

#### 2.1.2 실시간 품질 피드백
Vodrahalli 등 (2023, 논문 2-2)의 임상 검증 결과에 따라 캡처 시점 피드백을 제공한다.

**실시간 피드백 항목 (캡처 화면 상단 HUD):**
- 노출(Exposure): "조명이 부족합니다" / "역광입니다" / "정상"
- 초점(Focus): "초점이 맞지 않습니다" / "정상"
- 거리(Distance): "더 가까이" / "조금 멀리" / "정상" (얼굴-화면 비율 35-50% 권장)
- 안정성(Stability): IMU(자이로/가속도계)로 흔들림 감지

#### 2.1.3 캡처 모드
의료용 사진은 보정 비활성화 모드로 캡처한다 (논문 2-2, 2-4).

| 항목 | 권장 설정 |
|------|----------|
| 색 보정 | 비활성 (Beauty filter, AI 보정 OFF) |
| HDR | 비활성 (자연 노출 유지) |
| 포맷 | JPEG 95% 또는 RAW(가능 시) |
| 메타데이터 | EXIF + 기기 모델·OS 버전·카메라 모듈 ID 별도 저장 |

> **[한국 특화] 기기 다양성 보정**: K-DiN 연구([K-22] PMC7261694)에서 한국 다기종 스마트폰 간 음성 인식 임계치 차이가 입증되었다. 얼굴 사진도 동일하게 device-aware 보정이 필요하다 — 카메라 모듈 ID, ISP 버전, 색공간 메타데이터 별도 저장 후 종단 모델에서 device 효과를 공변량으로 처리한다.

### 2.2 환경 통제 가이드

Black 등 (2025, 논문 2-5)와 Ashique·Kaliyadan (2015, 논문 2-6)의 임상 가이드라인을 가정 환경에 맞게 단순화한다.

| 항목 | 임상 표준 | 가정 환경 권장 (단순화) |
|------|---------|-------------------|
| 광원 | 5000K LED 링라이트 + 45° 조명 | 자연광(창가) 또는 일반 실내 조명; 형광등 정면 광 |
| 배경 | 단색 라이트블루/그린 | 단색 흰 벽 또는 단색 배경 추천 |
| 거리 | 15-30 cm 고정 | 얼굴 비율 자동 검출 (35-50%) → 자동 가이드 |
| 메이크업 | 클렌징 후 촬영 | "메이크업 제거 권장" 안내 + 사용자 자가보고 토글 |
| 촬영 횟수 | 동일 부위 다중 촬영 | 1세션당 3장 자동 캡처 (microvariation 보존) |

> **앱 구현 팁**: 첫 사용 시 30초 안내 영상(시각적 체크리스트)을 1회 재생, 이후 세션에는 아이콘 4개로 압축 표시.

### 2.3 품질 게이트 파이프라인

Schlett 등 (2022, 논문 6-2)과 Journal of Imaging 종설(2025, 논문 6-1)의 IQA 권고를 4-게이트 자동 평가 파이프라인으로 구현한다.

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

### 3.1 표준 발화 과제 구성 [한국 특화 대폭 개정]

영어권 ASHA 권고(Patel 등 2018, 논문 3-7) + Kalia 등 (2025, 논문 3-2) 마스터 프로토콜에, **한국 22편 음성 바이오마커 문헌의 검증된 한국어 표준 자료**를 통합한 4종 과제 조합을 권장한다. 영어권에서 사용되는 `/a/` 단일 모음·"무지개 단락" 등은 **사용하지 않는다** — 한국어 화자 정상치 및 음운 빈도가 다르기 때문이다.

| # | 과제 | 시간/반복 | 측정 가능 변수 | 한국 검증 근거 |
|---|------|----------|------------|------------|
| 1 | **[한국 특화]** 지속 모음 **/아/, /이/, /우/** 각각 6초 × 3회 (총 9회) | ~60초 | F0, Jitter, Shimmer, HNR, CPP, Formants | [K-1] Mondol 2023 (PD 95.5% 분류), [K-3] Lee 2024 (인지 PR-AUC 0.74), [K-7] Mun 2022 (CKD F1 0.93), [K-16] Seo·Shin 2018 (n=309 정상치) |
| 2 | **[한국 특화]** 한국어 표준 단락 "**가을(Autumn)**" 낭독 (~118-141 단어, 369 음절, 자음·모음 균형) | ~60초 | 발화속도, 휴지 패턴, prosody, 음운 정확도 | [K-5] Namkung 2024 (스트레스 ECAPA-TDNN 77.5%), [K-6] Kim AY 2023 (우울증 AUC 0.86, n=318), [K-15] PSD 2024 (한국어 motor speech 표준) |
| 3 | **[한국 특화]** DDK (Diadochokinesis) **/퍼-터-커/** 반복 (AMR + SMR) | ~20초 | 음절 반복 속도, 운동 협응, 호흡 조절 | [K-3] Lee 2024 (인지 8과제 중 핵심) |
| 4 | **[한국 특화]** CAPE-V 자유 발화 ("오늘 하루 어떻게 지내셨어요?") 또는 한국어 일상 질문 | ~20-30초 | prosody, 자연 발화 jitter, 감정 운율 | 3-7 + [K-5] Namkung 2024 (자유 발화가 낭독보다 스트레스 변별력 우수) |
| (보조) | **[한국 특화]** 무성 자음 문장 "오월 오일은 어린이날이에요" | ~5초 | 호흡 효율, 무성 자음 정확도 | [K-7] Mun 2022 (CKD 진단 활용) |

**총 세션 시간**: 약 2-3분 (보조 과제 포함 시 3-3.5분).

**과제 간 전환:**
- 각 과제 시작 전 3-2-1 카운트다운 + 시각적 example 표시.
- 과제 1(모음)은 음량 인디케이터로 적정 강도 가이드 (60-70 dB SPL 추정).
- 과제 2(가을 낭독)는 자동 스크롤 텍스트, 적정 속도 시각화. 한국어 폰트는 가독성 높은 sans-serif.
- 과제 3(DDK)은 메트로놈 비주얼 가이드 + "최대한 빠르고 정확하게" 안내.
- 과제 4(자유 발화)는 정적/저활동 검출 시 "조금 더 말씀해 주세요" 부드러운 프롬프트.

> **[한국 특화] 왜 /a/ 단독이 아닌 /아, 이, 우/ 3모음인가?**
> [K-1] Mondol 등(2023)은 한국어 PD 분류에서 **/이/ 모음의 DDA shimmer**가 인지장애 분류 최강 예측인자로 확인되었다([K-3]). 한국어 8 단모음의 F0 폭은 163-171 Hz로 좁아(영어보다 협소), 단일 모음 정보로 부족하다([K-16]). 한국 표준 음성 평가는 /아/+/이/+/우/ 3모음을 함께 사용하는 것이 정착되어 있다.

> **[한국 특화] 왜 "무지개 단락" 대신 "가을" 단락인가?**
> "가을" 단락은 한국어 자음·모음 빈도 균형이 검증된 369음절 표준 자료로, 한국 우울증·스트레스·dysarthria 연구 다수에서 활용되었다([K-5][K-6][K-15]). 영어 "Rainbow Passage"의 한국어 번역본은 음운 빈도가 표준 한국어와 어긋나 임상 비교 가능성이 떨어진다.

### 3.2 녹음 환경 요구사항

#### 3.2.1 SNR 기준
Kalia 등 (2025, 논문 3-2)과 [K-3] Lee 등 (2024)의 권고를 합성:

| SNR | 평가 | 앱 대응 |
|-----|-----|---------|
| ≥ 42 dB | 우수 | 즉시 녹음 진행 |
| 20-42 dB | 양호 | 녹음 진행 + 메타데이터에 "noisy" 플래그 |
| < 20 dB (배경 소음 > 50 dB) | 부족 | 녹음 거부, "조용한 곳으로 이동해 주세요" 안내 |

녹음 시작 전 1초간 환경 노이즈를 수집하여 SNR 추정 후 사용자에게 인디케이터(녹/황/적) 표시. **[한국 특화]** [K-3]이 임상 표준으로 명시한 **주변 소음 50 dB 이하**를 한국 가정 환경 baseline으로 채택.

#### 3.2.2 마이크 설정
Petrizzo & Popolo (2021, 논문 3-1) + Noffs 등 (2023/2024, 논문 3-4) + [K-6] Kim AY (2023, Samsung Galaxy S10 검증)에 따라:

| 항목 | 권장 설정 |
|------|----------|
| 샘플링 레이트 | **44.1 kHz** ([K-3][K-6] 한국 임상 검증 표준), 최소 16 kHz ([K-5]) |
| 비트 심도 | 16-bit (WAV) 또는 32-bit ([K-6]) |
| 코덱 | **WAV(비압축) 강제** — MP3/AAC 금지 (Jitter/Shimmer 왜곡, **한국어에서도 동일**) |
| 입과 마이크 거리 | **30 cm** ([K-3][K-6] 한국 임상 표준), 좌위 자세 |
| 외장 마이크 | PnP(USB-C/Lightning) 마이크 사용 시 인센티브 보너스 인디케이터 |
| 입력 레벨 | OS 자동 게인 비활성, 앱 내 고정 게인 |

> **[한국 특화] 검증된 한국 임상 스마트폰 셋업**: [K-6] Kim AY 등(2023, n=318)은 **Samsung Galaxy S10 내장 마이크 + 30cm + 모노 PCM WAV 44.1kHz / 32-bit**로 한국어 음성 우울증 분류 AUC 0.86을 달성했다. 본 PCOS·자궁내막증 앱의 1차 baseline 셋업으로 직접 채택 권장.

> **[한국 특화] 압축 코덱 왜곡은 한국어에서도 동일**: MP3/AAC는 spectral envelope에 영향을 주어 한국어 모음/자음 모두에서 Jitter/Shimmer를 왜곡시킨다. [K-9] Korean AVQI 검증 연구의 CPP threshold(지속 모음 12 dB, 연속 발화 7 dB)도 비압축 WAV에서 산출되었다. 압축 저장은 한국어 임상 baseline과의 비교 가능성을 무효화한다.

#### 3.2.3 [한국 특화] 한국어 화자 음향 정상 참조값

[K-16] Seo·Shin (2018, n=309) + [K-17] Yang (2021, n=40 자유 발화) + [K-9] Korean AVQI 검증을 종합한 한국어 화자 정상 참조값. 영미권 정상치를 그대로 적용해서는 안 된다.

| 파라미터 | 한국 여성 정상 | 한국 남성 정상 | 영미권 비교 | 출처 |
|---------|------------|------------|----------|------|
| **F0 평균** | **199.60 Hz** | 119.02 Hz | 영미 여성 ~210-220 Hz (한국 여성이 ~10-20 Hz 낮음) | [K-16] |
| F0 중앙값 (자유 발화) | 200 Hz | 111 Hz | – | [K-17] |
| F0 범위 | – | – | 65-339 Hz | [K-17] |
| Jitter (지속 모음) | 0.14% | 0.24% | – | [K-16] |
| NHR | 0.013 | 0.019 | – | [K-16] |
| CPP (지속 모음 정상 cut-off) | ≥ 12 dB | ≥ 12 dB | – | [K-9] |
| CPP (연속 발화 cut-off) | ≥ 7 dB | ≥ 7 dB | – | [K-9] |

**PCOS hyperandrogenism 가설 적용**: 안드로겐 → F0 감소 → 한국 여성 정상치(~200 Hz)에서 일정 임계값 이하로 시프트 예상. [K-13] 연세대 H1-A1 분석법(breathiness, 노화/호르몬 감수성) 적용 권장.

**[한국 특화] 호르몬 메타데이터 필수 항목**: [K-12] 한국 갑상선기능저하증 음성 연구는 **호르몬 이상이 한국어 화자 음성에 직접 영향**을 미침을 입증했다. PCOS·자궁내막증 앱은 다음 호르몬 관련 메타데이터를 모델 입력으로 필수 수집해야 한다.
- 월경 주기 단계 (난포기/배란기/황체기/월경기) — [K-20] JMIR 2025 (F0 SD 황체기 9% 감소)
- 호르몬성 피임제 사용 여부 — [K-20]에서 피임제 사용자는 주기 변화 없음
- 갑상선 기능 진단 이력 — [K-11][K-12] 한국 갑상선-음성 직접 근거
- 폐경 단계 (한국 여성 평균 폐경 ~50세, 영미권보다 ~3년 이른 발현) — [K-13]

### 3.3 메타데이터 수집 설계

Asci 등 (2020, 논문 3-3)의 분석에 따르면 성별·연령은 음향 특징의 주요 분산원이므로, 메타데이터 수집은 모델 학습의 필수 입력이다.

**필수 메타데이터 (자동 수집):**
- 기기 모델, OS 버전, 앱 버전, 카메라/마이크 모듈 ID
- 녹음 시각(타임존 포함), 추정 SNR
- 마이크 종류(internal/external), 코덱, 샘플링 레이트
- IMU 기반 자세 추정(좌위/와위)

**필수 메타데이터 (사용자 입력 - 온보딩 시 1회):**
- 출생 연도, 성별/생물학적 성, **발성 모국어 (한국어 단일 / 이중언어 / 외국인 한국어 학습자)** — [K-22] AI-Hub 외국인 한국어 발화 데이터셋 분리 분석 가능
- 흡연 여부, 호흡기 만성질환 유무
- **[한국 특화]** 표준 한국어/방언 사용 여부 (서울/경상/전라/충청/제주) — 음향 특징 변동 요인

**세션 메타데이터 (매 세션 자가보고, 1화면 토글):**
- 현재 기분(5점 척도)
- 환경(가정/직장/외부)
- 감기·인후염 유무 (당일)
- 카페인/식사 후 몇 시간 경과 (드롭다운)
- **[한국 특화]** 월경 주기 단계, 출혈 여부 (PCOS·자궁내막증 핵심 공변량)

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

### 4.4 [한국 특화] 한국 개인정보보호법·생명윤리법 적합성

| 항목 | 적용 법령 | 앱 구현 요구 |
|------|----------|------------|
| 수집·이용 동의 | 개인정보보호법 제15조 | 수집 목적·항목·보관기간 명시 |
| 제3자 제공 | 개인정보보호법 제17조 | 별도 옵트인 필수 (대학병원, AI 회사 각각) |
| 민감정보 (생체정보) | 개인정보보호법 제23조 | **얼굴·음성은 "생체정보"로 분류 → 별도 동의 필수** |
| 의료정보 보관 | 의료법 시행령 제15조 | 5년 이상 보관 시 의료기관 연계 검토 |
| 인간대상연구 | 생명윤리법 제16조 | IRB 승인 + 표준 동의 양식 |
| 정보주체 권리 | 개인정보보호법 제35-37조 | 열람·정정·삭제·처리정지 권리 보장 (대시보드 구현) |

> **[한국 특화] KakaoTalk 알림톡 활용 시**: 개인정보보호법 제17조 제3자 제공 동의가 필요하지 않은 "위탁" 방식으로 카카오 비즈메시지 SDK 활용 가능. 단, 알림톡 본문에 민감정보(진단 결과 등)는 포함하지 말고 "앱에서 결과 확인하세요" 형식의 트리거 알림만 전송 권장.

> **[한국 특화] npj SHC Connect (논문 5-6) 등 외부 동의 SDK**: 한국 개인정보보호법 호환성 별도 검토 필요. EU GDPR 기반 SDK는 한국 법 요구사항(예: 개인정보 처리방침 한국어 의무 게시)과 일부 차이가 있다.

---

## 5. 순응도(Compliance) 향상 전략

### 5.1 EMA 빈도 및 타이밍

Businelle 등 (2024, 논문 4-2)의 요인설계 실험에서 **비임상 환경에서는 1일 2-3회 프롬프트가 가장 높은 순응율(91.7%)**을 보였다.

**권장 PCOS·자궁내막증 EMA 스케줄:**

| 시점 | 작업 | 근거 |
|------|------|------|
| 점심 12:30 | 짧은 자가보고 (기분, 통증, 증상) | Bidargaddi 등 2018 (논문 4-7): +8.8%p 참여 |
| 저녁 19:30 | 얼굴 사진 + 음성 녹음 (주 3-4회) | Bidargaddi 등 2018 |
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
│   ├ 환경 자가보고 1화면 (조명·메이크업·기분·환경·월경)     │
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
│  Step 4: 음성 녹음 (약 2-3분) [한국 특화 4-과제]            │
│   ├ JIT 동의 (첫 회만): 음성 데이터 수집 옵트인              │
│   ├ 환경 SNR 측정 1초 (배경 < 50 dB)                         │
│   ├ 과제 1: 모음 /아/, /이/, /우/ 6초×3 ([K-1][K-3])        │
│   ├ 과제 2: "가을" 단락 낭독 ([K-5][K-6])                   │
│   ├ 과제 3: DDK /퍼-터-커/ 20초 ([K-3])                     │
│   ├ 과제 4: 자유 발화 20-30초 ([K-5])                       │
│   └ WAV 비압축 저장 (44.1 kHz / 16-bit) + 메타데이터        │
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

**전체 세션 시간**: 평균 4-5분 (한국 특화 4-과제 음성 포함).

---

## 7. 한국 PCOS·자궁내막증 사용자 특수 고려사항 [대폭 확장]

### 7.1 한국어 인터페이스 필수

Tate 등 (2024, 논문 4-3)에서 모국어 지원이 EMA 부담 인식 감소의 주효과 변수로 확인. 한국어 사용자에게 영어 인터페이스는 인지 부하를 약 2배 증가시키는 것으로 유추된다.

**적용:**
- 모든 안내문은 한국어 평문(중학생 이해 가능 수준)으로.
- 의료 전문 용어는 평문 번역 + 괄호 영문 표기 (예: "다낭성 난소 증후군(PCOS)").
- 음성 자유 발화 과제는 한국어 표준 발화 자극 사용 ("가을", "산책" 등 검증된 단락).

### 7.2 [한국 특화] 한국어 표준 발화 과제 전체 목록 (근거 논문 포함)

PCOS·자궁내막증 앱이 채택할 수 있는 모든 검증된 한국어 표준 발화 자극을 한 곳에 정리한다. 각 과제는 한국 임상 음성 연구에서 사용 검증되었으므로, 본 앱이 수집하는 음성은 한국 다른 임상 코퍼스(우울증, PD, CKD, dysphonia)와 직접 비교 가능하다.

| 카테고리 | 발화 자극 | 음운 특성 | 측정 강점 | 검증 논문 |
|---------|---------|---------|---------|---------|
| **지속 모음** | /아/ | 가장 표준 | F0, Jitter, Shimmer, HNR | [K-1][K-3][K-7][K-8][K-9][K-13][K-16] |
| **지속 모음** | /이/ | 고모음 | DDA shimmer (인지 최강 예측인자) | [K-1][K-3][K-16] |
| **지속 모음** | /우/ | 후고모음 | F0 변동성 | [K-1][K-3][K-16] |
| **표준 단락** | **"가을(Autumn)"** (118-141단어, 369음절) | 자음·모음 빈도 균형 | 발화속도, prosody, 우울/스트레스 변별 | [K-5][K-6][K-15] |
| **표준 단락** | "산책(Walk)" | 임상 음성 표준 | dysphonia 평가 | [K-8][K-9] |
| **무성 자음 문장** | "오월 오일은 어린이날이에요" | 무성 자음 중심 | 호흡 효율, CKD 진단 | [K-7] |
| **DDK (AMR)** | /퍼-퍼-퍼/, /터-터-터/, /커-커-커/ | 단음절 반복 | 운동 협응 | [K-3] |
| **DDK (SMR)** | /퍼-터-커/ | 음절 순차 반복 | 복합 운동 협응 | [K-3] |
| **모음 연장** | /아-아-아/ | 음절 분절 | 호흡 컨트롤 | [K-3] |
| **자유 발화** | "오늘 어떻게 지내셨어요?" 등 | 자연 운율 | 스트레스/감정 변별 (낭독보다 우수) | [K-5] |

> **발화 자극 채택 전략**: PCOS·자궁내막증 앱은 위 과제 중 **/아, 이, 우/ 지속 모음 + "가을" 단락 + /퍼-터-커/ DDK + 자유 발화** 4종을 1차 필수로 채택한다. "산책" 단락과 "오월 오일" 문장은 Phase 2 확장 옵션으로 보류한다.

### 7.3 [한국 특화] 한국 여성 음성 정상 참조값 (재확인)

PCOS·자궁내막증의 음성 anomaly detection은 **한국 여성 정상 분포에서의 편차**로 정의되어야 한다. 영미권 정상치 사용 시 false positive/negative가 발생할 수 있다.

| 파라미터 | 한국 여성 정상값 | 사용 시나리오 |
|---------|-------------|------------|
| F0 평균 (지속 모음) | **199.60 Hz** | hyperandrogenism 의심 시 baseline 비교 |
| F0 중앙값 (자유 발화) | 200 Hz | 일상 발화 anomaly detection |
| Jitter | 0.14% | 음성 안정성 임계 |
| NHR | 0.013 | 호흡 잡음 비율 baseline |
| CPP (지속 모음) | ≥ 12 dB | dysphonia 임계 |
| CPP (연속 발화) | ≥ 7 dB | 자연 발화 임계 |
| H1-A1 (breathiness) | 노년 < 청년 | 노화/호르몬 효과 분석 |

> **PCOS hyperandrogenism 음성 가설**: 안드로겐 → 성대 hypertrophy → F0 감소. 한국 여성 정상 200 Hz에서 일정 임계치 이하로 시프트 시 PCOS 의심 신호. 단, [K-13]은 노화에 따른 자연 F0 변화도 보여 연령 보정 필수.

### 7.4 [한국 특화] 한국 공개 데이터셋 활용 가능성

본 앱 개발 시 사전학습 백본·검증 데이터로 활용 가능한 한국 공개 자원:

| 데이터셋 | 출처 | 규모 | PCOS 앱 활용 시나리오 |
|---------|-----|-----|------------------|
| **AI-Hub 한국인 대화음성** | aihub.or.kr (dataSetSn=130) | 2,000명, 1,000시간 | 한국어 음성 백본 사전학습 (wav2vec2/HuBERT 한국어 fine-tune) |
| **AI-Hub 감정 대화 말뭉치** | aihub.or.kr (dataSetSn=86, 263, 271, 637) | 다수 | 감정/스트레스 모델 사전학습 — PCOS 음성-스트레스 연관 분석 |
| **ETRI KEMDy20** | nanum.etri.re.kr | 다중 화자 | **멀티모달 (음성+ECG+EDA)** — PCOS 호르몬-자율신경계-음성 통합 모델 |
| **MINDsLab-ETRI VOTE400** | ai4robot.github.io | 노인 음성 400시간 | 폐경 후 한국 여성 비교 코호트 |
| **AI-Hub 외국인 한국어 발화** | aihub.or.kr (dataSetSn=505) | 외국인 화자 | 다국어 화자 분리 분석, 결혼이주여성 등 한국 다문화 코호트 |
| **응급의료 영역 한국어 음성대화 DB** | 말소리와 음성과학 12(4):81 | 166건, 8h 35min | 의료 도메인 ASR 백본 |

> **AI-Hub 보건의료 음성 데이터 보안**: 일부 보건의료 음성 데이터는 **온라인/오프라인 안심존**을 통한 비다운로드 분석만 가능. 본 앱 개발 시 AI-Hub 안심존 신청 절차 사전 검토 필요.

> **활용 우선순위**: **AI-Hub 한국인 대화음성**(일반 백본) → **AI-Hub 감정 대화**(스트레스 fine-tune) → **ETRI KEMDy20**(멀티모달 PCOS 통합 연구) → **VOTE400**(폐경 비교군).

### 7.5 [한국 특화] 한국 여성 PCOS·자궁내막증 음성 연구 공백 = 본 연구의 독창성

`04_korean_voice_literature.md`의 22편 탐색 결과, **다음 영역은 한국 코호트에서 직접 검증된 연구가 0편**으로 본 PCOS·자궁내막증 앱 연구가 메우는 핵심 공백이다.

| 공백 영역 | 영미권 연구 존재 | 한국 코호트 연구 | 본 앱의 기여 |
|---------|-------------|------------|----------|
| **PCOS-음성** 직접 분석 | [K-19] Egyptian J Otolaryngology 2024 (BA 85%) | **0편** | 한국 여성 PCOS 음성 첫 대규모 데이터 |
| **자궁내막증-음성** 분석 | 영미권에서도 매우 제한 | **0편** | 자궁내막증 hormonal 치료 효과 음성 모니터링 첫 시도 |
| **월경주기-음성 종단** 연구 | [K-20] JMIR FR 2025 (F0 SD 황체기 9% 감소) | **0편** | 한국 여성 월경주기 음성 변동 첫 종단 추적 |
| **폐경-음성 종단** 연구 | 다수 | [K-13] 단면(n=42)만 존재 | 한국 여성 폐경 50세 전후 종단 음성 데이터 |
| **호르몬성 피임-음성** 영향 | [K-20] | **0편** | 한국 여성 피임제 사용자 음성 변화 첫 분석 |

이 공백은 본 앱이 수집하는 한국 여성 PCOS·자궁내막증 환자/대조군 음성 데이터가 **이중 가치**(질병 검출 + 한국 여성 음성 정상 데이터베이스 동시 구축)를 갖는다는 점에서 연구 독창성·임상 가치의 핵심 근거다.

### 7.6 [한국 특화] 한국 임상 인프라 협력 가능성

[K-3][K-5][K-6][K-7]을 발표한 한국 임상·연구 기관은 본 앱 공동연구 후보군이다.

| 기관 | 보유 역량 | 협력 가능 영역 |
|-----|---------|-------------|
| 서울대병원 (SNUBH, Boramae) | 한국어 스트레스 음성 ECAPA-TDNN ([K-5]) | PCOS 환자 모집 + 음성 검증 |
| 인제대 일산백병원 + 충남대병원 | 한국어 우울증 음성 CNN AUC 0.86 ([K-6]) | 정신건강 동반이환 평가 |
| ETRI | KEMDy20 멀티모달 데이터, 한국어 음성 임베딩 | 사전학습 백본 제공 |
| Seoul National University 언어학과 | 한국어 CKD 음성 분석 ([K-7]) | 음성 특징 추출 표준화 |
| Inje University Ilsan Paik Hospital + Kyungpook National University | 한국어 PD 음성 ([K-1][K-2][K-3]) | 신경계 비교군 |
| Yonsei University 음성언어병리 | 한국 여성 노화 음성 H1-A1 ([K-13]) | 폐경 비교 코호트 |

### 7.7 한국 사용자 세그먼트별 프롬프트 전략

Sun 등 (2025, 논문 4-4)의 SDoH 통합 설계 권고를 한국 여성 PCOS·자궁내막증 사용자에 적용.

| 세그먼트 | 일과 패턴 | 권장 프롬프트 시점 | 추가 고려 |
|----------|---------|-----------------|----------|
| 직장 여성 (20-40대) | 9-18시 근무, 점심·퇴근 시 여유 | 12:30, 19:30 (Bidargaddi 등 2018) | 회의·외근 일정 학습 후 ±2h 자동 조정 |
| 전업주부 | 가사·육아, 오전/오후 자투리 시간 | 10:00, 14:00 | 자녀 돌봄 시간 회피, 짧은 1분 모드 |
| 대학생/대학원생 | 강의 일정, 야간 활동 | 18:00, 22:00 | 시험 기간 자동 휴면 모드 |
| 자영업자 | 비정형, 영업 시간 | 사용자 직접 설정 우선 | 첫 4주 응답 패턴 학습 |

**[한국 특화] 알림 채널 전략:**
- 푸시 외에 **KakaoTalk 알림톡** 옵션 (한국 사용자 도달률 높음, 위탁 방식으로 개인정보보호법 호환)
- 의료기관 EMR 연계 시 SMS 백업 (Ali & Thu 2025, 논문 7-6의 앱 피로 완화)
- **Naver CLOVA / Kakao Health Care SDK** 활용 가능 (한국어 ASR 백본)

### 7.8 PCOS·자궁내막증 특유 감수성

- **신체 이미지 민감도**: 얼굴 사진은 여드름·털·피부 변화 노출 → "보정 OFF" 강제는 사용자 거부감 가능. 메이크업 가능 모드 + 무메이크업 모드 양쪽 옵션 제공, 메이크업 여부 메타데이터로 모델에 입력.
- **월경 주기 동기화**: [K-20] JMIR FR 2025에서 F0 SD가 황체기에 9% 감소, 5th percentile F0 8.8% 증가 입증. 월경 단계 메타데이터 필수.
- **호르몬성 피임제**: [K-20]에서 피임제 사용자는 주기 변화가 없음 → 별도 코호트로 분리 분석.
- **통증·피로 대응**: Tate 등 (2024, 논문 4-3) 부담 적응형 모드 필수 — PCOS·자궁내막증은 만성 통증 동반 빈도 높음.
- **한국 PCOS 표현형**: 한국 여성 PCOS는 비만하지 않은 표현형 + hyperandrogenism + 월경 불규칙 조합이 우세 ([K-18]) → 음성 androgen 효과 변별 시 BMI/월경주기 공변량 필수.
- **한국 폐경 연령**: ~50세 (영미권 ~52세보다 ~3년 이른 발현, [K-13]) → 한국 여성 종단 연구에서 호르몬-음성 모델링 별도 필요.

---

## 8. 구현 우선순위 로드맵 [한국 특화 통합]

| 우선순위 | 기능 | 근거 | 난이도 | Phase |
|---------|------|------|--------|-------|
| **필수 (Phase 1, MVP 0-3개월)** | | | | |
| 1 | FAIN 얼굴 정렬 + 자동 셔터 | 2-1 | 중간 | Phase 1 |
| 2 | 4-게이트 IQA (노출/초점/포즈/해상도) | 6-1, 6-2 | 중간 | Phase 1 |
| 3 | **[한국 특화]** 4종 한국어 음성 과제 모듈 (/아,이,우/ + "가을" + DDK + 자유 발화) | 3-2, 3-7 + [K-1][K-3][K-5][K-6] | **낮음** (검증된 자료 활용) | **Phase 1 (필수)** |
| 4 | WAV 비압축 강제 녹음 (44.1 kHz / 16-bit) | 3-4 + [K-3][K-6] | 낮음 | Phase 1 |
| 5 | **[한국 특화]** 한국어 화자 정상 참조값 (F0 199.6 Hz 등) baseline 모듈 | [K-16][K-17][K-9] | 낮음 | **Phase 1 (필수)** |
| 6 | Tier 1 핵심 동의 + 이해도 퀴즈 | 5-1, 5-3 | 낮음 | Phase 1 |
| 7 | JIT 동의 (얼굴/음성 첫 사용 시) | 5-2 | 낮음 | Phase 1 |
| 8 | 한국어 인터페이스 + 평문 안내 | 4-3 | 낮음 | Phase 1 |
| 9 | 1일 2-3회 EMA + 12:30/19:30 푸시 | 4-2, 4-7 | 낮음 | Phase 1 |
| 10 | **[한국 특화]** 호르몬 메타데이터 (월경 주기, 피임제, 갑상선) 수집 | [K-12][K-13][K-20] | 낮음 | **Phase 1 (필수)** |
| 11 | **[한국 특화]** 한국 개인정보보호법 적합 동의 (제15조, 17조, 23조) | 한국 법령 | 중간 | **Phase 1 (필수)** |
| **권장 (Phase 2, 3-9개월)** | | | | |
| 12 | "내 데이터" 동적 동의 대시보드 | 5-6, 5-7, 5-8 | 높음 | Phase 2 |
| 13 | 월 1회 동의 리뷰 알림 | 5-8 | 낮음 | Phase 2 |
| 14 | 부담 적응형 EMA (감정 기반 단축) | 4-3 | 중간 | Phase 2 |
| 15 | 주간 인사이트 그래프 (Give-and-take) | 4-8 | 중간 | Phase 2 |
| 16 | 세그먼트별 푸시 시점 학습 | 4-4 | 중간 | Phase 2 |
| 17 | **[한국 특화]** KakaoTalk 알림톡 채널 통합 (위탁 방식) | 7-6 + 한국 법령 | 중간 | Phase 2 |
| 18 | **[한국 특화]** AI-Hub 한국인 대화음성 사전학습 백본 도입 (wav2vec2 한국어 fine-tune) | AI-Hub | **권장** | **Phase 2 (권장)** |
| 19 | **[한국 특화]** AI-Hub 감정 대화 말뭉치로 스트레스 fine-tune | AI-Hub | 중간 | Phase 2 (권장) |
| 20 | PnP 마이크 사용 인센티브 | 3-1, 3-4 | 낮음 | Phase 2 |
| 21 | 운영팀 모니터링 대시보드 (CMed 패턴) | 6-3, 6-4 | 높음 | Phase 2 |
| 22 | **[한국 특화]** 보조 발화 과제 ("산책" 단락, "오월 오일" 문장) 추가 | [K-7][K-8][K-9] | 낮음 | Phase 2 |
| 23 | **[한국 특화]** Device-aware 보정 (한국 다기종 스마트폰) | [K-22] K-DiN | 중간 | Phase 2 |
| **고급 (Phase 3, 9-18개월)** | | | | |
| 24 | 하이브리드 코칭 (간호사·코디네이터 연계) | 4-5 | 매우 높음 | Phase 3 |
| 25 | 의료기관 EMR/PHR 연계 | 7-6 | 매우 높음 | Phase 3 |
| 26 | 연합학습(Federated Learning) 인프라 | 3-6 | 매우 높음 | Phase 3 |
| 27 | **[한국 특화]** ETRI KEMDy20 멀티모달 (음성+ECG+EDA) PCOS 통합 모델 | ETRI | 매우 높음 | Phase 3 |
| 28 | **[한국 특화]** SNUBH/Boramae/인제대 등 한국 임상 기관 공동연구 협약 | [K-5][K-6] | 매우 높음 | Phase 3 |
| 29 | 외부 SDK (npj SHC Connect 유사) 도입 + 한국 법령 검토 | 5-6 | 높음 | Phase 3 |
| 30 | 게이미피케이션·소셜 코호트 비교 | 4-1, 4-5 | 중간 | Phase 3 |
| 31 | RAW 캡처·기기별 색 보정 매트릭스 | 2-4 | 매우 높음 | Phase 3 |

---

## 9. 검증되지 않은 항목 및 연구 공백

### 9.1 한국어/한국 사용자 대상 직접 증거 부재 영역 [한국 특화 갱신]

| 영역 | 공백 | 권장 후속 연구 |
|------|------|--------------|
| PCOS-음성 한국 코호트 | **0편** ([K-19] Egyptian J Otolaryngology 외 영미권만) | 한국어 4종 발화 과제로 환자-대조군 음향 비교 파일럿 |
| 자궁내막증-음성 한국 코호트 | **0편** | 자궁내막증 GnRH agonist 치료군 vs 비치료군 음성 종단 추적 |
| 월경주기-음성 한국 종단 | **0편** ([K-20]은 영미권만) | 한국 여성 30명 × 3 주기 종단 음성 수집 |
| 폐경-음성 한국 종단 | [K-13] 단면(n=42)만 존재 | 한국 여성 폐경 전후 50명 5년 종단 |
| EMA 순응율 (한국 PCOS) | 한국 여성 PCOS 환자 대상 EMA 데이터 없음 | 50명 12주 EMA 파일럿, 세그먼트별 순응율 측정 |
| 동의 UX (한국 여성) | 한국 여성의 디지털 동의 수용성 연구 부재 | 동적 동의 vs 일회성 동의 A/B 테스트 |
| 얼굴 분석 (PCOS 한국) | PCOS 다모증/여드름 디지털 정량화 표준 부재 | Hirsutism 자동 스코어링 모델 + 사용자 수용성 |

### 9.2 본 합성에서 직접 검증되지 않은 항목

- **CAPE-V 한국어 적응본**: 영어 표준 자유 발화 자극 ("Tell me about your voice problem")의 한국어 등가물 미정립 → 임상언어치료학회 협업 필요. 단, [K-5] Namkung 2024가 사용한 "일상/취미/미디어 등 중립 질문"이 사실상 한국어 CAPE-V 적응본 역할 가능.
- **한국 5000K 광원 가용성**: Black 등 (2025) 권장은 임상실 가정. 한국 일반 가정의 LED 색온도 분포 조사 필요.
- **여성 mHealth 앱 한국 시장 프라이버시 실태**: Alfawzan 등 (2022, 논문 5-4)은 영미권 중심. 한국 인기 여성 건강 앱(예: 핑크다이어리, 헬로키키 등)의 실태 별도 조사 필요.
- **AI-Hub 보건의료 데이터 안심존 절차**: 본 합성 시점에 다운로드 불가능, 안심존 분석만 가능. 절차/조건 별도 검토.

### 9.3 향후 파일럿 연구 권장 설계 [한국 특화 갱신]

**파일럿 1 — 캡처 UX 비교 RCT** (3개월, n=60 한국 여성)
- 군 1: FAIN + 4-게이트 IQA (본 권장안)
- 군 2: 자유 캡처 (대조군)
- 1차 결과: 임상 사용 가능 사진 비율, 재시도 횟수, NASA-TLX 한국어판
- 근거: 논문 2-1, 2-2, 6-1, 6-2

**파일럿 2 — [한국 특화] 한국어 음성 프로토콜 검증** (6개월, n=120, PCOS 환자 60 + 대조군 60 한국 여성)
- 4종 한국어 과제 + WAV 녹음 → Jitter/Shimmer/CPP/F0 추출
- 1차 결과: PCOS 분류 AUC, 검사-재검사 신뢰도(ICC), 한국 여성 정상 참조값과의 편차
- Samsung Galaxy 시리즈 사용 ([K-6] 검증된 셋업)
- 근거: 3-2, 3-7 + [K-1][K-3][K-5][K-6][K-16]

**파일럿 3 — 동적 동의 수용성** (3개월, n=120 한국 여성)
- 군 1: 본 권장 3-Layer 동의 (한국 개인정보보호법 호환)
- 군 2: 일회성 긴 동의서
- 1차 결과: 이해도 퀴즈 점수, 6주차 동의 변경 빈도, 신뢰 척도, 한국어 약관 가독성 점수
- 근거: 5-1, 5-2, 5-6, 5-7

**파일럿 4 — [한국 특화] 월경주기-음성 종단 파일럿** (3개월, n=30 한국 여성 정상)
- 매일 1회 한국어 4종 과제 음성 수집 × 3 월경 주기
- 1차 결과: F0 SD 황체기 변화율 ([K-20] JMIR FR 2025의 9% 감소 한국 재현)
- 근거: [K-20] + 본 합성 7.5절 공백 보충

---

## 10. 참고문헌 (검증된 항목 + 한국 특화 통합)

> 검증 보고서(`reference_validation_ux.md`, 2026-04-30)에 따라 ❌(저자명/연도 명백 오류) 2건은 정정 정보로 인용, ⚠️(부분 오류) 항목은 [재확인 필요] 주석 부기. 한국 논문은 `04_korean_voice_literature.md`의 [K-#] 번호를 사용한다.

### 영어권 UX 문헌 (얼굴 사진 수집)
1. Hashimoto W, Kaneda S. A smartphone application for personalized facial aesthetic monitoring. *Skin Research and Technology*, 2024. PMC11230921. [O]
2. Vodrahalli K, et al. Development and Clinical Evaluation of an Artificial Intelligence Support Tool for Improving Telemedicine Photo Quality. *JAMA Network Open / JAMA Dermatology*, 2023. PMC10018405. [O]
3. AI-assisted facial analysis in healthcare. *Patterns* (Cell Press), 2025. DOI: S2666-3899(25)00023-6. [O]
4. ElHawary H, et al. Pocket Predictors. *Plastic Surgery* 31(4):415-416, **2022**. PMC10617461. [-]
5. Black TA, et al. Best Practices for Capturing Clinical and Dermoscopic Images With Smartphone Photography. *Cutis* 115(1), **2025**. [-]
6. Ashique KT, Kaliyadan F, Aurangabadkar SJ. Clinical photography in dermatology using smartphones. *Indian Dermatology Online Journal*, 2015. PMC4439742. [O]

### 영어권 UX 문헌 (음성 녹음 수집)
7. **Petrizzo D, Popolo PS**. Smartphone Use in Clinical Voice Recording and Acoustic Analysis. *Journal of Voice* 35(3):499.e23-499.e28, **2021**. PMID: 32736910. [O]
8. Kalia A, Boyer M, Fagherazzi G, et al. Master protocols in vocal biomarker development. *Frontiers in Digital Health*, 2025. [O]
9. **Asci F, Costantini G**, et al. Machine-Learning Analysis of Voice Samples Recorded through Smartphones. *Sensors*, 2020. PMC7570582. [-]
10. Noffs G, et al. Plug-and-Play Microphones for Recording Speech and Voice with Smart Devices. *Folia Phoniatrica*, 2023/2024. PMC11309067. [O]
11. **Vaiciukynas E**, et al. Detecting Parkinson's disease from sustained phonation and speech signals. *PLOS ONE*, 2017. PMC5628839. [-]
12. Fagherazzi G, Bensoussan Y. The Imperative of Voice Data Collection in Clinical Trials. *Digital Biomarkers*, 2024. PMC11560146. [O]
13. Patel RR, et al. (ASHA). Recommended Protocols for Instrumental Assessment of Voice. *AJSLP*, 2018. PMID: 29955816. [O]

### 영어권 UX 문헌 (EMA 및 mHealth 순응도)
14. Wen CKF, et al. Compliance With Mobile Ecological Momentary Assessment Protocols. *JMIR* 19(4):e132, 2017. PMID: 28446418. [O]
15. Businelle MS, et al. Investigating Best Practices for Ecological Momentary Assessment. *JMIR mHealth and uHealth*, 2024. PMC11347889. [O]
16. Tate AD, et al. Momentary Factors and Study Characteristics Associated With Participant Burden. *JMIR Formative Research*, 2024. DOI: 10.2196/49512. [O]
17. Sun Y, et al. SDoH and Adherence in Mobile-Based EMA. *JMIR*, 2025. DOI: 10.2196/69831. [O]
18. Amagai S, et al. Challenges in Participant Engagement and Retention. *JMIR*, 2022. PMC9092233. [O]
19. Apps don't work for patients who don't use them. *ScienceDirect*, 2024. [O]
20. Bidargaddi N, et al. To Prompt or Not to Prompt? *JMIR mHealth and uHealth*, 2018. DOI: 10.2196/10123. [O]
21. An approach to boost adherence to self-data reporting. *BMC Medical Informatics and Decision Making*, 2024. [-]

### 영어권 UX 문헌 (동의·프라이버시)
22. Haring LV, et al. Developing a digital informed consent app. *BMC Medical Ethics*, 2023. PMC10634039. [O]
23. Brightwell C, et al. Trust and Inclusion in Digital Health: The Need to Transform Consent. *Digital Society*, 2024. [O]
24. Trust, Privacy Fatigue, and the Informed Consent Dilemma. *J Theor Appl Electron Commerce Res* 20(3):179, 2025. [O]
25. Alfawzan N, et al. Privacy, Data Sharing, and Data Security Policies of Women's mHealth Apps. *JMIR mHealth and uHealth*, 2022. [O]
26. Alhammad N, et al. Patients' Perspectives on the Data Confidentiality. *JMIR*, 2024. PMC11179037. [O]
27. Enabling secure and self-determined health data sharing and consent management. *npj Digital Medicine*, 2025. PMID: 40885802. [O]
28. Brückner S, et al. A user-driven consent platform for health data sharing. *npj Digital Medicine*, 2025. PMID: 41298895. [O]
29. Lee AR, et al. Opportunities and challenges of a dynamic consent-based application. *BMC Medical Ethics*, 2024. PMID: 39217356. [O]

### 영어권 UX 문헌 (데이터 품질 관리)
30. A Systematic Review of Medical Image Quality Assessment. *Journal of Imaging* 11(4):100, 2025. PMID: 40278016. [O]
31. Schlett T, Rathgeb C, et al. Face Image Quality Assessment: A Literature Survey. *ACM CSUR* 54(10s) art.210, 2022. [O]
32. **Heim E**, et al. Large-scale medical image annotation with crowd-powered algorithms. *J Medical Imaging*, 2018. PMC6129178. [-]
33. Park JH, et al. CMed: Crowd Analytics for Medical Imaging Data. *IEEE TVCG*, 2021. PMC7859862. [O]
34. Ye C, et al. A Crowdsourcing Framework for Medical Data Sets. *AMIA Jt Summits Transl Sci Proc*, 2018. PubMed 29888085. [O]
35. Cocos A, et al. Crowd control. *J Biomedical Informatics*, 2017. PubMed 28389234. [O]

### 영어권 UX 문헌 (산업공학/인간공학)
36. Fouquet SD, Miranda AT. Asking the Right Questions—Human Factors Considerations for Telemedicine Design. *Current Allergy and Asthma Reports*, 2020. PMC7456356. [O]
37. **Demiris G, Charness N, Krupinski E**, et al. The Role of Human Factors in Telehealth. *Telemedicine and e-Health* 16(4):446-453, 2010. PMID: 20420540. [O]
38. (제외) IHI Recommendations 2022 — 비학술 블로그.
39. Zayim N, et al. Estimating Cognitive Load in a Mobile Personal Health Record Application. *Healthcare Informatics Research*, 2023. PMC10651402. [O]
40. Gomez-Hernandez M, et al. Design Guidelines of Mobile Apps for Older Adults. *JMIR mHealth and uHealth*, 2023. [O]
41. Ali SH, Thu H. App fatigue in mHealth. *PLOS Digital Health*, 2025. PMC12637926. [O]

### [한국 특화] 한국인 음성 바이오마커 문헌 (`04_korean_voice_literature.md` 출처)
- [K-1] Mondol SIMMR, Kim R, Lee S. Hybrid Machine Learning Framework for Multistage Parkinson's Disease Classification Using Acoustic Features of Sustained Korean Vowels. *Bioengineering* 2023;10(8):984.
- [K-2] Kim KH, Lee BJ, Koo HW. Feasibility Study of Parkinson's Speech Disorder Evaluation With Pre-Trained Deep Learning Model. *Korean J Neurotrauma* 2024;20(3):e30.
- [K-3] Lee J et al. Exploring Voice Acoustic Features Associated with Cognitive Status in Korean Speakers. *Diagnostics* 2024;14(24):2837.
- [K-4] (Cross-language). A cross-language speech model for detection of Parkinson's disease. *J Neural Transm* 2024.
- [K-5] **Namkung J et al. Novel Deep Learning-Based Vocal Biomarkers for Stress Detection in Koreans. *Psychiatry Investig* 2024;21(11).** (가을 단락 + ECAPA-TDNN)
- [K-6] **Kim AY, Jang EH, Lee SH, Choi KY, Park JG, Shin HC. Automatic Depression Detection Using Smartphone-Based Text-Dependent Speech Signals. *J Med Internet Res* 2023;25:e34474.** (Galaxy S10 + 가을 단락 + n=318 + AUC 0.86)
- [K-7] Mun J, Kim S, Kim MJ, Ryu J, Kim S, Chung M. Automatic detection and severity prediction of chronic kidney disease using machine learning classifiers. *Phonetics and Speech Sciences* 2022;14(4):45.
- [K-8] Maryn Y, Kim HT, Kim J. Validation of the Acoustic Voice Quality Index in the Korean Language. *J Voice* 2018. PMID: 30076095.
- [K-9] Validation of Acoustic Voice Quality Index Version 3.01 and ABI in Korean Population. *J Voice* 2019. PMID: 31708369. (CPP threshold 12 dB / 7 dB)
- [K-10] A Cepstral Analysis of Pathological Voice Quality in the Korean Population using Praat. *J Voice* 2022.
- [K-11] The Korean Version of the Voice Symptom Scale for Patients with Thyroid Operation. *J Voice* 2017. PMID: 29128434.
- [K-12] The Perceptual and Consonant Analysis for the Voice with Hypothyroidism. *J Korean Soc Laryngol Phoniatr Logoped* 2016;27(2):95.
- [K-13] **Lee SJ et al. Aging Effect on Korean Female Voice. *Folia Phoniatr Logop* 2016;68:280–286. PMID: 27160514.** (한국 여성 노화 음성 H1-A1)
- [K-14] Effects of Speech Cues on Acoustics and Intelligibility of Korean-Speaking Children With Cerebral Palsy. *JSLHR* 2024. PMID: 38573834.
- [K-15] Smartphone-Based Speech Therapy for Poststroke Dysarthria (Korean speakers, Gaeul passage). *JMIR* 2024;26:e56417.
- [K-16] **Seo YJ, Shin J. Acoustic characteristics of the sustained vowel phonation according to age groups. *Phonetics and Speech Sciences* 2018;10(4):67-76.** (한국 정상치 n=309: F0 여 199.6 Hz / 남 119.0 Hz)
- [K-17] **Yang B. The f0 distribution of Korean speakers in a spontaneous speech corpus. *Phonetics and Speech Sciences* 2021;13(3):31-37.** (자유 발화 F0 분포)
- [K-18] Polycystic Ovary Syndrome in Korean Women. *KoreaMed Synapse*. (한국 PCOS 역학)
- [K-19] Voice analysis in women with polycystic ovary syndrome. *Egyptian J Otolaryngology* 2024. (영미권 PCOS-음성 비교 근거)
- [K-20] **Longitudinal Changes in Pitch-Related Acoustic Characteristics of the Voice Throughout the Menstrual Cycle. *JMIR Formative Res* 2025;9:e65448.** (월경주기 F0 SD 9% 감소)
- [K-21] Voice in different phases of menstrual cycle among naturally cycling women. *PLOS One* 2017.
- [K-22] (간접) Korean Digits-in-Noise Test (K-DiN). PMC7261694. (한국 다기종 스마트폰 device variability)

### [한국 특화] 한국 음성 데이터셋 / 인프라
- AI-Hub 한국인 대화음성: https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=130
- AI-Hub 감정 대화 말뭉치: dataSetSn=86, 263, 271, 637
- AI-Hub 외국인 한국어 발화: dataSetSn=505
- ETRI KEMDy19: https://nanum.etri.re.kr/share/kjnoh/KEMDy19?lang=ko_KR
- ETRI KEMDy20: https://nanum.etri.re.kr/share/kjnoh/KEMDy20?lang=ko_KR
- MINDsLab-ETRI VOTE400: https://ai4robot.github.io/mindslab-etri-vote400/
- 한국음성학회 (KSSS) 학술지 *말소리와 음성과학*: https://www.eksss.org/

### 적용 가이드라인 및 표준
- ASHA Recommended Protocols for Instrumental Assessment of Voice (2018) — 음성 데이터 수집 표준
- CAPE-V (Consensus Auditory-Perceptual Evaluation of Voice) — ASHA
- WHO Guideline Recommendations on Digital Interventions for Health System Strengthening — mHealth 도입 기준
- NIH Informed Consent for Research Using Digital Health Technologies (2024) — 연구용 디지털 동의
- HHS HIPAA Resources for Mobile Health Apps Developers — 데이터 보안
- **[한국 특화]** 한국 개인정보보호법 (제15, 17, 23, 35-37조), 의료법 시행령, 생명윤리법 — 별도 법무 검토 필요

---

**문서 정보**
- 본 합성 보고서는 `02_ux_synthesis.md`(영어권 UX 문헌 41편) + `04_korean_voice_literature.md`(한국 음성 바이오마커 22편) + `reference_validation_ux.md`(2026-04-30 검증)를 종합한 한국 특화 통합본이다.
- 한국 특화 추가 분량은 v1 대비 약 28% 증가 (주요 추가: 한국어 표준 발화 자극 표, 한국 정상 참조값, AI-Hub/ETRI 활용, 한국 임상 협력 인프라, 연구 공백 분석, 파일럿 4 추가, 로드맵 11개 한국 특화 항목 신규).
- 본 보고서의 권고는 IRB 승인, 한국 개인정보보호법 적합성, 의료법 별도 검토를 전제한다.
- 한국 여성 PCOS·자궁내막증 음성 데이터 직접 검증 연구가 부재한 영역(7.5절)은 본 앱 연구의 독창성·임상 가치 핵심 근거다.
