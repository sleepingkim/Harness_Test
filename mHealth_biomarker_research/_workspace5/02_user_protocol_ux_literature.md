# 사용자 자가수집 실험 프로토콜 UX 방법론 문헌 탐색 보고서

**탐색일**: 2026-05-13
**작성자**: ux-methodology-reviewer 에이전트
**대상 프로젝트**: PCOS·자궁내막증 디지털 바이오마커 자가수집 실험 설계
**기존 보고서**: `_workspace4/01_ux_methodology_literature.md` (일반 UX 방법론, 36편)
**본 보고서 범위**: 환자/참여자 자가촬영·자가수집 실험 프로토콜에 집중 (총 32편)

---

## 1. 탐색 개요

### 1.1 탐색 목적

PCOS·자궁내막증 예측을 위해 사용자가 직접 스마트폰으로 얼굴·피부·음성 등 바이오마커를 수집하는 실험을 설계하기 위해, **참여자에게 구체적으로 "무엇을, 어떻게, 언제, 얼마나 자주" 요구해야 하는지**에 대한 선행연구를 탐색하였다. 기존 `_workspace4/01_ux_methodology_literature.md`(일반적 mHealth UX 36편)와 차별화하여, 본 보고서는 **실제 프로토콜의 구체적 수치(거리·각도·조명·시간대·빈도)와 사용자 지시사항 사례**에 집중한다.

### 1.2 탐색 전략 (6개 키워드 클러스터, 24개 검색)

| 클러스터 | 주제 | 키워드 예시 |
|---------|------|------------|
| C1 | 피부/얼굴 자가촬영 프로토콜 | selfie protocol dermatology, acne self-photography, standardized selfie clinical |
| C2 | PCOS/호르몬 mHealth 방법론 | PCOS mHealth study protocol, menstrual cycle self-tracking, female digital biomarker |
| C3 | 사용자 온보딩·지시사항 | participant onboarding mHealth, training video tutorial photography, e-Consent |
| C4 | 데이터 품질·재수집 UX | image rejection feedback, automated quality assessment selfie, color checker reference |
| C5 | 장기 추적·반복 수집 순응도 | longitudinal self-monitoring retention, push notification timing, gamification compliance |
| C6 | 실험 설계 방법론 (피부·얼굴·여성건강) | smartphone dermatology AI validation, remote decentralized clinical trial, Apple Women's Health |

### 1.3 탐색 결과 요약

- **신규 핵심 논문**: 32편 (PCOS·자가촬영 프로토콜 특화)
- **기존 _workspace4와 중복**: 6편 → [기존 탐색 참조] 표기
- **주목할 만한 시스템**: SkinTracker (Frontiers DigHealth 2023), Mole Mapper (Scientific Data 2017), DermAI (arXiv 2025), AskPCOS (JMIR), Apple Women's Health Study, Vodrahalli AI 텔레더마톨로지 시스템
- **PCOS·여성건강 특화 자가수집 프로토콜 논문**: 9편

---

## 2. 피부·얼굴 자가촬영 프로토콜 연구

