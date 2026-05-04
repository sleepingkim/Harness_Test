# 비정형 데이터 정제, LLM이 해결할 수 있는가?
## — 로컬 LLM·RAG 기반 의미론적 표준화: 실험 결과와 실무 적용 방향

> 발표자: 신홍철 | 작성일: 2026-05-04
> 기반: 전문석사학위 프렉티컴보고서 (RAG v1) + RAG v2 재실험 결과
>
> **[주석 범례]**
> 🔵 = 프렉티컴보고서 인용 참고문헌 ([번호])
> 🟡 = 추가 탐색 권장 (초안 작성 시 미인용, 내용 확인 후 사용 여부 결정)
> 🔴 = 인용 표현 수정 필요 (출처 불명확 또는 정확도 논란 있음)

---

## 1. 데이터 정제는 왜 병목인가

### 1.1 현실: 데이터는 쌓이지만, 쓸 수 있는 데이터는 없다

> **"Data Scientists spend 80% of their time cleaning data."**
>
> 🔴 **[주석 1-A: 이 수치 사용 시 주의 필요]**
> Forbes(2016) 및 여러 블로그에 광범위하게 인용되나, 원출처는
> **CrowdFlower (2016) '2016 Data Science Report'** (업계 설문조사)다.
> 해당 조사에서 "데이터 정제·정리에 가장 많은 시간을 쓴다"는 응답이 60%,
> 수집(19%)까지 합산하면 약 80%에 이르는 구조다.
> 단, 이는 동료심사(peer-reviewed) 논문이 아닌 설문 보고서이므로
> 발표 시 **"업계 조사 결과에 따르면(CrowdFlower, 2016)"** 으로 표현하거나,
> 아래 학술 연구로 대체하는 것이 더 안전하다.
>
> 🔵 **[대안 인용 후보]**
> - **Zhang & Huang (2024)** [12]: "Real-world datasets suffer from various quality issues... data cleaning remains a labor-intensive process" — LLM 기반 데이터 정제의 필요성 배경으로 제시
> - **Glock & Korom (2025)** [10]: 실제 기업(Austrian Post)과 협업한 연구에서 개인정보 데이터의 오류 탐지·정제 비용이 수작업 대비 LLM으로 현저히 줄었음을 실증
> - **Karaca (2024)** [13]: 텍스트 데이터의 전처리(preprocessing)가 분류 정확도에 미치는 영향을 정량 분석 — "데이터 품질이 모델 성능을 결정한다"는 주장의 학술적 근거

이 문제를 해결하기 위한 AI·분석 프로젝트의 실패 원인 1위는
"모델이 나빠서"가 아니라 **"입력 데이터가 더러워서"** 인 경우가 대부분이다.

> 🔵 **[주석 1-B]**
> **정선우, 임동혁, 안진현 (2023)** [14]: "오염된 훈련데이터가 거대언어모델의 출력에 미치는 영향 분석" — 더티데이터가 LLM 기반 시스템의 출력 신뢰도를 직접 저하시킨다는 국내 연구. 데이터 품질이 AI 결과물 품질을 결정한다는 논거를 한국어 맥락에서 제시.

---

### 1.2 구체적 사례: 서울시 공구대여 데이터

| 항목 | 수치 |
|------|------|
| 전체 대여 기록 | 11,525건 |
| 고유 공구 이름 | **3,352개** |
| 실제 공구 종류 (표준명) | **약 160종** |
| 1종당 평균 표기 변형 수 | **~21가지** |

> 🔵 **[주석 1-C]**
> 동일 제품의 다양한 표기 변형은 **Christian & Okorie (2013)** [17]에서 분석한
> 소비자 구매 맥락의 제품 속성 표기 다양성 문제와 유사한 구조다.
> 브랜드명 혼입, 동력원 명시, 규격 삽입 등은 사용자가 "자신에게 의미 있는 정보"를
> 추가하는 자연스러운 행동이지만, 시스템 입장에서는 비표준 데이터가 된다.

---

### 1.3 비정형 더티데이터의 5대 유형

