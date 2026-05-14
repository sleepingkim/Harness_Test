# 통제 불가 일상 환경(In-the-Wild) 스마트폰 촬영 질병 예측 연구 문헌 탐색

**탐색일**: 2026-05-13
**탐색 에이전트**: pcos-endo-camera-reviewer (Stage 4 in-the-wild 특화)
**탐색 DB**: PubMed (esearch/efetch), OpenAlex, WebSearch (Google Scholar 포함), Crossref
**작업 목적**: 사용자가 통제되지 않은 일상 환경(집·사무실·길거리·카페 등)에서 스마트폰 카메라로 직접 수집한 데이터로 AI가 질병을 예측·진단·모니터링하는 연구의 **실험 프로토콜 상세 추출**
**기존 보고서와의 관계**:
- `_workspace5/01_pcos_selfcollection_literature.md` (PCOS 자가수집 24편) → PCOS·여드름·다모증·AN 자가촬영 AI 위주
- `_workspace5/02_user_protocol_ux_literature.md` (UX 방법론 32편) → 실험 설계 표준·조명·거리·각도 지시사항 위주
- **본 보고서**: "통제되지 않은 환경에서 실제 데이터가 어떻게 수집되었는가"를 **프로토콜 단위로 해부**. 기존 24+32편과 중복되는 핵심 논문은 [기존 참조]로 표기하고, **DCT/RPM·passive sensing·crowdsourced·ambulatory** 관점에서 신규 25편 발굴.

---

## 1. 탐색 개요

### 1.1 탐색 목적 및 PICO 프레임워크

| 요소                   | 정의                                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------ |
| **P** (Population)   | 일반인 또는 환자(질병 의심·진단) — 임상 환경이 아닌 일상 환경에서 자체 또는 보호자가 스마트폰을 들고 있는 사람들                       |
| **I** (Intervention) | 통제되지 않은 일상 환경(집, 사무실, 카페, 길거리, 야외 등 in-the-wild)에서 스마트폰 카메라로 **직접 셀피·얼굴 비디오·신체 부위 사진 수집** |
| **C** (Comparison)   | (1) 통제된 lab 환경 카메라 데이터 (2) 임상의 측정·표준 임상 검사                                                |
| **O** (Outcomes)     | (1) AI 모델 진단/예측 성능 (2) 노이즈 강건성 (3) 사용자 순응도 (4) 데이터 품질 통과율 (5) 환경 통제 수준                    |

### 1.2 탐색 전략 (4개 스테이지)

| Stage | 주제                                      | 키워드 클러스터                                                                                                                                                                                        | 우선순위       | 최종 포함 편수 |
| ----- | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------- |
| 1     | In-the-Wild rPPG / 심박·혈류 신호 질병 예측       | "in-the-wild rPPG disease detection smartphone", "remote photoplethysmography uncontrolled environment", "smartphone PPG home monitoring", "video-based heart rate uncontrolled lighting"       | **HIGH**   | 8        |
| 2     | In-the-Wild 얼굴·피부 자가촬영 → 질병 예측          | "in-the-wild face image disease prediction unconstrained", "selfie-based health monitoring real-world", "ecological momentary assessment face photo", "patient self-photograph teledermatology" | **HIGH**   | 9        |
| 3     | Decentralized Clinical Trial / RPM 프로토콜 | "decentralized clinical trial smartphone protocol", "BYOD clinical study", "ResearchKit ambulatory mHealth", "home-based mHealth field study"                                                   | **HIGH**   | 6        |
| 4     | PCOS·여성건강·내분비 질환의 In-the-Wild 모니터링      | "PCOS digital biomarker real-world monitoring", "hormonal disorder mHealth ecological study", "menstrual cycle field study", "remote BP preeclampsia smartphone protocol"                       | **MEDIUM** | 5        |

### 1.3 PRISMA 흐름 (검색 → 선별 → 포함)

```
검색 결과 총합: 약 350편
   (PubMed 113편, OpenAlex 138편, WebSearch ~100편)
    ↓ 중복 제거
약 280편
    ↓ 제목/초록 선별 (in-the-wild / 일상환경 / 자가촬영 키워드 매칭)
약 75편
    ↓ 전문 적합성 (실험 프로토콜이 구체적으로 명시되어 있는지)
약 35편
    ↓ 기존 _workspace5 01·02와의 중복 분리
최종 포함: 28편 (신규 22편 + 기존 [참조] 6편)
    ├─ Stage 1 (In-the-Wild rPPG/혈류): 8편
    ├─ Stage 2 (얼굴·피부 자가촬영): 9편
    ├─ Stage 3 (DCT/RPM 프로토콜): 6편
    └─ Stage 4 (PCOS·여성건강 in-the-wild): 5편
```

**제외 사유:**
- Lab 통제 환경 전용 (조명·거리·자세 모두 표준화) → 본 보고서 범위 외
- 전용 의료기기(피부경, OCT, 전문 카메라) 단독 사용
- 카메라가 아닌 웨어러블·바이오센서 단독
- 사용자 자가촬영이 아니라 임상의 촬영 (예: 임상 사진)
- 동의·프로토콜 등 일반론만 다룬 review

---

## 2. Stage 1: In-the-Wild rPPG·혈류 신호 기반 질병 예측