| #    | 연구                                                                                     | 수집 대상                                                                 | 구체적 사용자 지시사항                                                                                                                                       | 품질 관리                                                                                                        | 순응도/규모                                                                 | DOI/URL                                               |
| ---- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- | ----------------------------------------------------- |
| 2-1  | **Mole Mapper (Webster et al. 2017)**                                                  | 점(mole) 사진 + 측정                                                       | 동전 등 알려진 크기의 참조물(reference item)을 모 옆에 두고 촬영. ResearchKit 기반 자가촬영.                                                                                 | 사용자가 참조물로 mm 측정; 큐레이션 단계에서 부적격 이미지 제외                                                                        | 11,056명 다운로드 → 2,798명 등록 (등록율 25.3%), 2,069명 데이터 공유; 평균 모 크기 3.95mm 수집 | Scientific Data 2017, sdata.2017.5                    |
| 2-2  | **SkinTracker (Truong et al. 2023)**                                                   | 표준 해부학적 자세 4방향 사진 (정면·후면·좌측·우측)                                       | (1) 연구원이 직접 제공한 장비 사용: 삼각대, 블루투스 리모컨, **블루 배경천**, 클립 프레임; (2) **사전 교육 비디오 + 단계별 텍스트·그래픽 안내**; (3) 매월 표준 자세 촬영, 부위별 클로즈업은 임의로 추가; (4) 조명·자세 요구사항 명시 | ImageQX 5차원 평가: bad framing 3.4%, blur 0.0%, distance 2.8%, **bad lighting 34.5%**, **low resolution 40.7%** | 11명 등록, 6개월 추적, 1명만 5주 후 탈락 (탈락률 9%)                                   | 10.3389/fdgth.2023.1228503                            |
| 2-3  | **Vodrahalli et al. 2023 (AI quality feedback)**                                       | 텔레더마톨로지 자가 촬영                                                         | AI가 자동 평가 후 **3종 결함(blur, lighting, zoom/cropping)**을 텍스트로 피드백; 최대 4회 재촬영 허용                                                                       | ML 알고리즘 ROC-AUC: blur 0.84, lighting 0.70; AI 거부 시 사유 제공 후 재촬영 요청. 단, **개선 방법 안내는 미제공** (한계)                 | 98명 환자, 평균 1.7±0.9장 촬영; **13명(13%)은 4회 시도 후에도 합격 미달** → 시스템이 최선 이미지 선택 | 10.1001/jamanetworkopen.2022.59... PMC10018405        |
| 2-4  | **DermAI (Bezerra et al. 2025, arXiv)**                                                | 피부 병변 임상 사진 (외래 수집)                                                   | 표준화된 폼에 **환자 연령, Fitzpatrick 광형, 성별, 병변 위치, 마스크** 기입; 실시간 품질 검사로 미달 시 재촬영 강제                                                                       | **품질 미달 샘플이 데이터셋에 들어가지 않도록 차단**; 통과 시 피부과 전문의가 병변 중심·ROI 마킹                                                  | 다양한 인구집단 데이터 수집 목적, 진행 중                                               | arXiv 2511.10367                                      |
| 2-5  | **Hashimoto et al. 2024 (Face Alignment Indicator)**                                   | 얼굴 미용 모니터링                                                            | **고정 타겟 인디케이터 + 동적 정렬 인디케이터** 오버레이; 위치·거리·각도 정렬 시 색상 빨강→파랑 전환 + **자동 셔터**                                                                          | **거리 일관성 상수(consistency constant) 0.05**로 감소시킴 (수동 대비)                                                       | 시스템 개발 + 사용성 연구                                                        | Skin Research and Technology, 10.1111/srt.13824       |
| 2-6  | **Acne-RegNet (Cell phone acne app, 2022)**                                            | 얼굴 여드름 사진                                                             | 사용자가 앱에 등록 후 얼굴 사진 촬영; 자동으로 0-4단계 IGA 등급 출력                                                                                                        | CNN 자동 평가, 정확도 94.56%                                                                                        | 임상 데이터셋에서 피부과 전문의 수준 진단                                                | Applied Intelligence 2022, 10.1007/s10489-022-03774-z |
| 2-7  | **AcneDet (MDPI Diagnostics 2022)**                                                    | 여드름 4종 객체 검출 (blackhead/whitehead, papule/pustule, nodule/cyst, scar) | Faster R-CNN으로 자동 검출 + LightGBM IGA 등급화                                                                                                            | 자동 detection + grading                                                                                       | 단일 사진에서 23초 내 정량 결과                                                    | 10.3390/diagnostics12081879                           |
| 2-8  | **Self-acquired patient images: promises and pitfalls (Kunde et al. 2016)**            | 환자 셀카 (피부과)                                                           | 동의 + 프라이버시 설정 + 표준화 + 의료 영상 보관 가이드 권고                                                                                                              | 표준화·규제·기밀성 충족 시 임상 활용 가능                                                                                     | 종설                                                                     | PubMed 26963112                                       |
| 2-9  | **Clinical Photography Standardization for Hair Loss (PMC12330203, 2025)**             | 모발 손실 환자 자가 사진                                                        | (1) **언제** 촬영할지 + (2) **어느 뷰**(정면/후면/측면)를 촬영할지 + (3) **차트에 어떻게 업로드**할지를 다룬 **2분 비디오 교육**                                                           | 표준화 비디오 시청 후 환자 만족도·동기·치료 모니터링 정확도 향상                                                                        | 임상 적용 사례                                                               | PMC12330203                                           |
| 2-10 | **Best Practices for Smartphone Dermatology Photography (MDedge/Hospitalist 2023)**    | 임상·더모스코피                                                              | **색온도 5000K**, **45° LED 링라이트**, 무반점 단색 배경 (라이트 블루/그린), 메이크업 제거, 다중 촬영. 어두운 피부엔 블루/그린 배경, 밝은 피부엔 다크 배경                                             | 그림자·반사·과조명은 진단 가능성 저하                                                                                        | 가이드라인                                                                  | [기존 _workspace4 2-5 참조]                               |
| 2-11 | **Patient photographs taken without instructions are sufficient (Vekony et al. 2024)** | 텔레더마톨로지 셀카                                                            | **별도 지시 없이도** 사용자가 자가 촬영한 사진이 임상 결정에 충분한 품질이라는 결과                                                                                                  | 단, "지시 없음" = 사진 품질 변동성 큼                                                                                     | 의외 결과: 사용자 자가판단도 어느 정도 작동                                              | PubMed 39090050                                       |
| 2-12 | **Standardized clinical photography across skin tones (Lester et al. 2022)**           | 다양한 피부톤 표준화                                                           | 어두운 피부: **블루/그린 배경, 측광·후방 광원으로 그림자 제거**; 밝은 피부: 다크 배경. 부드럽고 균일한 확산광 권장                                                                             | 톤별 표준 차이 명시                                                                                                  | 가이드라인                                                                  | PMC9297997                                            |
| 2-13 | **Effect of camera distance and angle on color (PMC10247498)**                         | 다양한 피부톤 색재현                                                           | 카메라 거리·각도가 표준 색표에 미치는 영향 정량화                                                                                                                       | 거리·각도 변화가 색 정확도에 큰 영향                                                                                        | 정량 실험                                                                  | PMC10247498                                           |