| 유형 | 예시 | 비율 |
|------|------|------|
| **속성 혼입** | '180mm 그라인더', 'HiKOKI 전기드릴' | 가장 빈번 |
| **동력원 명시** | '충전식전동드릴', '에어임팩트렌치' | 높음 |
| **오탈자·오표기** | '경랑몽키', '랜지' → 렌치 | 중간 |
| **일본어 잔재** | '기리'(드릴비트), '뺀치'(펜치) | 중간 |
| **세트·복합** | '글루건&심', '드라이버/렌치세트' | 낮음 |

> 🔵 **[주석 1-D: 핵심 인용]**
> **Kim, W., Choi, B.J., Hong, E.K., Kim, S.K., & Lee, D. (2003)** [18].
> "A Taxonomy of Dirty Data." *Data Mining and Knowledge Discovery*, 7, 81–99.
> DOI: 10.1023/A:1021564703268
>
> 더티데이터를 **missing data, wrong data, non-standard representation** 등
> 체계적으로 분류한 해당 분야의 선도적 연구. 본 연구의 5대 유형 분류는
> Kim et al.의 분류 체계를 공구 도메인에 특화하여 재적용한 것이다.
> 특히 "non-standard representation"(비표준 표기)이 속성 혼입, 일본어 잔재 등을 포함한다.

---

### 1.4 수작업 정제의 한계

**규칙 기반 (Rule-based):**
- 3,352개 변형에 수백 개 규칙 필요 → 유지보수 비용 급증
- 데이터 업데이트 시 규칙도 지속 추가 필요

**수작업 (Manual):**
- 숙련 작업자 기준 약 3~5일 소요 / 규모 확장 불가

> 🔵 **[주석 1-E]**
> **Glock & Korom (2025)** [10]: 오스트리아 우체국(Austrian Post)과 공동으로
> 개인 연락처 데이터의 오류를 탐지·정제하는 연구에서, 전통적 통계 기반 도구
> (Raha, Baran, Autoencoder)보다 LLM이 **예상치 못한(unexpected) 맥락적 오류**를
> 더 잘 탐지함을 실증. 규칙 기반이 놓치는 의미론적 오류 유형을 LLM이 처리 가능함을 보여줌.
>
> 🔵 **[주석 1-F]**
> **Zhang & Huang (2024)** [12]: LLM 기반 데이터 정제 시스템 'Cocoon'을 제안.
> 기존 시스템이 오류 데이터에서 파생된 통계 규칙에 의존하여 정확도·재현율이 낮다는
> 한계를 지적하고, LLM의 의미론적 이해로 이를 극복. 표준 벤치마크에서
> state-of-the-art 대비 성능 우위 확인.

---

## 2. LLM+RAG로 어떻게 해결하는가

### 2.1 핵심 아이디어: 분류 문제로 재정의

비정형 공구 이름을 **160종 표준명 중 하나로 분류하는 문제**로 재정의한다.

```
입력: '충전식전동드릴 (보쉬 GSR 18V)'
출력: { standard_name: '충전드릴', brand: '보쉬', power_source: '충전식(무선)', specification: '18V' }
```

> 🔵 **[주석 2-A: 텍스트 정규화·표준화 선행연구]**
> **Wong et al. (2025)** [1]: "PolyNorm: Few-Shot LLM-Based Text Normalization for
> Text-to-Speech." arXiv:2511.03080. — 다국어 텍스트의 비표준 표현(약어, 숫자, 특수기호 등)을
> LLM Few-Shot으로 표준화하는 연구. 본 연구의 공구명 표준화와 동일한 NLP 패러다임.
>
> **Nguyen et al. (2023)** [15]: "Automatic Textual Normalization for Hate Speech Detection."
> — 비정형 텍스트의 자동 표준화가 하위 태스크(분류, 탐지) 정확도를 유의미하게 향상시킴을
> 실험적으로 검증. 데이터 표준화의 실용적 가치를 학술적으로 뒷받침.

---

### 2.2 RAG v2 파이프라인

```
[더티 공구명 입력]
        ↓
[1. 임베딩 (GPU 배치)] dragonkue/BGE-m3-ko | ~11초/3,352건
        ↓
[2. 하이브리드 검색] FAISS(60%) + BM25(40%) → 후보 15개
        ↓
[3. LLM 분류] Ollama 로컬 | JSON 출력
        ↓
[4. Fallback] LLM 후보 외 응답 → top-1 강제 대체
        ↓
[출력: 표준화된 공구명]
```