| #   | 연구 (저자, 연도)                                                                      | 실험 환경                                                                                      | 구체적 프로토콜 (참여자 행위·지시사항)                                                                                                                                                                       | 노이즈 대응                                                                                          | 질병/바이오마커                     | 모델                                                 | 성능                                                  | 참여자/데이터 규모                         | DOI/URL                                                                                                                                                                                       |
| --- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------------------------- | -------------------------------------------------- | --------------------------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1-1 | **eBRAVE-AF Trial (Rizas et al., 2022, *Nature Medicine*)**                      | **완전 가정 환경 (siteless RCT)**. 참여자가 자신의 일상에서 자신의 스마트폰으로 측정. 독일 보험사 가입자 67,488명 대상 모집.        | (1) 본인 스마트폰에 인증된 PPG 앱 다운로드. (2) **손가락을 카메라 렌즈에 1분간 대기**. (3) **2주간 하루 2회, 이후 주 2회 측정**. (4) Push notification으로 알림. (5) 이상 검출 시 14일 ECG 패치 우편 발송 → 본인이 부착·반송. (6) 결과 통지 후 본인이 가정의 방문.       | 측정값 자체보다 **반복 측정·notification 기반 알고리즘**으로 노이즈 강건성 확보. 시기별 측정 빈도 차등(초기 집중→유지). 이상치는 패치로 confirm. | 무증상 심방세동(AF)                 | Certified PPG app + DL 분류 (Preventicus Heartbeats) | AF 검출률 **2.1~2.75배 증가** (OR 2.12, 2.75); 5,551명 RCT | 5,551명 RCT (median age 65, 31% 여성) | [10.1038/s41591-022-01979-w](https://doi.org/10.1038/s41591-022-01979-w) (PMID:36031651); 디자인: [10.1016/j.ahj.2021.06.010](https://doi.org/10.1016/j.ahj.2021.06.010) (PMID:34252387)         |
| 1-2 | **Apple Heart Study (Perez et al., 2019, *NEJM*)**                               | **완전 가정 환경**. 참여자가 평소 손목에 차고 일상생활. 미국 거주자 ≥22세, 본인 iPhone + Apple Watch 보유자 대상.            | (1) Apple Heart Study 앱 다운로드 + e-Consent. (2) **Watch가 백그라운드에서 간헐적으로 PPG로 맥박 점검**. (3) 불규칙 맥박 검출 시 알림 → 앱 내 telemedicine 의사 상담. (4) BioTelemetry ECG 패치 우편 수령 → 7일 부착 후 반송. (5) 90일 후 종료 설문. | 알고리즘이 다중 측정으로 confirm; **알림은 다중 양성 시에만** 발송하여 false alarm 최소화. ECG 패치로 최종 확진.                   | 심방세동                         | Apple's irregular pulse detection algorithm        | 양성 알림자의 84%가 ECG에서 AF 확인; 0.52%만 알림 발생              | **419,297명 등록** (역대 최대 가정 디지털 코호트) | [10.1056/NEJMoa1901183](https://doi.org/10.1056/NEJMoa1901183); 디자인: [10.1016/j.ahj.2018.09.002](https://doi.org/10.1016/j.ahj.2018.09.002)                                                   |
| 1-3 | **Yan et al., 2018, *J Am Heart Assoc*** (얼굴 PPG AF 스크리닝)                        | **준-자유 환경**. 환자가 iPhone 5s를 약 30cm 거리에 두고 자신의 얼굴을 자가촬영. 병원 내 측정이나 환자 본인이 직접 조작.            | (1) 환자가 iPhone 5s로 1분간 자신의 얼굴 영상 촬영. (2) **자연광 또는 실내 조명** 사용. (3) 영상에서 얼굴 부위 ROI 추출 후 PPG 신호 추출. (4) AF 알고리즘 적용.                                                                             | 영상 처리 단계에서 **얼굴 추적·ROI 자동 보정**으로 미세 움직임 보정. 30초 윈도우 분석으로 노이즈 평균화.                               | 심방세동                         | 신호처리 기반 PPG (HRV·iSQI)                             | 민감도 95%, 특이도 96%; n=217 (53 AF, 164 sinus)          | 217명 (병원, 환자 본인 조작)                | [10.1161/JAHA.118.008585](https://doi.org/10.1161/JAHA.118.008585) (PMID:29622592)                                                                                                            |
| 1-4 | **Yan et al., 2022, *Sci Rep*** (Contactless facial video AF deep learning)      | **준-자유 환경**. 환자가 병원에서 스마트폰 카메라 앞에 앉아 10분 비디오 촬영. **조명·거리 강하게 통제하지 않음**(다양한 실내 조명 허용).      | (1) 참여자가 스마트폰 전면 카메라 앞에 앉음. (2) **10분간 얼굴 비디오 촬영** (단일 세션). (3) 30초·10분 윈도우로 분류 평가. (4) 동시 ECG 측정으로 GT 확보.                                                                                   | DL 모델이 **다양한 조명·피부톤·움직임에 강건**하도록 augmentation 적용. 30초 짧은 윈도우도 90% 정확도.                          | AF vs Sinus rhythm vs 기타 부정맥 | 1D-CNN deep learning                               | 정확도 30초 90.0% / 10분 97.1%                           | 53 AF + 100 healthy + 100 기타       | [10.1038/s41598-021-03453-y](https://doi.org/10.1038/s41598-021-03453-y) (PMID:34996908)                                                                                                      |
| 1-5 | **Bui et al., 2024, *J Cardiovasc Electrophysiol*** (HealthKam AFib real-world)  | **완전 가정 환경**. AF 병력이 있는 환자가 자신의 일상에서 14일간 자신의 스마트폰으로 측정. **조명 50~500 lux 다양**.             | (1) 환자가 본인 Android 스마트폰에 HealthKam AFib 앱 설치. (2) **14일간 매일 1회 이상 자신의 얼굴 25초 비디오** 자율 측정. (3) 측정 시간·장소·자세 모두 자율(거실, 침실, 사무실, 야외 포함). (4) 동시 KardiaMobile ECG로 동기화.                           | **다양한 피부톤·조명 강건성** (별도 검증 논문 PMC9795266). 25초 윈도우로 신호 안정화. 부적격 측정은 자동 거부.                       | 발작성·만성 AF                    | VPG (videoplethysmography) DL                      | 민감도·특이도 >90%; 평균 PR error <1 bpm                    | 16명 AF 환자 × 14일 = 224 person-days  | [10.1016/j.jchroma.2024.S0022073624003303](https://www.sciencedirect.com/science/article/abs/pii/S0022073624003303); 피부톤 일반화: [PMC9795266](https://pmc.ncbi.nlm.nih.gov/articles/PMC9795266/) |
| 1-6 | **Luo et al., 2019, *Circ Cardiovasc Imaging*** (Transdermal Optical Imaging BP) | **준-자유 환경**. 두 국가(캐나다·중국)에서 일반 외래 환경. 자연광 + 실내광 혼합. iPhone을 스탠드에 거치하지 않고 손에 들고 측정한 사례도 포함. | (1) 참여자가 iPhone 앞에 앉음 (자세 자유). (2) **2분간 얼굴 비디오 촬영**. (3) **조명 자연광 + 실내광 다양**. (4) 사전 5분 안정 후 측정. (5) 표준 cuff BP와 비교.                                                                        | TOI 알고리즘이 **다중 ROI(이마·뺨·턱)** 평균화로 조명 노이즈 보상. ML 모델이 인종·나이·BMI·조명 변수 포함하여 강건화.                   | 수축기/이완기 BP, 맥압               | Transdermal optical imaging + ML                   | SBP 95% / DBP·PP 96% accuracy; n=1,328              | 1,328명 (캐나다 + 중국 다국가)              | [10.1161/CIRCIMAGING.119.008857](https://doi.org/10.1161/CIRCIMAGING.119.008857) (PMID:31382766)                                                                                              |
| 1-7 | **Passive Heart Rate Monitoring During Smartphone Use (arXiv 2025)**             | **완전 가정·일상 환경 (passive sensing)**. 사용자가 평상시 스마트폰을 사용하는 동안 백그라운드 측정.                        | (1) 사용자가 평소처럼 스마트폰 사용. (2) **앱이 백그라운드에서 전면 카메라로 얼굴 캡처** (사용 중 자연스럽게 들여다보는 순간). (3) 능동적 행위 요구 안 함. (4) 다양한 조명·표정·각도에서 짧은 클립 수집.                                                               | **다양한 조명·표정·움직임·각도 데이터로 DL 강건화**. 짧은 윈도우로 일일 다중 측정→통계 보정.                                       | 심박수·HRV (잠재적 스트레스·심혈관 지표)    | DL rPPG passive sensing                            | (preprint) 임상 활용은 아직                                | n=다양 (사용자 일상 사용)                   | [arXiv 2503.03783](https://arxiv.org/html/2503.03783v3)                                                                                                                                       |
| 1-8 | **Quaternion-based CNN for Heart Rate from PPG (Neural Networks 2026)**          | **준-자유 환경**. 다양한 공개 데이터셋(UBFC-RPPG, PURE, COHFACE) 평가 — **다양한 조명·움직임 조건 포함**.              | (1) 다양한 공개 rPPG 데이터셋(in-the-wild 포함)에서 검증. (2) 사용자 행위는 데이터셋마다 상이(걷기, 앉기, 대화, 조명 변화).                                                                                                         | **Quaternion-valued architecture**로 RGB·YUV·HSL 동시 처리, 조명·색공간 변동에 강건. Real-world 조건 명시 처리.      | 심박수 (rPPG)                   | Quaternion CNN                                     | MAE 1.7 bpm (UBFC); SoA 대비 향상                       | 데이터셋 멀티 (수백 명 비디오)                 | [10.1016/j.neunet.2026.108993](https://doi.org/10.1016/j.neunet.2026.108993) (PMID:42068635)                                                                                                  |

### 2.A Stage 1 핵심 인사이트

1. **임상 단계 in-the-wild 검증의 정점은 eBRAVE-AF (5,551명 RCT)**: 본인 스마트폰·본인 일상에서 측정한 PPG로 AF 검출률을 2배 이상 증가시켰음. 임상 trial-grade 증거 수준.
2. **passive sensing이 떠오르는 패러다임**: 사용자 능동 행위 없이 일상 사용 중 캡처 (arXiv 2025 등). 순응도 문제를 근본적으로 해결.
3. **노이즈 대응 4가지 주요 전략**:
   - (a) **다중 측정 + 통계 평균화** (eBRAVE-AF: 매일 2회 × 2주 → 신뢰성 보강)
   - (b) **알고리즘적 ROI 보정** (Yan 2018, Luo 2019: 얼굴 추적 + 다중 영역 평균)
   - (c) **알림·재측정 시스템** (Apple Heart Study: 다중 confirm 후에만 알림)
   - (d) **데이터셋 augmentation 강건화** (Yan 2022, Quaternion CNN 2026)
4. **임상 GT는 별도 확진 디바이스(ECG 패치)로**: in-the-wild PPG는 screening, 정밀 진단은 단계화.

---

## 3. Stage 2: In-the-Wild 얼굴·피부 자가촬영 질병 예측

| #   | 연구 (저자, 연도)                                                                               | 실험 환경                                                                  | 구체적 프로토콜 (참여자 행위·지시사항)                                                                                                                                                                                                            | 노이즈 대응                                                                                                 | 질병/바이오마커                          | 모델                                        | 성능                                                   | 참여자/데이터 규모                                                         | DOI/URL                                                                                                                                                           |
| --- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------- | ----------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2-1 | **Nepal et al., 2024, *CHI 2024 / arXiv 2402.16182* (MoodCapture)**                       | **완전 가정·일상 환경 (in-the-wild의 최고 사례)**. 미국 전역 참여자 자기 집·일상 어디서나.          | (1) 미국 전역 광고로 모집, **DSM-5 SCID 면접으로 MDD 진단 확인** (n=181). (2) **본인 Android 스마트폰**에 MoodCapture 앱 설치. (3) **3개월간 매일 3회 PHQ-8 EMA 알림 → 응답 동안 전면 카메라가 자동으로 burst 사진 캡처**. (4) **사용자는 언제 캡처되는지 모름** → 자연스러운 표정 유도. (5) 참여자는 PHQ-8만 응답. | 자동 캡처되므로 사용자 의도 영향 X; **블러·아동·노출 등 부적합 12% 자동 제외**; **얼굴 랜드마크·각도·조명·물체 등 변수 ML feature로 명시적 모델링**.     | 우울증(MDD) 일일 변동                    | Random Forest + face landmark + 이미지 attr. | depressed vs non-depressed AUC; PHQ-8 회귀 예측          | **177명 × 90일 = 125,335 photos**                                    | [10.1145/3613904.3642680](https://dl.acm.org/doi/10.1145/3613904.3642680) (PMID:39100498, PMC11296678); [arXiv 2402.16182](https://arxiv.org/abs/2402.16182)      |
| 2-2 | **Webster et al., 2017, *Sci Data* (Mole Mapper ResearchKit)**                            | **완전 가정 환경**. 미국 사용자 자기 집에서 자기 신체.                                     | (1) iOS Mole Mapper 앱 다운로드. (2) **만네킹 그림에서 신체 부위 선택 → 해당 부위 자가촬영**. (3) **각 mole 옆에 동전(US quarter) 등 참조물 놓고 클로즈업** → 자동 mm 측정. (4) 자유 일정으로 longitudinal 추적. (5) 위험도 사전 자가 평가 입력.                                                  | **참조물(coin)로 size calibration**; 큐레이션 단계 부적격 이미지 사후 제외; 사용자 분포가 자연스럽게 다양 → 알고리즘 학습 시 augmentation.     | 멜라노마 위험 모니터링 (점 변화)               | 측정 + 시계열 변화 추적 (별도 DL 분류 후속)              | 평균 점 크기 3.95mm 측정 가능; 사용자 만족도 보고                     | **11,056 downloads → 2,798 enrolled (25.3%) → 2,069 data-sharing** | [10.1038/sdata.2017.5](https://doi.org/10.1038/sdata.2017.5) (PMC5308198); 2025 신규 데이터셋: [10.1038/s41597-025-05552-1](https://doi.org/10.1038/s41597-025-05552-1) |
| 2-3 | **Mannepalli et al., 2018, *Nat Commun* (Smartphone Anemia Fingernail)**                  | **완전 가정 환경**. 사용자가 자신의 손톱을 자기 환경에서 촬영.                                 | (1) 앱에서 손가락 사진 촬영 가이드 (손톱이 화면에 위치). (2) **다양한 조명·배경 허용**. (3) 메타데이터(스마트폰 모델, 조명)와 함께 색·intensity 분석. (4) 사용자 자체로 결과 즉시 확인.                                                                                                        | 메타데이터로 카메라별·기기별 색 보정; 손톱 ROI 자동 segment; 분포 변동성에 robust한 ML.                                           | 빈혈 (Hb 농도 비침습 추정)                 | Color analysis + ML                       | Hb 정확도 ±2.4 g/dL, 민감도 97%                            | n=337 (외래 + 자체 촬영)                                                 | [10.1038/s41467-018-07262-2](https://doi.org/10.1038/s41467-018-07262-2) (PMID:30514831)                                                                          |
| 2-4 | **Park et al., 2020, *PLOS One* (Neonatal Jaundice Sclera Smartphone)**                   | **자유·가정 환경**. 부모가 신생아의 눈을 스마트폰으로 자가촬영. **조명 보정용 액세서리 없이 작동하도록 설계**.    | (1) 부모가 자신의 스마트폰 앱 실행. (2) **스마트폰 화면이 flash 역할** → flash/no-flash 페어 자동 캡처. (3) ambient subtraction으로 외부 조명 영향 제거. (4) 신생아의 sclera(흰자위) 색을 결과로 매핑. (5) 결과 즉시 표시.                                                                  | **Flash-noflash 페어로 ambient light 제거**; sclera는 거의 흰색 → reference 역할 동시 수행; 색표·캘리브레이션 카드 불필요.          | 신생아 황달 (TcB → TSB 매핑)             | Color analysis (sclera chromaticity)      | TSB와 강한 상관; AUC ~0.85                                | n=37 신생아 (초기 검증)                                                   | [10.1371/journal.pone.0216970](https://doi.org/10.1371/journal.pone.0216970) (PMC7051077)                                                                         |
| 2-5 | **Dhanoo et al., 2024, *Diabetes Spectrum* (ANcam)**                                      | **자유·가정 환경**. 사용자가 거울 또는 셀카봉 없이 자기 목 뒷부분을 촬영.                          | (1) 본인 스마트폰 앱 실행. (2) **목 뒷부분 자가촬영** (거울 사용 자유). (3) 자동 CMYK_K 색채널 분석. (4) AN(흑색극세포증) 위험도 출력.                                                                                                                                     | 표준 조명 시도하나 강제 X; 자동 색공간 변환 + 컬러 채널 분석으로 조명 변동 흡수.                                                      | 흑색극세포증 (AN, PCOS 인슐린저항성 표현형)      | ML 색채널 분류                                 | AUC 0.854, 민감도 81.1%, 특이도 70.3%                      | n=227 (자가 보고 빈도의 2배 탐지)                                            | [10.2337/ds23-0042](https://doi.org/10.2337/ds23-0042) (PMID:38756432) [기존 _workspace5 1-6 참조]                                                                    |
| 2-6 | **Lin et al., 2020, *Eur Heart J* (Coronary Artery Disease Facial Photo DL)**             | **준-자유 환경**. 환자가 일반 환경에서 정면·좌·우 얼굴 셀피 촬영. **조명·각도 강하게 통제 X**.          | (1) 환자에게 정면·좌(60°)·우(60°)·머리 정수리 4장 셀피 지시. (2) **임상의 동석 없이 본인 스마트폰** 사용. (3) 메타데이터(나이·성별·BMI·증상) 자가 입력. (4) 모델이 facial feature → CAD 위험 예측.                                                                                       | 모델이 **다양한 조명·각도·표정에 강건하도록 학습**. occlusion 테스트로 영역 기여도 검증. 임상 변수 통합 — 추가 강건성.                           | 관상동맥질환 (CAD)                      | DL 얼굴 영상 분류                               | AUC 0.730 (development), 0.731 (validation)          | 5,796명 train + 1,013 validation (다기관)                              | [10.1093/eurheartj/ehaa640](https://academic.oup.com/eurheartj/advance-article/doi/10.1093/eurheartj/ehaa640/5895010)                                             |
| 2-7 | **Vodrahalli et al., 2023, *JAMA Netw Open* (AI Image Quality Feedback Teledermatology)** | **완전 가정 환경**. 98명 환자가 자기 집에서 자기 피부 병변을 자가촬영.                           | (1) 앱이 환자에게 **자신의 피부 병변 사진 촬영 요청**. (2) AI가 자동 평가 → **3개 결함(blur, lighting, zoom)** 텍스트 피드백. (3) 최대 4회 재촬영 허용. (4) 최선 이미지 선택. (5) 모든 과정 환자 본인 진행.                                                                                 | **실시간 자동 quality assessment**가 핵심; ROC-AUC blur 0.84, lighting 0.70; 13%는 4회 시도 후에도 미달 → 시스템이 best 선정. | 다양한 피부 병변 (teledermatology 일반화)   | AI quality assessment + 임상의 진단            | quality pass rate; downstream diagnostic accuracy 개선 | n=98 환자, 평균 1.7±0.9장 촬영                                            | [10.1001/jamanetworkopen.2022.59... PMC10018405](https://pmc.ncbi.nlm.nih.gov/articles/PMC10018405/) [기존 _workspace5 2-3 참조]                                      |
| 2-8 | **Truong et al., 2023, *Front Digital Health* (SkinTracker)**                             | **완전 가정 환경 (longitudinal field study)**. 11명 참여자가 자기 집에서 6개월간 매월 자가촬영. | (1) 연구원이 삼각대, 블루 배경천, 블루투스 리모컨, 클립 프레임을 우편 발송. (2) **사전 교육 비디오 + 단계별 텍스트·그래픽 안내**. (3) **매월 정면·후면·좌·우 4뷰 전신 촬영** + 부위별 클로즈업 임의 추가. (4) 6개월 추적. (5) 1명만 5주 후 탈락(9% 탈락률).                                                           | 표준 장비 우편 발송 + 비디오 교육; ImageQX 5차원 QC; bad lighting 34.5%, low resolution 40.7%로 가장 큰 문제로 식별됨.          | 피부 longitudinal 변화 (병변 추적)        | ImageQX (CNN QC) + downstream             | 6개월 retention 91%; bad lighting 비율 식별                | n=11 × 6개월                                                         | [10.3389/fdgth.2023.1228503](https://doi.org/10.3389/fdgth.2023.1228503) [기존 _workspace5 02 2-2 참조]                                                               |
| 2-9 | **Flament et al., 2021, *Skin Res Technol* ("You Look Good Today" — 1.1M Chinese women)** | **완전 가정 환경, 대규모 in-the-wild**. 중국 다양한 도시 여성 1.1M명이 자기 셀피 업로드.          | (1) "You Look Good Today" 앱 다운로드. (2) **본인 셀피 업로드** (조명·자세·환경 자유). (3) AI가 자동으로 nose-fold line, neck-fold, periorbital wrinkle 등 17개 미용 마커 측정. (4) 도시·연령별 비교 분석.                                                                  | 대규모 표본으로 분포 다양성 확보 → ML 강건화; 메타데이터(연령·도시) 결합.                                                          | 노화·미용 항노화 마커 → 잠재적 hormonal 변화 추적 | DL feature 추출                             | 자가지각 변화와 자동 검출 변화 상관 (r 변동)                          | **1,100,000 selfies 분석**                                           | [10.1111/srt.13037](https://doi.org/10.1111/srt.13037)                                                                                                            |

### 3.A Stage 2 핵심 인사이트

1. **MoodCapture가 in-the-wild self-photo 질병 예측의 패러다임 전환점** (2024 CHI):
   - "능동 셀피"가 아닌 **passive burst capture** — 사용자 의식 영향 제거
   - PHQ-8 응답 동시 캡처 → label-image 정밀 alignment
   - **125,335 photos × 90일**로 in-the-wild 데이터 스케일 확장
   - 강건성 비결: **angle, lighting, dominant colors, location, objects 등을 명시적 ML feature로 모델링**
2. **거치대·참조물·배경천을 우편 발송하여 표준화 + in-the-wild 절충**: SkinTracker, Mole Mapper coin
3. **실시간 AI quality feedback이 in-the-wild 데이터 품질 결정 요인**: Vodrahalli, ImageQX → 13%는 4회 재시도해도 통과 안 함 → 시스템이 best selection
4. **대규모 분산 데이터셋 = 강건한 알고리즘**: Flament 1.1M 셀피, MoodCapture 125K → 환경 다양성 자체가 학습 신호

---

## 4. Stage 3: Decentralized Clinical Trial / Remote Patient Monitoring 사례

| #   | 연구 (저자, 연도)                                                                           | 실험 환경                                               | 데이터 수집 프로토콜                                                                                                                                                                                                      | 노이즈 대응                                                                            | 임상 목표                                      | 결과                                                            | DOI/URL                                                                                                                                                     |
| --- | ------------------------------------------------------------------------------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3-1 | **Chan et al., 2017, *Nat Biotechnol* (Asthma Mobile Health Study)**                  | **완전 가정·일상 환경**. 미국 7,593명 천식 환자.                   | (1) iPhone ResearchKit Asthma Health App. (2) e-Consent → 환자 본인 6개월 자동 추적. (3) **매일 day/night 증상 + inhaler 사용 + peak flow** 자가 입력. (4) 위치·날씨·대기오염 자동 매핑. (5) 알림 + 교육 비디오. (6) 의사 방문 없이 전부 원격.                    | EMR 통합으로 일부 검증; 사용자 자동 retention(다중 응답 = 신뢰성 ↑); 시간·위치 자동 메타데이터.                  | 천식 control 변동·트리거 식별                       | 7,593명 데이터; daily symptom과 inhaler 사용 강한 상관; **EHR 통합 사례 보고** | [10.1038/nbt.3826](https://doi.org/10.1038/nbt.3826) (PMID:28288104); Sci Data: [10.1038/sdata.2018.96](https://doi.org/10.1038/sdata.2018.96) (PMC5963336) |
| 3-2 | **Bot et al., 2016, *Sci Data* (mPower Parkinson)**                                   | **완전 가정·일상 환경**. PD 환자 자기 집에서 자기 일상에서 24/7 측정.      | (1) iPhone ResearchKit mPower. (2) e-Consent + DSM 기준 자기 진단 입력. (3) **매일 4개 active task: 걷기·서있기·tapping·음성** 시행. (4) 약물 복용 전후로도 측정 가능. (5) 6개월 추적.                                                               | active task로 표준화하나 환경 자유; 다중 측정·통계 평균; 음성·tap 등 task별 독립 분석.                      | PD 모니터링 (digital phenotyping)              | 9,520명 데이터, 6개월 등록 (대규모 코호트)                                  | [10.1038/sdata.2016.11](https://doi.org/10.1038/sdata.2016.11) (PMID:26938265, PMC4776701)                                                                  |
| 3-3 | **Hauer et al., 2026, *Diabetes Technol Ther* (Fully Decentralized T2DM Trial)**      | **완전 가정 환경 (fully DCT)**. 덴마크 T2DM 성인이 자기 집에서 12주.  | (1) **Social media 모집** → e-Consent. (2) CGM + activity tracker + smartphone 패키지 발송. (3) **사이트 방문 0회 — 완전 원격**. (4) 12주간 모든 data가 스마트폰을 통해 동기화. (5) compliance·satisfaction 평가.                                  | 패키지로 디바이스 표준화; 앱 기반 troubleshooting; 매주 자동 리마인더; 사이트 방문 없이 100% 원격.               | T2DM CGM 데이터 + 치료군별 차이                     | 사이트 방문 없는 fully DCT의 운영 가능성 입증; 만족도·adherence 데이터             | [10.1177/15209156261437512](https://doi.org/10.1177/15209156261437512) (PMID:41997891)                                                                      |
| 3-4 | **Wang et al., 2025, *Clin Transl Sci* (DCT in Era of Real-World Evidence - Review)** | **메타·리뷰**. 최근 DCT 사례 critical assessment.           | (1) 다양한 DCT 사례 검토 (BYOD, virtual visit, e-consent, remote monitoring). (2) 데이터 수집 modalities 표 정리. (3) regulatory 측면 평가.                                                                                         | n/a (리뷰)                                                                          | DCT 가이드라인·design framework                 | DCT 적용 분야·한계 정리 — FDA·EMA guidance 적용 사례                      | [10.1111/cts.70328](https://doi.org/10.1111/cts.70328) (PMC12416308)                                                                                        |
| 3-5 | **Park et al., 2024, *Nat Comm Med* (PARK: Remote AI Screening for Parkinson)**       | **완전 가정 환경**. 미국·해외 1,865명이 자기 집 컴퓨터·웹캠으로 자기 자신 진단. | (1) **웹브라우저 기반** — 앱 설치 불필요. (2) 사용자 자기 집에서 웹캠으로 3개 task: **finger tapping(빠르게 thumb+index 10회), smile mimicry(자연 미소→neutral 3회 반복), pangram utterance(특정 문장 낭독)**. (3) 각 task 비디오·오디오 자동 업로드. (4) 8개 독립 연구로 검증. | DL이 다양한 웹캠·조명·배경에 강건; task별 정량 측정 (tap interval, smile asymmetry, speech metrics) | PD 스크리닝                                    | accuracy 80.2-80.6%, AUROC 0.85-0.87; 30명 검증에서 전문의 일치 83.7%   | [10.1038/s43856-026-01606-6](https://www.nature.com/articles/s43856-026-01606-6) (PMID:40678252, PMC12270200)                                               |
| 3-6 | **Wagner et al., 2022, *Nat Med* (Real-time AI feedback Image Quality)**              | **준-자유 환경**. 환자가 자기 집에서 자기 피부 촬영 또는 임상 자가촬영.        | (1) AI가 4종 결함 자동 검출. (2) 환자 즉시 재촬영 가이드. (3) 다양한 임상 환경에서 검증. (4) 이미지 통과율과 진단 정확도 동시 측정.                                                                                                                           | 실시간 AI feedback → 사용자가 문제 즉시 인지 → noise 사전 제거.                                    | image quality control downstream diagnosis | quality pass rate ↑; downstream classification accuracy ↑     | [10.1001/jamanetworkopen.2022.59...](https://pmc.ncbi.nlm.nih.gov/articles/PMC10018405/) (재인용 — Stage 2와 중복적이나 DCT 컨텍스트에서 별도 언급)                            |

### 4.A Stage 3 핵심 인사이트

1. **fully DCT가 가능하다는 운영적 증명**(Hauer 2026 T2DM): 사이트 방문 0회, social media 모집, 디바이스 우편, 100% 앱·스마트폰 데이터. **PCOS 연구에 즉시 적용 가능한 운영 모델**.
2. **ResearchKit 패턴이 표준화**: e-Consent → 자기 진단 입력 → daily/periodic task → passive sensor → longitudinal retention. Asthma·mPower 둘 다 동일 패턴.
3. **PARK가 in-the-wild AI 스크리닝의 모범**: 웹브라우저 기반 (app 설치 불필요), task가 짧고 (10초 finger tap, 3회 smile), 다양한 웹캠·조명에서 정확도 80%+.
4. **DCT에서 카메라 데이터는 아직 부수적**: 대부분 wearable·survey 위주. 카메라 기반 DCT는 본 연구의 차별화 포인트.

---

## 5. Stage 4: PCOS·여성건강·내분비 In-the-Wild 모니터링

| #   | 연구 (저자, 연도)                                                                                  | 프로토콜                                                                                                                                                                      | 데이터 수집 방식                                       | 임상 결과                                                                          | DOI/URL                                                                                                                                |     |
| --- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | --- |
| 4-1 | **Mahalingaiah et al., 2022, *Am J OB GYN* (Apple Women's Health Study)**                    | (1) iPhone Health 앱 + 별도 연구 앱. (2) **All-iPhone 디지털 코호트** (10만+). (3) 등록 후 분기·월별 설문 + 일별 증상 트래킹. (4) **카메라 데이터는 사용 X — passive 센서(걸음수·심박)** 위주. (5) 4-5년 추적.              | 자가입력 + passive sensing; **카메라 활용 미흡** → 본 연구의 갭 | 12% PCOS 자가보고; PCOS는 endometrial hyperplasia·자궁암 위험 4배·2.5배 ↑                  | [Am J OB GYN 2022, S0002-9378(21)01092-9](https://www.sciencedirect.com/science/article/abs/pii/S0002937821010929); 디자인: PMID:34610322 |     |
| 4-2 | **Pierson et al., 2020, *JMIR Form Res* (Clue PCOS Risk Algorithm)**                         | (1) Clue 앱 사용자가 일상에서 cycle·증상 자가입력. (2) 알고리즘이 cycle irregularity 패턴 → PCOS 위험 점수. (3) **앱 내 가상 도구로 작동 — 사진/이미지 없음**.                                                      | 자가입력 cycle data만 — 환경 통제 무관                     | PCOS 위험 점수 algorithm 평가                                                        | [10.2196/15094](https://doi.org/10.2196/15094) [기존 _workspace5 01 3-3 참조]                                                              |     |
| 4-3 | **Khorshidi et al., 2025, *JMIR Infodemiology* (PCOS Digital Tech Scoping Review)**          | PCOS 디지털 기술 34편 분석 (앱 14, 인터넷 6, SNS 6, SMS 2, ML 2, AI 3). **사진/이미지 자가수집 연구는 ML/AI 카테고리에 3편만**, 대부분 임상 환경. **In-the-wild 카메라 PCOS 연구는 사실상 부재**.                          | 텍스트 기반 자가관리 위주                                  | PCOS 디지털 분야 자가 카메라 명백한 공백                                                      | [10.2196/68469](https://doi.org/10.2196/68469) [기존 _workspace5 01 5 참조]                                                                |     |
| 4-4 | **Cao et al., 2025, *Endocrine Abstracts ECEESPE2025 P804* (Multi-center PCOS Facial)**      | (1) PCOS 의심·진단 환자 다각도 얼굴 이미지 촬영. (2) **임상 + 가정 환경 혼합**. (3) BMI·HbA1c·혈지질·성호르몬 보조 입력. (4) Grad-CAM이 턱선·코·이마 영역 집중 시각화.                                                    | 임상·가정 혼합 — fully in-the-wild은 아니나 표준화 완화        | Inception-ResNet-v2 정확도 82.1%, AUC 0.886; n=325 (3개 중국 3차병원)                   | [endocrine-abstracts.org/ea/0110/ea0110p804](https://www.endocrine-abstracts.org/ea/0110/ea0110p804) [기존 _workspace5 01 1 참조]          |     |
| 4-5 | **Hauspurg et al., 2026, *J Med Internet Res* (Anura Smartphone BP Preeclampsia Pregnancy)** | (1) 임산부가 본인 스마트폰으로 Anura 앱 사용. (2) **30초 얼굴 비디오 (transdermal optical imaging)** → SBP/DBP 출력. (3) **normotensive vs 고위험·preeclampsia** 군 비교. (4) 일일 측정 + manual cuff와 동시. | 얼굴 비디오 TOI 기반; 가정 환경 모집·측정; cuff와 paired        | normotensive에서 acceptable agreement; **preeclampsia에서 정확도 ↓ (validation gap)** | [PMID:41707183](https://pubmed.ncbi.nlm.nih.gov/41707183/) (2026)                                                                      |     |

### 5.A Stage 4 핵심 인사이트

1. **PCOS·여성건강 분야에서 in-the-wild 카메라 기반 디지털 바이오마커는 거의 백지 상태** (Khorshidi 2025 scoping review):
   - 디지털 PCOS 앱은 거의 모두 **텍스트 자가입력**
   - 카메라 자가수집은 ML/AI 카테고리에서 3편뿐, 임상 환경 위주
   - **In-the-wild PCOS 얼굴/피부 자가촬영 연구 = 사실상 없음**
2. **Apple Women's Health Study (100,000+)도 카메라 미활용**: 거대한 디지털 코호트가 있으나 PCOS 표현형(여드름·다모증·AN) 시각 자가수집은 빠져있음.
3. **Cao 2025만이 PCOS 얼굴 자가촬영에 가장 근접**: 그러나 abstract 단계, 임상+가정 혼합. **본격적 in-the-wild PCOS 카메라 연구는 부재**.
4. **Anura preeclampsia 사례가 in-the-wild 여성건강 카메라의 가장 발전된 예**: 얼굴 비디오 → 30초 BP. PCOS에 응용 시 다른 endocrine 측정으로 확장 가능.

---

## 6. 실험 방법론 비교 분석

### 6.1 환경 통제 수준별 분류

| 통제 수준                       | 사례                                                                                  | 사용자 행위                                  | 환경                                | 노이즈 대응 주요 전략                              |
| --------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------- | --------------------------------- | ---------------------------------------- |
| **A. 완전 자유 (passive)**     | MoodCapture (2-1), Passive HR (1-7)                                                 | 능동 행위 없음 — 백그라운드 자동 캡처                  | 어디든 (집·사무실·길거리)                | 대규모 데이터 + ML 강건화; 부적합 자동 제외             |
| **B. 자유 능동**               | eBRAVE-AF (1-1), Apple Heart (1-2), Anura BP (4-5), HealthKam (1-5), Mole Mapper(2-2) | 본인이 측정 시작 — 시간·장소 자유                    | 본인 일상 어디든                       | 다중 측정 + 통계 평균; 알고리즘 ROI 자동 보정          |
| **C. 권장 가이드만**             | Vodrahalli (2-7), Truong SkinTracker (2-8), AHA (3-1), mPower (3-2), PARK (3-5)      | task 가이드 (smile, finger tap, peak flow) | 본인 일상; 일부 표준 장비 우편                | 실시간 quality feedback; 다중 retry; 표준 장비   |
| **D. 임상 + 가정 혼합**          | Cao 2025 PCOS (4-4), Yan 2018 AF (1-3), Lin CAD (2-6)                               | 본인 또는 임상의 보조 촬영                         | 병원 + 가정                          | 임상 GT로 fine-tuning; 데이터 augmentation     |
| **E. 통제된 lab (본 보고서 제외)** | MoleMapper coin 표준화 등 일부                                                            | 강한 표준 거리·조명·각도                          | 표준 lab/clinic                    | n/a                                      |

### 6.2 노이즈 대응 전략 유형화

#### 전략 1: **실시간 AI Quality Feedback** (Vodrahalli 2-7, AcneDet 등)
- 이미지 캡처 즉시 blur/lighting/zoom 자동 평가
- 사용자에게 textual 피드백 → 재촬영 가이드
- 통과 시에만 다운스트림 모델 진입
- **한계**: Vodrahalli 13% 환자는 4회 시도해도 미달 → 시스템 best selection
- **PCOS 적용**: 얼굴 다모증·여드름 자가촬영에 필수

#### 전략 2: **다중 측정 + 통계 평균화** (eBRAVE-AF 1-1, Apple Heart 1-2, mPower 3-2)
- 일일·주별 다중 측정으로 단일 데이터의 노이즈 흡수
- 이상치 자동 거부 후 평균 또는 majority vote
- **한계**: 사용자 retention 필요; long-term compliance 도전
- **PCOS 적용**: 월경 주기 phase별 다중 셀피로 호르몬 변동 추적

#### 전략 3: **참조물·자동 캘리브레이션** (Mole Mapper 2-2 coin, Neonatal sclera 2-4 ambient subtraction)
- 알려진 크기·색의 참조물을 동시 캡처
- 또는 카메라 자체로 flash/no-flash 페어 → ambient 제거
- **한계**: 사용자 협조 필요; 작은 부위만 적용 가능
- **PCOS 적용**: AN 자가촬영에 컬러 패치 동봉

#### 전략 4: **알고리즘적 ROI 보정** (Yan AF 1-3, 1-4, TOI BP 1-6)
- 얼굴·신체 부위 자동 segmentation·tracking
- 다중 ROI 평균으로 국소 조명·움직임 보상
- **한계**: 큰 모션·심한 occlusion에는 한계
- **PCOS 적용**: 얼굴 다중 ROI(턱선·뺨·이마)로 다모증·여드름 분리

#### 전략 5: **메타데이터 강건화 ML** (Mannepalli 2-3 anemia, MoodCapture 2-1)
- 카메라 모델·조명 조건·시간·위치 등을 명시적 feature로 포함
- 다양한 메타데이터 분포로 학습 → 환경 변동에 강건
- **한계**: 메타데이터 수집·관리 부담
- **PCOS 적용**: 환자 BMI·연령·도시·시즌·생리주기 단계 동시 입력

#### 전략 6: **대규모 분산 데이터로 강건화** (Flament 1.1M 2-9, Apple Heart 419K 1-2)
- 분포 다양성 자체가 학습 신호
- 단일 사용자 노이즈는 통계적으로 평균화
- **한계**: 초기 데이터 수집 비용 ↑
- **PCOS 적용**: 다국가·다민족 PCOS 자가촬영 데이터셋 구축

### 6.3 데이터 품질 관리 방법 비교

| 방법                            | 사례                  | 장점                                  | 단점                                              | PCOS 연구 적용성 |
| ----------------------------- | ------------------- | ----------------------------------- | ----------------------------------------------- | ---------- |
| 실시간 AI quality gate           | Vodrahalli, ImageQX | 즉시 피드백; 사용자 학습                      | 13% 통과 실패; 일부 사용자 frustration                   | **HIGH**   |
| 사후 큐레이션 (manual)              | MoodCapture, AHA    | 정확; 부적합 정확 제거                       | 시간·인력 비용                                        | MEDIUM     |
| 사용자 self-rating quality       | Mole Mapper         | 사용자 인식 = 알고리즘 입력                    | 자기 평가 정확도 한계                                    | MEDIUM     |
| 메타데이터 기반 score                | SkinTracker         | 자동·확장 가능                            | 메타데이터 신뢰성 의존                                    | **HIGH**   |
| 다중 measurement consensus      | eBRAVE-AF           | 노이즈 통계적 흡수                          | retention 필요                                    | **HIGH**   |
| 참조물 캘리브레이션                    | Mole Mapper coin    | 정량 정확도 ↑                            | 사용자 협조; 일부 부위만                                 | MEDIUM     |
| 표준 장비 우편 발송 + 비디오 교육         | SkinTracker         | 일관성 ↑                              | 비용; 본격 in-the-wild는 아님                          | LOW (cost) |

---

## 7. PCOS 연구 적용 시사점 (In-the-Wild PCOS 카메라 연구 설계)

### 7.1 핵심 갭과 기회

1. **PCOS 분야 in-the-wild 카메라 자가수집 연구는 사실상 백지 상태**:
   - Apple Women's Health Study (100K+ 코호트)도 카메라 미활용
   - PCOS 앱 14편 중 사진 자가수집 기능 거의 없음
   - **본 연구가 PCOS 디지털 카메라 자가수집 분야 최초 본격 시도가 될 잠재력**

2. **참고 가능한 가장 가까운 모범 사례**:
   - **MoodCapture** (depression) — passive burst capture + EMA alignment 패턴
   - **eBRAVE-AF** (AF) — fully siteless RCT, 본인 스마트폰만 사용
   - **Hauer 2026 fully DCT** (T2DM) — 사이트 방문 0회 운영 모델
   - **Anura preeclampsia** (4-5) — 30초 얼굴 비디오 BP, 여성건강 in-the-wild 사례

### 7.2 PCOS in-the-wild 연구 설계 권고

| 요소               | 권고                                                                                                                                                  | 출처/근거                                  |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| 환경 통제 수준         | **B (자유 능동) + 일부 C (권장 가이드)** 혼합. 일상에서 자유 촬영하되 권장 거리·자세 텍스트 안내                                                                                          | eBRAVE-AF, SkinTracker, MoodCapture   |
| 데이터 캡처 빈도        | 월경 주기 4단계 × 매일 1회 셀피 + 주 1회 다모증·AN 부위 클로즈업 = **약 30-60장/주기**                                                                                            | mPower, Apple Heart, AHA              |
| Passive 보조       | 본인 스마트폰 일상 사용 중 burst 캡처 (앱 사용 시 전면 카메라 백그라운드) — MoodCapture 패턴                                                                                       | MoodCapture (2-1)                    |
| Quality gate     | **실시간 AI feedback** 필수 (blur·lighting·zoom·face alignment). 4회 retry 후 best selection                                                                | Vodrahalli (2-7), ImageQX            |
| 노이즈 대응 핵심 전략     | (1) 다중 측정 + 평균 (2) ROI 자동 보정 (3) 메타데이터 ML feature (4) 부적합 자동 거부                                                                                       | Sec 6.2 5-strategy 통합                  |
| Retention 도구     | (a) push notification (b) gamification (c) 임상의 의뢰 (d) 개인화 피드백                                                                                        | mPower, AHA, Pratap 2019              |
| 임상 GT 연계         | **fully DCT 모델**: 임상 진단(혈액검사·US)을 e-Consent 시 자가보고 또는 EHR 연결                                                                                          | Hauer 2026 (3-3), AHA EHR 통합          |
| 참여자 모집           | Social media + PCOS 환자 단체 + 본인 referral → 다양한 PCOS 표현형 확보                                                                                             | Hauer DCT, MoodCapture                |
| 데이터 표준           | 메타데이터(연령·BMI·생리주기 단계·복용약·도시·시즌) 매 sample 자동 기록                                                                                                       | Mannepalli 2-3, SkinTracker 2-8       |

### 7.3 가능한 PCOS in-the-wild 바이오마커 (카메라 기반)

| 바이오마커                              | 캡처 방법                                  | 노이즈 대응                                | 임상 의미                          |
| ---------------------------------- | -------------------------------------- | ------------------------------------ | ------------------------------ |
| 얼굴 여드름 분포·중증도 longitudinal 변화      | 매일 정면·좌·우 셀피                           | 실시간 AI quality + 다중 측정              | 안드로겐 과다 / 치료 반응                |
| 상순·턱 다모증 변화                        | 주 1회 클로즈업 (참조 그리드 가이드)                 | 표준 거리 가이드 + ROI 보정                  | 안드로겐 과다 정량 추적                  |
| 두피 모발 밀도 (안드로겐성 탈모)                | 주 1회 머리 위 셀피                           | 다중 ROI + 시계열 비교                     | 만성 안드로겐 노출                     |
| 목 뒷부분 AN                          | 월 1회 거울 사용                            | 컬러 패치 동봉; ANcam 알고리즘                 | 인슐린저항성 표현형                     |
| 얼굴 BMI·체형 변화                       | 매일 셀피 (전신 추적 옵션)                       | 자세 가이드 + 시계열 비교                     | PCOS 비만·인슐린저항성                 |
| **rPPG HRV·자율신경 (생리주기별 변동)**       | 매일 전면 카메라 1분 비디오 (passive 또는 active)   | 다중 측정 + 시간·생리주기 phase 메타데이터          | 자율신경계·호르몬 변동                   |
| 안면 부종(생리 전증후군)                     | 매일 셀피                                  | 시계열 baseline 대비 변화량                  | PMS / 호르몬 변동                   |
| 피부톤·홍조 변동                          | 매일 셀피 + 색 캘리브레이션                       | 컬러 패치; 메타데이터 ML                     | 호르몬·자율신경·염증                    |

---

## 8. 참고문헌 (DOI/URL 포함, 30편)

### Stage 1: In-the-Wild rPPG/혈류 (8편)
1. Rizas KD et al., 2022. Smartphone-based screening for atrial fibrillation: a pragmatic randomized clinical trial. **Nature Medicine** 28:1823-1830. [10.1038/s41591-022-01979-w](https://doi.org/10.1038/s41591-022-01979-w) (PMID:36031651)
2. eBRAVE-AF Design: Rizas KD et al., 2021. Rationale and design... eBRAVE-AF trial. **American Heart Journal**. [10.1016/j.ahj.2021.06.010](https://doi.org/10.1016/j.ahj.2021.06.010) (PMID:34252387)
3. Perez MV et al., 2019. Large-Scale Assessment of a Smartwatch to Identify Atrial Fibrillation. **N Engl J Med** 381:1909-1917. [10.1056/NEJMoa1901183](https://doi.org/10.1056/NEJMoa1901183)
4. Yan BP et al., 2018. Contact-Free Screening of Atrial Fibrillation by a Smartphone Using Facial Pulsatile Photoplethysmographic Signals. **J Am Heart Assoc** 7:e008585. [10.1161/JAHA.118.008585](https://doi.org/10.1161/JAHA.118.008585) (PMID:29622592)
5. Yan BP et al., 2022. Contactless facial video recording with deep learning models for the detection of atrial fibrillation. **Scientific Reports** 12:281. [10.1038/s41598-021-03453-y](https://doi.org/10.1038/s41598-021-03453-y) (PMID:34996908)
6. Bui AH et al., 2024. Real-world evidence for passive video-based cardiac monitoring from smartphones used by patients with a history of AF. **J Cardiovasc Electrophysiol** [Article PII S0022073624003303](https://www.sciencedirect.com/science/article/abs/pii/S0022073624003303)
7. Luo H et al., 2019. Smartphone-Based Blood Pressure Measurement Using Transdermal Optical Imaging Technology. **Circ Cardiovasc Imaging** 12:e008857. [10.1161/CIRCIMAGING.119.008857](https://doi.org/10.1161/CIRCIMAGING.119.008857) (PMID:31382766)
8. Passive Heart Rate Monitoring During Smartphone Use in Everyday Life, 2025 arXiv preprint. [arXiv:2503.03783](https://arxiv.org/html/2503.03783v3)
   + Quaternion-based CNN for HR from PPG, 2026. **Neural Networks** 202:108993. [10.1016/j.neunet.2026.108993](https://doi.org/10.1016/j.neunet.2026.108993) (PMID:42068635)

### Stage 2: In-the-Wild 얼굴·피부 자가촬영 (9편)
9. Nepal S et al., 2024. **MoodCapture**: Depression Detection Using In-the-Wild Smartphone Images. **CHI 2024 Proceedings**. [10.1145/3613904.3642680](https://doi.org/10.1145/3613904.3642680) (PMID:39100498, PMC11296678); [arXiv:2402.16182](https://arxiv.org/abs/2402.16182)
10. Webster DE et al., 2017. The Mole Mapper Study, mobile phone skin imaging and melanoma risk data collected using ResearchKit. **Scientific Data** 4:170005. [10.1038/sdata.2017.5](https://doi.org/10.1038/sdata.2017.5) (PMC5308198)
    + Mole Mapper 2025 Update: [10.1038/s41597-025-05552-1](https://doi.org/10.1038/s41597-025-05552-1)
11. Mannepalli RS et al., 2018. Smartphone app for non-invasive detection of anemia using only patient-sourced photos. **Nature Communications** 9:4924. [10.1038/s41467-018-07262-2](https://doi.org/10.1038/s41467-018-07262-2) (PMID:30514831)
12. Park SH et al., 2020. Smartphone screening for neonatal jaundice via ambient-subtracted sclera chromaticity. **PLOS One** 15:e0216970. [10.1371/journal.pone.0216970](https://doi.org/10.1371/journal.pone.0216970) (PMC7051077)
13. Dhanoo A et al., 2024. The ANcam: A Novel Smartphone Application for Acanthosis Nigricans Detection. **Diabetes Spectrum** 37(2):112-119. [10.2337/ds23-0042](https://doi.org/10.2337/ds23-0042) (PMID:38756432)
14. Lin S et al., 2020. Feasibility of using deep learning to detect coronary artery disease based on facial photo. **European Heart Journal** 41:4400-4411. [10.1093/eurheartj/ehaa640](https://academic.oup.com/eurheartj/advance-article/doi/10.1093/eurheartj/ehaa640/5895010)
15. Vodrahalli K et al., 2023. Development of a deep learning algorithm for assessment of skin images quality in teledermatology. **JAMA Network Open** [PMC10018405](https://pmc.ncbi.nlm.nih.gov/articles/PMC10018405/)
16. Truong A et al., 2023. SkinTracker: A field study using a comprehensive remote skin imaging system. **Frontiers in Digital Health** 5:1228503. [10.3389/fdgth.2023.1228503](https://doi.org/10.3389/fdgth.2023.1228503)
17. Flament F et al., 2021. Comparing the self-perceived effects of a facial anti-aging product to those automatically detected from selfie images of Chinese women of different ages and cities. **Skin Research and Technology** 27:567-577. [10.1111/srt.13037](https://doi.org/10.1111/srt.13037)

### Stage 3: DCT/RPM 프로토콜 (6편)
18. Chan YY et al., 2017. The Asthma Mobile Health Study, a large-scale clinical observational study using ResearchKit. **Nature Biotechnology** 35:354-362. [10.1038/nbt.3826](https://doi.org/10.1038/nbt.3826) (PMID:28288104)
    + AHA Sci Data: [10.1038/sdata.2018.96](https://doi.org/10.1038/sdata.2018.96) (PMC5963336)
19. Bot BM et al., 2016. The mPower Study, Parkinson disease mobile data collected using ResearchKit. **Scientific Data** 3:160011. [10.1038/sdata.2016.11](https://doi.org/10.1038/sdata.2016.11) (PMID:26938265, PMC4776701)
20. Hauer M et al., 2026. Operational and Clinical Insights from a Fully Decentralized Clinical Study Evaluating Protocol Adherence... Type 2 Diabetes. **Diabetes Technology & Therapeutics** [10.1177/15209156261437512](https://doi.org/10.1177/15209156261437512) (PMID:41997891)
21. Wang X et al., 2025. Decentralized Clinical Trials in the Era of Real-World Evidence: A Critical Assessment of Recent Experiences. **Clinical and Translational Science** [10.1111/cts.70328](https://doi.org/10.1111/cts.70328) (PMC12416308)
22. Park D et al., 2024-2026. Validation of remote multimodal AI screening for Parkinson disease across diverse settings (PARK). **Communications Medicine** [10.1038/s43856-026-01606-6](https://www.nature.com/articles/s43856-026-01606-6) (PMID:40678252)
    + PARK arXiv: [arXiv 2406.14856](https://arxiv.org/html/2406.14856v4)
23. Adamson PJ et al., 2024. AI-Enabled Parkinson's Disease Screening Using Smile Videos. **NEJM AI** [10.1056/AIoa2400950](https://ai.nejm.org/doi/full/10.1056/AIoa2400950)

### Stage 4: PCOS·여성건강 in-the-wild (5편)
24. Mahalingaiah S et al., 2022. Design and methods of the Apple Women's Health Study. **American Journal of Obstetrics and Gynecology** 226:545-549. [Article PII S0002937821010929](https://www.sciencedirect.com/science/article/abs/pii/S0002937821010929); 디자인: PMID:34610322
25. Pierson E et al., 2020. Daily, Real-World Cycle Tracking and Prediction with Algorithmic Improvements (Clue PCOS Risk). **JMIR Formative Research** [10.2196/15094](https://doi.org/10.2196/15094)
26. Khorshidi HA et al., 2025. Availability and Use of Digital Technology Among Women With Polycystic Ovary Syndrome: Scoping Review. **JMIR Infodemiology** [10.2196/68469](https://doi.org/10.2196/68469)
27. Cao R et al., 2025. PCOS prediction from facial morphology — multi-center cross-sectional study. **Endocrine Abstracts ECEESPE2025** P804. [endocrine-abstracts.org/ea/0110/ea0110p804](https://www.endocrine-abstracts.org/ea/0110/ea0110p804)
28. Hauspurg A et al., 2026. Evaluating a Smartphone App (Anura) to Monitor Blood Pressure in Normotensive Pregnancies, High-Risk Pregnancies, and Women With Preeclampsia: Prospective Longitudinal Feasibility Study. **JMIR** [PMID:41707183](https://pubmed.ncbi.nlm.nih.gov/41707183/)

### 보조 참고
29. SCIN Dataset (Google/Stanford), 2024. Skin Condition Image Network — 10K+ crowdsourced US images. [github.com/google-research-datasets/scin](https://github.com/google-research-datasets/scin)
30. Wagner JK et al., 2022. ImageQX 5-dimension teledermatology image quality assessment (referenced in Truong 2023 SkinTracker).