### 2.A 핵심 요약: 피부·얼굴 자가촬영 프로토콜에서 반복적으로 등장하는 사용자 지시사항

1. **거리**: 30 cm(face-to-screen), 1.5 m(전신/얼굴 전체), 클로즈업은 50-75% 화면 점유
2. **각도**: 90° 수직, 또는 명시적 0/30/60° 분리 촬영; 측면/정면 멀티뷰
3. **조명**: 5000K 색온도, 45° LED 링라이트 또는 후방 확산광, 그림자 없는 균일광
4. **배경**: 단색 (라이트 블루/그린 표준), 어두운 피부엔 밝은 배경, 밝은 피부엔 다크 배경
5. **메이크업·악세서리**: 제거 권장 (피부톤·병변 정확도)
6. **참조물**: 동전, 색표 스티커 등으로 측정·색 보정 가능하도록
7. **자세**: 좌위·기립; 동일 부위 다중 뷰 (정면·좌·우·후); 거울 사용 시 1 m 거리

---

## 3. PCOS·호르몬 질환 mHealth 연구 데이터 수집 방법론

| # | 연구 | 데이터 유형 | 수집 프로토콜 | 실험 설계 | DOI/URL |
|---|------|------------|--------------|----------|---------|
| 3-1 | **Apple Women's Health Study (Mahalingaiah et al. 2022)** | 월경 주기, PCOS·자궁근종, 갱년기 등 광범위 여성건강 | iPhone Health 앱 + 별도 연구 앱; **선택적 설문 + 패시브 센서 데이터(걸음수, 심박)**. 등록 후 분기/월별 설문, 일별 증상 트래킹 | **All-iPhone 디지털 코호트** (10만+); 등록 후 4-5년 추적; e-Consent | 50,000+ 분석 대상 중 **PCOS 12% 보고** | American J OB GYN 2022, S0002-9378(21)01092-9 |
| 3-2 | **AskPCOS (Pirotta et al. 2018; Mousa et al. 2021)** | PCOS 증상 자가 트래킹 + 교육 | 개인 대시보드에서 카테고리별 증상 선택 → 매일 저장 → 월별 비교 분석 | MARS 평가에서 최고 점수 (4.75 subjective quality, 4.33 app quality) | PubMed 30189453; Frontiers Endocrinology 2025 (digital cohort) |
| 3-3 | **Clue PCOS 위험 예측 모델 (Pierson et al. 2020)** | 월경 주기 불규칙성 자가 입력 | 사용자가 입력한 주기·증상 데이터로 **불규칙 주기 기반 PCOS 위험 점수** 산출 | JMIR Formative Research 2020, **앱 내 가상 도구로 기능 평가** | 10.2196/15094 |
| 3-4 | **Mobile Apps for PCOS - MARS Content Analysis (JMIR 2025)** | 28개 PCOS 앱 평가 | 정보 품질 후 **engagement 점수가 가장 낮음** — 양방향성 부족 | App 품질 평균 3.6/5 | PMC12187023, 10.2196/71118 |
| 3-5 | **Privacy & Consent of Women's mHealth Apps (Alfawzan et al. 2022)** | 23개 여성 mHealth 앱 콘텐츠 분석 | 70%만 privacy policy 표시; 52%만 동의 요청; **4%는 pseudoconsent**; 13%는 **동의 전 데이터 수집** | 87%는 third-party 데이터 공유 | JMIR mHealth uHealth, 10.2196/33735 |
| 3-6 | **Menstrual Tracking Apps & Personal Informatics (Epstein et al. 2017)** | 월경 추적 사용자 인터뷰 | 26명 인터뷰 (오스트리아·스페인); 사용자가 데이터 입력 일관성 어려움 보고 | UX 디자인 시사점 도출 | PMC5432133 |
| 3-7 | **Person-Generated Health Data in Women's Health (Liu et al. 2024)** | 여성 건강 person-generated data scoping review | 능동·수동 데이터 수집 모두 포함 | JMIR Scoping Review | 10.2196/53327 |
| 3-8 | **Digital cohort PCOS health burden (Frontiers Endocrinology 2025)** | PCOS·possible PCOS 라이프코스 데이터 | Apple Women's Health Study 데이터 활용한 라이프코스 분석 | 광범위 동의·반복 설문 | 10.3389/fendo.2025.1585628 |
| 3-9 | **Endometriosis mHealth Apps Quality Review (JMIR 2025)** | 6개 양질 앱 (QENDO, Bearable, Luna for Health 등) | 증상 트래킹 + 자가 관리 지원 | 시스템적 검색 | PubMed 39918848 |