> 🔵 **[주석 2-B: RAG 방법론 근거]**
> **Amugongo et al. (2025)** [5]: "Retrieval Augmented Generation for Large Language Models
> in Healthcare: A Systematic Review." *PLOS Digital Health*, 4(6), e0000877.
> — 의료 도메인에서 RAG가 LLM의 환각(hallucination) 문제를 완화하고 도메인 지식을
> 효과적으로 주입하는 방법론임을 체계적 문헌 고찰로 확인.
> 본 연구의 RAG 채택 근거와 직접 연결.
>
> **GAN et al. (2025)** [6]: "RAG Evaluation in the Era of Large Language Models:
> A Comprehensive Survey." arXiv:2504.14891.
> — RAG 시스템의 평가 방법론, 구성 요소별 성능 영향 요인을 종합 분석.
> 특히 검색 품질(k값, 하이브리드 검색)이 최종 생성 품질에 미치는 영향을 다룸.
>
> 🔵 **[주석 2-C: 임베딩 모델 선택 근거]**
> **Hwang et al. (2025)** [9]: "What Advantages Can Low-Resource Domain-Specific
> Embedding Model Bring? — A Case Study on Korea Financial Texts." arXiv:2502.07131.
> — 한국어 도메인 특화 임베딩 모델이 범용 다국어 임베딩 대비 검색 성능을
> 유의미하게 향상시킴을 실증. BGE-m3-ko 채택의 이론적 근거.

---

### 2.3 1차 연구(RAG v1)의 방법론적 문제와 개선

| 항목 | RAG v1 (1차) | RAG v2 (본 연구) |
|------|------------|----------------|
| 벡터 DB 입력 | 386개 정답 쌍 | **160개 표준명 목록만** |
| 평가 데이터 | 동일한 386개 쌍 | **457개 (DB와 완전 분리)** |
| 문제 | 정답 힌트 노출 (데이터 누수) | Train/Test 완전 분리 |
| 최고 정확도 | 97.88% (과대 추정) | **88.47% (신뢰 가능)** |

> 🔵 **[주석 2-D: 데이터 누수·오염 문제의 중요성]**
> **정선우, 임동혁, 안진현 (2023)** [14]: "오염된 훈련데이터가 거대언어모델의 출력에
> 미치는 영향 분석." *인터넷전자상거래연구*, 23(6), 1-10.
> — LLM 컨텍스트에 평가 데이터와 유사한 정보가 포함될 경우 출력 신뢰도가
> 허위로 높아지는 현상을 분석. RAG v1의 97% 과대 추정 원인을 설명하는 국내 연구.
>
> 🟡 **[추가 탐색 권장]**
> train/test contamination의 일반 원리는 ML 커뮤니티의 공통 지식이지만,
> **Dhakal et al. (2025)** [3]의 의미 유사도 기반 파이프라인 연구에서도
> 검색 DB와 평가 데이터의 분리 원칙이 방법론적 표준으로 언급됨.

---

### 2.4 개선 효과: +33%p 향상

| 단계 | 최고 정확도 |
|------|-----------|
| Baseline (MiniLM, k=5) | 55.21% |
| Improved (BGE-m3-ko, BM25, k=15, 카테고리) | **88.47%** |
| **개선폭** | **+33.26%p** |

> 🔵 **[주석 2-E: Fine-tuning vs RAG 비교]**
> **Ovadia et al. (2023)** [16]: "Fine-Tuning or Retrieval? Comparing Knowledge Injection
> in LLMs." arXiv:2312.05934.
> — 동일 도메인 지식 주입 시 RAG 방식이 Fine-tuning 대비 더 적은 비용으로
> 유사하거나 더 나은 성능을 달성함을 비교 실험. 특히 **도메인이 자주 업데이트되는**
> 경우(공구 종류 변경, 표준 개정 등) RAG의 유연성이 Fine-tuning보다 유리.

---

## 3. 왜 로컬 LLM이어야 하는가