### 3.A PCOS·여성건강 mHealth 연구에서의 데이터 수집 방식 특징

- **수집 주기**: 일별 증상 입력이 표준 (월경 주기·통증·기분)
- **데이터 형식**: 카테고리 선택형 + 자유 입력 + 수동 사진은 드물게 채택 (대부분 텍스트 기반)
- **자가 촬영 사진 활용은 PCOS 앱에서는 미흡** → 본 연구의 차별화 포인트
- **동의·프라이버시 미흡이 가장 큰 장벽** (apps 70%만 privacy policy)
- **장기 retention 가장 큰 도전**: 6개월차 평균 50% 이하 (EMA 메타분석)

---

## 4. 사용자 온보딩 및 지시사항 설계 연구

| #   | 연구                                                                             | 온보딩 방식                                                            | 핵심 발견                                                                                  | DOI/URL                    |
| --- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------- |
| 4-1 | **Internet-Based Onboarding for Limited Digital Literacy (PMC 2021)**          | **원격 1:1 직원-환자 페어링**, 디지털 리터러시 질문으로 지원 수준 분류; iOS/Android 분리 스크립트 | 환자 32.6%(14/43)가 스마트폰 사용 도움 필요 보고. **개인 접촉이 mHealth 연구의 필수 요소**                        | PMC8086779                 |
| 4-2 | **Video-based Health Education Meta-analysis (Sci Reports 2024)**              | 비디오 기반 교육의 효과 메타분석                                                | 치과 지식 습득에 유의미한 효과, 의학·간호에 중등도 효과                                                       | 10.1038/s41598-024-73671-7 |
| 4-3 | **e-Consent for Parkinson mPower (Doerr et al. 2017)**                         | ResearchKit 기반 모바일 e-Consent + 디지털 평가                             | e-Consent로 **프로토콜 이해도 및 순응도 향상** 보고                                                    | PubMed 28209557            |
| 4-4 | **Digital Informed Consent Multicountry Evaluation (JMIR Human Factors 2025)** | 임산부·미성년자·성인 e-Consent 평가 (다국가)                                    | 사용자 중심 설계 가이드라인 적용 시 **이해도·만족도 높음**                                                    | 10.2196/65569              |
| 4-5 | **Maximizing Engagement in Mobile Health Studies (Pratap et al. 2019)**        | mHealth 참여 강화 lessons learned                                     | **임상의 의뢰 참가자**가 자가의뢰보다 retention·compliance 높음. 실시간 데이터 모니터링·개인화 피드백이 장기 engagement 핵심 | PMC6483978                 |
| 4-6 | **Smartphone App for ED Clinical Photography (Mountain et al. 2019)**          | 응급실 임상사진 앱 + 표준 훈련                                                | 측정 도구로 스케일 표시법 + 식별 가능한 부위 기록법 학습 후 품질 향상                                              | 10.2196/14531              |
| 4-7 | **SkinTracker In-person Onboarding (Truong et al. 2023)**                      | Month 0 대면 방문: **장비 제공 + e-Consent + 사진 촬영 비디오 + 단계별 텍스트/그래픽 안내** | 강력한 대면 온보딩 + 원격 자가수집 하이브리드 모델                                                          | [본 보고서 2-2 참조]             |
| 4-8 | **Standardized Photography for Hair Loss - 2-minute Video (PMC12330203)**      | **언제·어떤 뷰·어떻게 업로드** 3개 핵심 항목의 2분 비디오                              | 짧은 비디오로 환자 동기·만족도·정확도 향상                                                               | [본 보고서 2-9 참조]             |

### 4.A 온보딩 설계 핵심 요소 (메타 종합)

1. **초기 대면(또는 화상) 1:1 세션**으로 장비·앱 사용법 시연 (PCOS 연구는 화상도 가능)
2. **2-5분 단편 비디오** + 단계별 텍스트+그래픽 안내
3. **e-Consent**에 다음 포함: 멀티미디어, 글로사리, Q&A, 이해도 퀴즈
4. **디지털 리터러시 사전 평가** → 지원 수준 차등 (개인 접촉 vs 자가 진행)
5. 시범 촬영 1-2회로 피드백 받은 후 본 데이터 수집 시작

---

## 5. 데이터 품질 관리 및 재수집 UX

| # | 연구 | 품질 관리 방식 | 재수집 UX | DOI/URL |
|---|------|--------------|----------|---------|
| 5-1 | **Vodrahalli AI quality tool (2023)** | 캡처 시점 ML 평가: blur/lighting/zoom 3종; ROC-AUC 0.78 | **사유 텍스트 + 최대 4회 재촬영 허용**; 다만 "어떻게 개선할지" 가이드는 부재가 한계 | [본 보고서 2-3] |
| 5-2 | **DermAI on-device real-time check (2025)** | 캡처 시 실시간 품질 검사; 미달 샘플은 데이터셋에 미진입 | 캡처 시점 차단 + 재촬영 강제 | [본 보고서 2-4] |
| 5-3 | **Wound Image Quality with Color Checker Feedback (Vouri et al. 2021)** | 색표 스티커 + 스마트폰 홀더로 표준화. **2개 객관 품질 매개변수**: sharpness + color checker presence | 실시간 피드백 그룹: color checker detection ratio **0.96 vs 0.86 (basic)**; 환자 1인 평가 시간 중앙값 < 50초 | 10.2196/26149 |
| 5-4 | **Crowdsourcing Framework for Medical Datasets (Quinn et al. 2018)** | Pre-/Real-time-/Post- 단계 품질 통제 | **실시간 품질 통제가 19% 데이터 품질 향상** | PMC5961774 |
| 5-5 | **Reject Analysis (digital radiography baseline, 1991)** | 거부 이미지 분석 → 재교육·워크플로 개선 | 거부 사유 48.4%는 자세, 21%는 아티팩트 | PubMed 1855510 |
| 5-6 | **Automated Image Quality and Protocol Adherence in Teledermatology (Liebertpub 2023)** | 딥러닝 기반 자동 프로토콜 준수 평가 | 신규 영역 | 10.1089/tmj.2023.0155 |
| 5-7 | **Best Face Auto Capture for Mobile (KBY-AI 2025)** | 모든 품질 요건 충족 시 자동 셔터 | UX 자동화로 사용자 부담 감소 | 산업 보고서 |
| 5-8 | **Color/Measurement Calibration for Wound (Wang et al. 2023)** | 보정용 차트 사용으로 다른 조명·거리·렌즈에서 촬영한 이미지 비교 가능 | 표준화 차트 = 환경 변동성 흡수 | 10.3390/healthcare11020273 |

### 5.A 품질 관리 UX 베스트 프랙티스

1. **캡처 시점 검사 > 업로드 시점 검사** (사후 거부는 사용자 좌절 ↑)
2. **자동 셔터** 사용 — 모든 품질 조건 충족 시에만 발동 (FAIN, KBY-AI)
3. **재촬영 시 "구체적 개선 방법" 제공** (Vodrahalli의 한계점: 사유만 제공 → 개선 권장 부재)
4. **참조물(색표 스티커, 동전)**로 카메라·조명 변동성 흡수
5. **최대 재시도 횟수 4-5회 권장** (Vodrahalli: 13%는 4회 후에도 미달)
6. **품질 미달 시에도 최선 이미지 저장** (완전 차단 시 데이터 손실)

---

## 6. 장기 순응도 향상 전략

| # | 연구 | 전략 | 효과 | DOI/URL |
|---|------|------|------|---------|
| 6-1 | **EMA Meta-analysis (Wrzus & Neubauer 2023)** | 평균 6회/일 프롬프트, 7일 추적, 평균 79% 순응 | **총 평가 수·일수·일별 횟수 모두 순응도 예측 못 함** → 디자인 결정은 다른 요인 의존 | 10.1177/10731911211067538 |
| 6-2 | **Investigating Best Practices for EMA (PMC 2024)** | 임상에선 6회/일 ↑(89%), 비임상에선 2-3회(91.7%) | 컨텍스트별 최적 빈도 다름 | [기존 _workspace4 4-2 참조] |
| 6-3 | **EMA Compliance in Children/Adolescents Meta (Wen et al. 2017)** | 시간 기반 표본화 평균 78.3% 순응 | **6개월 추적 시 66.7% → 42%로 감소** | [기존 _workspace4 4-1 참조] |
| 6-4 | **Self-monitoring & App Retention (Lee et al. 2018)** | 자기 모니터링 정규 사용자: 40주 후 80% 유지 vs 비사용자 60% | **자가 모니터링 기능 사용이 retention 핵심** | 10.1371/journal.pone.0201166 |
| 6-5 | **App Retention Survival Analysis (Pratap et al. 2020)** | 2/3 이상이 다운로드 후 한 번만 사용 | retention 위기 정량화 | 10.2196/16309 |
| 6-6 | **Notifications Micro-Randomized Trial (Bidargaddi et al. 2018)** | 시간 가변 푸시 알림; 임의배정 | 알림 후 24시간 내 engagement ↑ | 10.2196/10123 |
| 6-7 | **Notifications & Behavior Change (Hardeman et al. 2023)** | Behavior change 앱 알림 효과 | **단기 engagement 강함**, 장기 효과 제한 | 10.2196/38342 |
| 6-8 | **Stress App Push Notification Timing (PLOS 2017)** | 자연 peak: 평일 오후 8시 | 사용자의 자연 사용 시간대 활용 권장 | 10.1371/journal.pone.0169162 |
| 6-9 | **Gamification & Medication Adherence Scoping Review (JMIR 2022)** | 점수, 리더보드, 진행바, 보상 | 효과는 구현·실행 의존; 자기결정이론(SDT) 사용 | 10.2196/30671 |
| 6-10 | **Gamification on Physical Activity Systematic Review (JMIR 2022)** | 게이미피케이션이 활동 참여 증가 | 가족 협력 시 효과적, 모르는 사람 협력은 비효과적 (경쟁이 더 효과적) | 10.2196/27794 |
| 6-11 | **e-Diary Adherence in Dermatology Trials (Wettach et al. 2020)** | 매일 약 도포 사진 촬영 | **e-diary 사진 촬영 순응도 93%** (87-97%) | PMC7064941 |
| 6-12 | **Digital Phenotyping Pilot in Women's Cohort (PMC 2025)** | Beiwe 앱; 8일간 EMA 하루 2회 (오후·저녁) + 분 단위 가속도·GPS | 강력한 패시브 + 능동 결합 가능성 | PMC12407220 |