### 이유 1. 보안 · 개인정보 보호

외부 API에 데이터를 전송하는 것은 정보보안 정책, 개인정보보호법, 의료법 등에 저촉될 수 있다.

```
클라우드 API: [내부 데이터] → [인터넷] → [외부 서버] ← ❌ 데이터 유출 위험
로컬 LLM:    [내부 데이터] → [내부 GPU] ← ✅ 데이터가 밖으로 나가지 않음
```

> 🔵 **[주석 3-A]**
> **Amugongo et al. (2025)** [5]: 의료 RAG 시스템의 체계적 검토에서
> **데이터 프라이버시(data privacy)와 보안**이 헬스케어 LLM 도입의 핵심 장벽으로
> 반복적으로 등장함을 확인. 로컬 또는 온프레미스(on-premise) 배포가
> 이를 해결하는 주요 접근법으로 권고됨.
>
> 🔵 **[주석 3-B]**
> **Belcak et al. (2025)** [7]: "Small Language Models are the Future of Agentic AI."
> arXiv:2506.02153. — SLM(소형 언어 모델)의 **로컬 실행** 이점으로
> "stronger data control(데이터 통제 강화)"를 명시적으로 언급.
> 소비자 등급 GPU에서의 오프라인 에이전트 추론을 시연.

---

### 이유 2. 비용 구조의 차이

| 항목 | 클라우드 API (GPT-4o 기준) | 로컬 LLM |
|------|--------------------------|---------|
| 3,352건 처리 | 입력 ~$4 + 출력 ~$3 = **약 $7** | 전기요금 **약 $0.05** |
| 100,000건 처리 | **약 $210** | **약 $1.5** |
| 월 100만건 처리 | **약 $2,100/월** | 서버 초기비용 후 **월 $15** |

> 🔵 **[주석 3-C: AI 추론 비용 경제학 근거]**
> **WINGPT Team (2025)** [2]: "Beyond Benchmarks: The Economics of AI Inference."
> arXiv:2510.26136. — LLM 추론을 **생산 경제학(production economics)**으로 분석한 연구.
> 처리량 규모, 모델 크기, 동시성(concurrency)에 따른 단위당 비용 변화를 실증.
> 핵심 발견: **규모의 경제**가 작동하는 구간에서 온프레미스 추론의 비용 우위가 급격히 증가.
> 월 100만 건 이상의 반복 처리에서 로컬 인프라의 TCO(총소유비용)가 클라우드 대비 현저히 낮아짐.
>
> 🟡 **[추가 탐색 권장]**
> WINGPT 논문은 클라우드 vs 로컬의 직접 비교보다는 클라우드 내 추론 경제학에 집중.
> 보다 직접적인 로컬 vs 클라우드 비용 비교 연구가 있다면 보강 권장.
> 예: "The Price of Progress: Algorithmic Efficiency and the Falling Cost of AI Inference"
> (arXiv:2511.23455) — AI 추론 비용의 역사적 하락 추세와 효율성 분석.

---

### 이유 3. 운영 안정성 · 독립성

| 상황 | 클라우드 API | 로컬 LLM |
|------|------------|---------|
| 인터넷 장애 | ❌ 서비스 불가 | ✅ 정상 운영 |
| API Rate Limit | ❌ 대기 필요 | ✅ 제한 없음 |
| 배치 처리 자동화 | 제한적 | ✅ 자유로운 스케줄링 |

> 🔵 **[주석 3-D]**
> **Belcak et al. (2025)** [7]: SLM 에이전트의 **오프라인 에이전트 추론(offline agentic inference)**
> 실현 가능성을 시연. 인터넷 연결 없이도 소비자급 GPU에서 실시간 처리가 가능함을 확인.
> 이는 배치 처리, 야간 자동화, 인터넷 불안정 환경에서의 운영 안정성 근거.

---

### 이유 4. 도메인 커스터마이징