### 6.A 장기 순응도 베스트 프랙티스

1. **사진 촬영 자체가 자가 모니터링이 되도록 설계**: 자가 모니터링 사용자가 retention 80% (vs 60%)
2. **알림 빈도**: PCOS 일상 모니터링은 비임상 모델 → **하루 1-2회**가 최적
3. **자연 사용 시간대 활용**: 저녁 7-9시 (앱별로 다름)
4. **시각적 진행 표시**: 진행바, 스트릭(streak)
5. **임상의 의뢰**: 자가 의뢰보다 retention·compliance 모두 높음
6. **개인화 피드백**: 실시간 데이터 시각화로 사용자에게 가치 제공
7. **6개월 이상 추적은 단계적 강화 전략 필수** (인센티브, 코칭, 푸시 단계화)

---

## 7. 실험 프로토콜 설계 베스트 프랙티스 종합 (PCOS 적용)

### 7.1 사용자에게 요구할 구체적 행위 (PCOS 자가수집 표준 프로토콜 제안)

**얼굴 사진 (피부·여드름·다모증·잔주름):**

| 항목 | 권장 수치 | 근거 |
|------|----------|------|
| 빈도 | 매일 1회 (1차) → 주 3회 (장기) | EMA Meta + 6개월 retention 우려 |
| 시간대 | 매일 동일 시간(예: 기상 후 15분 이내) | 조명·피지 변동 통제 |
| 위치 | 동일 실내 위치, 창가 자연광 또는 일정 LED | Hair loss 가이드, MDedge dermatology |
| 거리 | 30 cm (얼굴 전체) / 클로즈업은 화면 50-75% 점유 | Almeida PD 표준 + FAIN |
| 각도 | 정면 90° + 좌·우 측면 30°/60° (3 뷰) | Light Angle Study + 미용외과 표준 |
| 자세 | 좌위, 정면 주시, 중립 표정 | 임상 사진 표준 |
| 메이크업·악세서리 | 제거 | MDedge dermatology |
| 배경 | 단색 (블루 또는 그린) | MDedge + Skin Tone 가이드 |
| 색 참조 | 색표 스티커 또는 컬러 체커 (선택) | Wound Image Color Checker |

**음성 녹음:**

| 항목 | 권장 수치 | 근거 |
|------|----------|------|
| 빈도 | 매일 1회 또는 주 3회 | EMA Meta + 사용자 부담 |
| 환경 | 저소음 환경 (조용한 방, 외부 소음 < 50 dB) | Master Protocol Vocal Biomarker |
| 마이크 거리 | 입과 마이크 30 cm | Almeida PD 표준 |
| 코덱 | 비압축 WAV 강제 (앱 내 고정) | Plug-and-Play Microphones 연구 |
| 과제 | (1) 지속 모음 /a/ 6초 × 3회, (2) 표준 문장 낭독, (3) 자유 발화 20초 (CAPE-V) | ASHA Expert Panel + Master Protocol |
| 메타데이터 | 기기 모델, OS, 시간, 환경 메모 | Master Protocol |

### 7.2 온보딩 프로토콜 (PCOS 자가수집 표준)

1. **사전 디지털 리터러시 평가**: 5문항 자가 진단
2. **e-Consent 모듈**:
   - 동영상(3분) + 텍스트 동의서
   - 글로사리 (PCOS, 디지털 바이오마커, 익명화)
   - 이해도 퀴즈 3문항 통과 후 동의 진행
   - 동의 항목: 사진 촬영, 음성 녹음, 익명 데이터 활용, 제3자 비공유, 철회권