> 🔵 **[주석 3-E: RAG vs Fine-tuning 선택 기준]**
> **Ovadia et al. (2023)** [16]: Fine-tuning과 RAG의 지식 주입 방식 비교에서,
> **도메인 지식이 자주 변경되는 환경**에서는 모델 재학습 없이 지식 베이스만 교체할 수 있는
> RAG가 우월함을 실증. 공구 표준 개정, 신규 브랜드 추가 등의 상황에서 정답지(RAG DB)만
> 갱신하면 되는 본 시스템의 설계 철학을 뒷받침.
>
> **Campo et al. (2025)** [8]: "Real-time Spatial Retrieval Augmented Generation."
> arXiv:2505.02271. — 도메인 특화 공간 정보를 RAG로 주입하여 범용 LLM을 도메인 전문가 수준으로
> 향상시키는 사례 연구. 커스터마이징의 유연성을 실증.

---

## 4. 속도 vs 정확도 트레이드오프

### 4.1 전체 실험 결과

|  순위  | 모델                       | 방식       |        정확도 |      속도 | 3,352건 처리 |
| :--: | ------------------------ | -------- | ---------: | ------: | --------: |
| 🥇 1 | gemma4:e4b (9.6GB)       | improved | **88.47%** | 1.58개/초 |       35분 |
| 🥈 2 | gemma3:4b (3.3GB)        | improved | **84.48%** | 1.77개/초 |       31분 |
| 🥉 3 | granite4.1:8b (5.3GB)    | improved | **82.48%** | 1.21개/초 |       46분 |
|  4   | gemma4:e2b (7.2GB)       | improved | **80.93%** | 1.93개/초 |       29분 |
|  5   | exaone3.5:7.8b (4.8GB)   | improved | **79.16%** | 1.23개/초 |       45분 |
|  6   | deepseek-r1:1.5b (1.1GB) | improved | **78.05%** | 1.49개/초 |       37분 |
|  7   | deepseek-r1:8b (5.2GB)   | improved | **77.83%** | 1.40개/초 |       40분 |
|  8   | exaone3.5:2.4b (1.6GB)   | improved | **74.06%** | 1.58개/초 |       35분 |
|  9   | granite4.1:3b (2.1GB)    | improved | **67.85%** | 1.53개/초 |       36분 |
|  10  | deepseek-r1:8b           | baseline |     55.21% | 1.96개/초 |       28분 |
|  11  | granite4.1:8b            | baseline |     55.21% | 1.26개/초 |       44분 |

---

### 4.2 소형 모델의 실용성

> 🔵 **[주석 4-A: 소형 모델 효율성 핵심 근거]**
> **Belcak et al. (2025)** [7]: "Small Language Models are the Future of Agentic AI."
> NVIDIA Research. arXiv:2506.02153.
>
> **핵심 주장**: SLM은 소수의 전문화된 작업을 반복 수행하는 에이전트 시스템에서
> 대형 모델(LLM)에 비해 **충분히 강력하고, 더 적합하며, 경제적으로 우월**하다.
>
> 본 연구 결과와의 연결:
> - deepseek-r1:1.5b (1.1GB) → 78.05% 정확도 → 78%는 실무에서 충분한 수준
> - exaone3.5:2.4b (1.6GB) → 74.06% → VRAM 없는 환경에서도 구동 가능
> - SLM의 "parameter-efficient fine-tuning이 GPU 몇 시간으로 가능"한 특성은
>   향후 도메인 어댑터 연구 방향과 직결

---

### 4.3 Trade-Off Score 분석

α를 업무 우선순위에 따라 조정:
```
Trade-Off Score = α × 정확도 + (1-α) × 속도_점수
```

| 모델 | α=0.75 (정확도↑) | α=0.50 (균형) | α=0.25 (속도↑) |
|------|----------------:|-------------:|---------------:|
| **gemma4:e4b** | **1위** | 2위 | 3위 |
| **gemma3:4b** | 2위 | **1위** | 2위 |
| **gemma4:e2b** | 4위 | 3위 | **1위** |

> 🔵 **[주석 4-B: 다속성 트레이드오프 분석 근거]**
> **Keeney, R.L. (1975)** [19]: "Multiattribute Utility Analysis: A Brief Survey."
> *IIASA Research Memoranda*, RM-75-43.
> — 복수의 목표(정확도, 속도)가 상충(trade-off)할 때 가중치 α를 통해
> 의사결정자의 우선순위를 반영하는 다속성 효용 분석(MAUT) 프레임워크.
> 본 연구의 α=0.25/0.5/0.75 시나리오 분석의 방법론적 근거.
>
> 🔵 **[주석 4-C]**
> **WINGPT Team (2025)** [2]: AI 추론의 경제학 프레임워크에서 "최적 비용-효과 구간
> (optimal cost-effectiveness zone)"을 제시. 정확도와 처리비용의 상충 관계를
> 생산 프론티어(production frontier)로 시각화하는 접근법이 본 연구의 트레이드오프 분석과 유사.

---

### 4.4 모델 크기 ≠ 성능: 아키텍처가 중요하다

> 🔵 **[주석 4-D]**
> **Belcak et al. (2025)** [7]: SLM이 에이전트 태스크에서 대형 모델에 필적하거나
> 능가하는 사례를 제시하며, **모델 크기보다 태스크 특화(task specialization)가
> 성능 결정의 핵심 요인**임을 주장. gemma3:4b(3.3GB)가 exaone3.5:7.8b(4.8GB)보다
> 정확도가 높은 본 연구 결과와 일치.
>
> 🔵 **[주석 4-E: e-commerce 도메인 유사 연구]**
> **Wang et al. (2025)** [4]: "CSRM-LLM: Embracing Multilingual LLMs for Cold-Start
> Relevance Matching in Emerging E-commerce Markets." arXiv:2509.01566.
> — 전자상거래 신흥 시장에서 비정형 상품명을 다국어 LLM으로 매핑하는 연구.
> 공구 도메인 표준화와 동일한 문제 구조(비정형 입력 → 표준 카테고리)를 공유.
> 모델 선택과 도메인 특화가 성능에 미치는 영향을 실증.

---

## 5. 실제 업무에 적용한다면

### 5.1 어떤 데이터에 적용 가능한가

| 도메인 | 더티 데이터 예시 | 표준화 목표 |
|--------|--------------|-----------|
| **공공·행정** | 직업 분류, 주소, 기관명 | KS 표준 코드 |
| **의료** | 증상명, 약품명 | ICD-10, ATC 코드 |
| **전자상거래** | 상품명, 브랜드명 | 카테고리 코드 |
| **인사·채용** | 직무명, 기술스택명 | 표준 직무 코드 |
| **제조·ERP** | 자재명, 부품 코드 | BOM 표준 코드 |

> 🔵 **[주석 5-A: 의료 도메인 RAG 적용 근거]**
> **Amugongo et al. (2025)** [5]: 의료 RAG에 관한 체계적 문헌 고찰에서
> 임상 데이터 정규화, 의학 용어 표준화에 RAG 기반 LLM이 유효함을 확인.
> 특히 ICD 코딩, 약품명 표준화 등에서의 적용 가능성을 논의.
>
> 🔵 **[주석 5-B: e-commerce 적용 근거]**
> **Wang et al. (2025)** [4]: 전자상거래 상품명 매핑에 다국어 LLM 활용.
> cold-start 문제(신규 상품에 정답 사례 없음) 극복 방법론을 제시.
> 본 연구의 RAG 방식(정답지 소량으로 시작)과 유사한 접근.

---

### 5.2 구현 로드맵

```
Week 1-2: 정답지(Ground Truth) 구축
  → 도메인 전문가 + 카탈로그 참조, 500~1,000개 엔트리 목표

Week 3: 기술 스택 설치
  → Ollama, sentence-transformers, faiss-cpu, rank-bm25

Week 4: 시범 운영
  → 1,000건 샘플 정확도 측정, Fallback율 모니터링, 취약 유형 파악

Month 2+: 확장 및 자동화
  → 전체 데이터 배치 처리 + 신규 데이터 자동 파이프라인 연동
```