3. **장비 가이드**:
   - 권장: 단색 배경(블루 시트), 링라이트 또는 자연광 위치
   - 옵션: 색표 스티커 제공 (우편 발송)
4. **2분 튜토리얼 비디오**: (1) 언제 (2) 어디서 (3) 어떻게 (4) 업로드 방법
5. **시범 촬영 2회**: 즉시 품질 피드백 + 개선 안내
6. **첫 주 화상 코칭 옵션**: 디지털 리터러시 낮은 사용자

### 7.3 캡처 시점 UX

1. **얼굴 정렬 인디케이터(FAIN)**: 타겟 위치 + 동적 정렬 인디케이터; 정렬 시 색상 빨강→파랑 + 자동 셔터
2. **실시간 품질 검사** (DermAI 모델):
   - blur, lighting, zoom/cropping 자동 검사
   - 미달 시 "구체적 개선 안내" (단순 사유가 아닌 행동 가이드)
   - 최대 4회 재촬영, 그래도 미달이면 최선 이미지 + 플래그 저장
3. **자동 메타데이터 기록**: 기기·OS·시간·조도(EXIF)

### 7.4 장기 순응도 전략

1. **푸시 알림**: 하루 1회, **사용자가 선택한 시간** (저녁 7-9시 기본)
2. **자가 모니터링 시각화**: 시간 경과에 따른 피부·음성 트렌드 차트 제공 (사용자 가치)
3. **진행 표시**: 스트릭(연속 일수), 진행바
4. **임상의 의뢰 권장**: 자가 의뢰 대비 retention 높음
5. **단계적 강화** (6개월 추적 시):
   - 1-2개월: 기본 알림
   - 3-4개월: 개인화 피드백 + 트렌드 인사이트
   - 5-6개월: 인센티브 또는 의료진 코칭

### 7.5 동의·프라이버시 UX

1. **데이터 사용 명세 명시**: 저장 위치, 보관 기간, 익명화 방법, 제3자 공유 정책
2. **선택적 동의**: 사진/음성 각각 별도 동의; 익명 연구 활용 vs 식별 데이터 활용 분리
3. **철회 인터페이스**: 1-탭 데이터 삭제 옵션
4. **민감 정보 라벨링**: 음성은 PHI 수준 보안 적용

---

## 8. 참고문헌 목록 (32편)

### 피부·얼굴 자가촬영 (12편)

1. Webster DE, Suver C, Doerr M, et al. The Mole Mapper Study, mobile phone skin imaging and melanoma risk data collected using ResearchKit. Sci Data. 2017;4:170005. doi:10.1038/sdata.2017.5
2. Truong K, Toribio A, et al. Development of SkinTracker, an integrated dermatology mobile app and web portal enabling remote clinical research studies. Front Digit Health. 2023;5:1228503. doi:10.3389/fdgth.2023.1228503
3. Vodrahalli K, Daneshjou R, et al. Development and Clinical Evaluation of an Artificial Intelligence Support Tool for Improving Telemedicine Photo Quality. JAMA Netw Open. 2023. PMC10018405
4. Bezerra et al. DermAI: Clinical dermatology acquisition through quality-driven image collection for AI classification in mobile. arXiv:2511.10367. 2025
5. Hashimoto T, et al. A smartphone application for personalized facial aesthetic monitoring. Skin Res Technol. 2024. doi:10.1111/srt.13824
6. Cell Phone App for Facial Acne Severity Assessment (Acne-RegNet). Applied Intelligence. 2022. doi:10.1007/s10489-022-03774-z
7. Automatic Acne Object Detection and Acne Severity Grading Using Smartphone Images and AI (AcneDet). Diagnostics. 2022;12(8):1879. doi:10.3390/diagnostics12081879
8. Kunde L, McMeniman E, Parker M. Self-acquired patient images: the promises and the pitfalls. PubMed 26963112. 2016
9. Standardization of Clinical Photos for Tracking Management of Hair Loss in Dermatology Clinics. PMC12330203. 2025
10. Best Practices for Capturing Clinical and Dermoscopic Images With Smartphone Photography. The Hospitalist/MDedge. 2023
11. Vekony et al. Patient photographs taken without instructions are of sufficient quality for clinical decision-making in teledermatology. PubMed 39090050. 2024
12. Lester JC, Jia JL, Zhang L, Okoye GA, Linos E. Absence of images of skin of colour in publications of COVID-19 skin manifestations. Br J Dermatol. 2020. (Skin tone standardization; PMC9297997)

### PCOS·여성건강 (9편)