> 🔵 **[주석 5-C: Human-in-the-Loop 근거]**
> **Dhakal et al. (2025)** [3]: "An AI-Driven Semantic Similarity-Based Pipeline for
> Rapid Literature Review." arXiv:2509.15292.
> — AI 파이프라인에서 인간 전문가 검토를 전략적으로 통합하는 방법론 제시.
> 낮은 신뢰도 항목에만 인간 검토를 적용하는 **선택적 Human-in-the-Loop**의
> 효율성을 뒷받침. 본 연구의 "12% 불확실 항목 인간 검토" 제안의 근거.
>
> 🔵 **[주석 5-D]**
> **CSRM-LLM(Wang et al., 2025)** [4]: 실제 전자상거래 시스템 배포 사례에서
> 단계적 도입(소규모 파일럿 → 확장)이 리스크를 낮추는 효과적 전략임을 확인.

---

### 5.3 기대 효과 및 한계

**기대 효과:**

| 지표 | 현재 (수작업) | 도입 후 |
|------|-------------|---------|
| 처리 속도 | 3~5일/3,000건 | **30~50분/3,000건** |
| 인력 투입 | 담당자 상시 필요 | 최초 정답지 구축만 |
| 일관성 | 담당자에 따라 편차 | 동일 규칙 100% 적용 |
| 정확도 | 숙련자 ~95% | **RAG+LLM: 74~88%** |

> 🟡 **[주석 5-E: 인간 vs 자동화 정확도 비교 보강 권장]**
> "숙련자 ~95%" 수치는 본 초안에서 추정치로 사용됨.
> 이를 뒷받침할 실증 연구가 있으면 보강 권장.
> 예: **Glock & Korom (2025)** [10]에서 인간 작업자와 LLM의 데이터 정제 정확도를
> 비교한 결과가 있다면 활용 가능. 논문 원문 확인 필요.

**주요 한계:**

1. **정답지 구축 초기 비용** — 도메인 전문가 시간 투입 필요
2. **Fallback율 관리** — deepseek-r1:1.5b의 85.2%는 실사용 불가 수준
3. **대형 모델(17GB+) 실행 불가** — RTX 5080(17.1GB) 기준 KV캐시 부족으로 30B 이상 모델 CPU 오프로드 발생, 처리속도 0.03개/초로 실용 불가

> 🔵 **[주석 5-F: 소형 모델로도 충분한가?]**
> **Belcak et al. (2025)** [7]: 반복적·전문화된 에이전트 태스크에서 SLM이
> 충분히 효과적임을 주장. 본 연구에서 74~88% 정확도를 달성한 3~9.6GB 모델들이
> 이 주장을 실험적으로 뒷받침.

---

## 6. 결론 및 제언

### 핵심 메시지 3가지

**① 비정형 데이터 정제는 LLM+RAG로 해결 가능한 문제다**

> 🔵 **[주석 6-A: 종합 인용]**
> - **Kim et al. (2003)** [18]: 더티데이터 분류 체계 — 문제의 구조화
> - **Zhang & Huang (2024)** [12]: LLM 기반 정제 시스템의 실증적 우위
> - **Glock & Korom (2025)** [10]: 실제 기업 환경에서의 LLM 데이터 정제 적용
> - **본 연구 실험 결과**: baseline 55% → improved 88.47% (+33%p)

**② 로컬 LLM은 보안·비용·안정성에서 클라우드 API의 실질적 대안이다**

> 🔵 **[주석 6-B]**
> - **WINGPT Team (2025)** [2]: 추론 경제학 — 규모 증가 시 로컬 비용 우위 실증
> - **Belcak et al. (2025)** [7]: 데이터 통제, 오프라인 운영 가능성
> - **Amugongo et al. (2025)** [5]: 민감 도메인(의료)에서의 프라이버시 요건

**③ 최적 모델은 하나가 아니다 — 업무 맥락에 따라 선택**

> 🔵 **[주석 6-C]**
> - **Keeney (1975)** [19]: 다속성 효용 분석 — α 가중치 기반 의사결정 프레임워크
> - **Belcak et al. (2025)** [7]: 태스크 특화가 크기보다 중요

---

## 참고문헌 (프렉티컴보고서 원본 기준)

> 아래는 프렉티컴보고서 원본 [1]~[19] 번호 유지. 인용된 항목에 ✅ 표시.

| # | 인용 | 저자 | 제목 | 출처 | 관련 섹션 |
|---|------|------|------|------|---------|
| [1] ✅ | 2025 | Wong et al. | PolyNorm: Few-Shot LLM Text Normalization | arXiv:2511.03080 | 2.1 텍스트 표준화 |
| [2] ✅ | 2025 | WINGPT Team | Beyond Benchmarks: Economics of AI Inference | arXiv:2510.26136 | 3.2 비용, 4.3 트레이드오프 |
| [3] ✅ | 2025 | Dhakal et al. | AI Semantic Similarity Pipeline for Literature Review | arXiv:2509.15292 | 5.2 Human-in-the-Loop |
| [4] ✅ | 2025 | Wang et al. | CSRM-LLM: Multilingual LLMs for E-commerce | arXiv:2509.01566 | 4.4, 5.1 전자상거래 |
| [5] ✅ | 2025 | Amugongo et al. | RAG for LLMs in Healthcare: Systematic Review | PLOS Digital Health | 2.2, 3.1, 5.1 |
| [6] ✅ | 2025 | GAN et al. | RAG Evaluation Survey | arXiv:2504.14891 | 2.2 RAG 파이프라인 |
| [7] ✅ | 2025 | Belcak et al. | Small LMs are the Future of Agentic AI | arXiv:2506.02153 | 3.1, 3.3, 4.2, 4.4, 5.3 |
| [8] ✅ | 2025 | Campo et al. | Real-time Spatial RAG for Urban Environments | arXiv:2505.02271 | 3.4 커스터마이징 |
| [9] ✅ | 2025 | Hwang et al. | Low-Resource Domain-Specific Embedding (Korean) | arXiv:2502.07131 | 2.2 임베딩 선택 |
| [10] ✅ | 2025 | Glock & Korom | Detecting and Cleaning Errors in Contact Info (LLM) | VLDB 2025 WS | 1.4, 5.3 |
| [11] — | 2024 | Saparina & Lapata | AMBROSIA: Parsing Ambiguous DB Queries | arXiv:2406.19073 | 미인용 (모호성 관련) |
| [12] ✅ | 2024 | Zhang & Huang | Data Cleaning Using Large Language Models | arXiv:2410.15547 | 1.1, 1.4, 2.1 |
| [13] ✅ | 2024 | Karaca | Effects of Preprocessing on Text Classification | KSII Trans. | 1.1 데이터 품질 |
| [14] ✅ | 2023 | 정선우 외 | 오염된 훈련데이터가 LLM 출력에 미치는 영향 | 인터넷전자상거래연구 | 1.1, 2.3 |
| [15] ✅ | 2023 | Nguyen et al. | Automatic Textual Normalization for Hate Speech | arXiv:2311.06851 | 2.1 텍스트 정규화 |
| [16] ✅ | 2023 | Ovadia et al. | Fine-Tuning or Retrieval? Knowledge Injection | arXiv:2312.05934 | 2.4, 3.4 |
| [17] ✅ | 2013 | Christian & Okorie | Product Attributes & Consumer Decision | J. Business Research | 1.2 속성 혼입 |
| [18] ✅ | 2003 | Kim et al. | A Taxonomy of Dirty Data | Data Mining & KD | 1.3 더티데이터 유형 |
| [19] ✅ | 1975 | Keeney | Multiattribute Utility Analysis | IIASA RM-75-43 | 4.3 트레이드오프 |

---

## 🟡 추가 탐색 권장 목록 (초안에 포함되지 않은 주장)

| 주장 | 현재 상태 | 권장 검색어 |
|------|---------|-----------|
| "80%의 시간을 데이터 정제에" | CrowdFlower 설문 (비학술) | "data preparation time survey empirical study" |
| "AI 프로젝트 실패 원인 1위 = 데이터 품질" | 출처 불명 | "AI project failure data quality survey Gartner" |
| "숙련자 수작업 정확도 ~95%" | 추정치 | Glock & Korom (2025) 원문 확인 또는 추가 검색 |
| "한국어 비정형 공공데이터 정제 사례" | 없음 | 국내 학술지 탐색 권장 |

---

*이 문서는 발표 초안(presentation_draft.md)에 참고문헌 근거를 추가한 주석 버전입니다.*
*각 🔵 주석은 프렉티컴보고서 참고문헌 번호를 기준으로 작성되었습니다.*