13. Mahalingaiah S, Fruh V, et al. Design and methods of the Apple Women's Health Study: a digital longitudinal cohort study. Am J Obstet Gynecol. 2022. PMC10518829
14. Pirotta S, Joham A, Hochberg L, et al. Personalized Mobile Tool AskPCOS Delivering Evidence-Based Quality Information about Polycystic Ovary Syndrome. PubMed 30189453. 2018
15. Identifying Women at Risk for Polycystic Ovary Syndrome Using a Mobile Health App: Virtual Tool Functionality Assessment. JMIR Form Res. 2020;4(5):e15094. doi:10.2196/15094
16. Mobile Apps Designed for Patients With Polycystic Ovary Syndrome: Content Analysis Using the Mobile App Rating Scale. JMIR. 2025. doi:10.2196/71118
17. Alfawzan N, Christen M, Spitale G, Biller-Andorno N. Privacy, Data Sharing, and Data Security Policies of Women's mHealth Apps: Scoping Review and Content Analysis. JMIR Mhealth Uhealth. 2022. doi:10.2196/33735
18. Epstein DA, et al. Examining Menstrual Tracking to Inform the Design of Personal Informatics Tools. CHI. 2017. PMC5432133
19. Liu et al. Person-Generated Health Data in Women's Health: Scoping Review. JMIR. 2024. doi:10.2196/53327
20. Utilizing a digital cohort to understand the health burden and lifestyle characteristics across the life course in individuals with polycystic ovary syndrome and possible PCOS. Front Endocrinol. 2025. doi:10.3389/fendo.2025.1585628
21. Good-Quality mHealth Apps for Endometriosis Care: Systematic Search. JMIR. 2025. PubMed 39918848

### 온보딩·동의 (5편)

22. Conducting Internet-Based Visits for Onboarding Populations With Limited Digital Literacy to an mHealth Intervention. PMC8086779. 2021
23. Doerr M, Maguire Truong A, Bot BM, et al. Formative Evaluation of Participant Experience With Mobile eConsent in the App-Mediated Parkinson mPower Study: A Mixed Methods Study. PubMed 28209557. 2017
24. Digital Informed Consent/Assent in Clinical Trials Among Pregnant Women, Minors, and Adults: Multicountry Cross-Sectional Evaluation of Comprehension and Satisfaction. JMIR Hum Factors. 2025. doi:10.2196/65569
25. Pratap A, et al. Maximizing Engagement in Mobile Health Studies: Lessons Learned and Future Directions. PMC6483978. 2019
26. Mountain et al. A Smartphone App for Improving Clinical Photography in Emergency Departments: Comparative Study. JMIR Mhealth Uhealth. 2019. doi:10.2196/14531

### 데이터 품질 (3편)

27. Vouri SM, et al. Wound Image Quality From a Mobile Health Tool for Home-Based Chronic Wound Management With Real-Time Quality Feedback: Randomized Feasibility Study. JMIR Mhealth Uhealth. 2021. doi:10.2196/26149
28. Quinn TC, et al. A Crowdsourcing Framework for Medical Data Sets. PMC5961774. 2018
29. Automated Image Quality and Protocol Adherence Assessment of Examinations in Teledermatology. Telemed J E Health. 2023. doi:10.1089/tmj.2023.0155

### 장기 순응도·알림·게이미피케이션 (3편)

30. Wrzus C, Neubauer AB. Ecological Momentary Assessment: A Meta-Analysis on Designs, Samples, and Compliance Across Research Fields. Assessment. 2023. doi:10.1177/10731911211067538
31. Lee K, Kwon H, Lee B, et al. Effect of self-monitoring on long-term patient engagement with mobile health applications. PLOS ONE. 2018. doi:10.1371/journal.pone.0201166
32. Bidargaddi N, et al. To Prompt or Not to Prompt? A Microrandomized Trial of Time-Varying Push Notifications to Increase Proximal Engagement With a Mobile Health App. JMIR Mhealth Uhealth. 2018. doi:10.2196/10123

---

## 9. 부록: 기존 `_workspace4/01_ux_methodology_literature.md` 와의 차별점

| 비교 항목 | _workspace4 (기존) | _workspace5/02 (본 보고서) |
|----------|-------------------|------------------------|
| 초점 | 일반 mHealth UX, EMA, 동의, 신뢰 | **PCOS·자가촬영 프로토콜 특화** |
| 대상 영역 | 얼굴·음성 수집 일반론 | **참여자에게 요구하는 구체적 행위** |
| 수치적 지시사항 | 부분적 (5000K, 30cm 등) | **거리·각도·시간대·빈도·자세 표 정리** |
| PCOS·여성건강 | 1-2편 언급 | **9편 집중 분석** |
| 시스템 사례 | 12개 시스템 종설 | Mole Mapper, SkinTracker, DermAI, Vodrahalli, AskPCOS, Apple WHS 등 **6개 핵심 자가수집 시스템 심층** |
| 출력 | 합성·가이드라인 일반 | **PCOS 적용 표준 프로토콜 표 7.1-7.5** |

본 보고서는 후속 ux-methodology-synthesizer 단계에서 `_workspace4`의 일반 UX 원칙과 결합하여, **PCOS·자궁내막증 자가수집 실험을 위한 종합 실행 가이드**로 통합되어야 한다.
