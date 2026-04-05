# Harness 100 — 사용 가능한 기능 전체 가이드

> 생성일: 2026-04-06
> 경로: `/Users/macbook/Desktop/08.Claude/Skill2_Harness100/harness-100/`
> 언어: 영어(`en/`) · 한국어(`ko/`) 동일 구조 제공

---

## 개요

**Harness 100**은 Claude Code용 **프로덕션급 에이전트 팀 하네스 100종** 라이브러리입니다.
각 하네스는 완결된 워크플로우로, 전문 에이전트 팀 + 오케스트레이터 스킬 + 도메인 확장 스킬로 구성됩니다.

| 항목 | 수치 |
|------|------|
| 하네스 수 | 100종 |
| 에이전트 정의 | 약 489개 |
| 스킬 정의 | 약 315개 |
| 지원 언어 | 영어 / 한국어 |

---

## 공통 구조 (모든 하네스 동일)

```
{NN}-{harness-name}/
└── .claude/
    ├── CLAUDE.md                    # 하네스 개요 및 사용법
    ├── agents/
    │   ├── {전문가-1}.md
    │   ├── {전문가-2}.md
    │   ├── {전문가-3}.md
    │   ├── {전문가-4}.md
    │   └── {reviewer}.md            # 교차 검증 에이전트
    └── skills/
        ├── {orchestrator}/skill.md  # 팀 조율 스킬
        ├── {domain-skill-1}/skill.md
        └── {domain-skill-2}/skill.md
```

**산출물**은 `_workspace/` 디렉토리에 순서대로 저장됩니다.

---

## 도메인별 100종 하네스 목록

### 1. 콘텐츠 제작 (01–15)

| # | 하네스 | 주요 기능 | 핵심 스킬 |
|---|--------|-----------|-----------|
| 01 | YouTube Production | 전략 → 스크립트 → 썸네일 → SEO | hook-writing, thumbnail-psychology |
| 02 | Podcast Studio | 리서치 → 스크립트 → 쇼노트 → 배포 | interview-techniques, audio-storytelling |
| 03 | Newsletter Engine | 콘텐츠 → 이메일 디자인 → 타겟팅 | email-copywriting, audience-segmentation |
| 04 | Content Repurposer | 영상→블로그→SNS 포맷 변환 | multi-format-optimization, platform-tailoring |
| 05 | Game Narrative | 스토리 → 다이얼로그 → 퀘스트 → 세계관 | branching-scenario-design, game-lore |
| 06 | Brand Identity | 브랜드 전략 → 로고 → 가이드라인 → 보이스 | brand-strategy-framework, tone-voice-guide |
| 07 | Comic Creator | 스토리 → 패널 → 다이얼로그 → 일러스트 방향 | panel-layout-patterns, comic-dialogue |
| 08 | Course Builder | 커리큘럼 → 콘텐츠 → 퀴즈 → 실습 | assessment-engineering, lab-scaffolding |
| 09 | Documentary Research | 리서치 → 소스 검증 → 내러티브 → 팩트체크 | research-methodology, source-validation |
| 10 | Social Media Manager | 전략 → 캘린더 → 캡션 → 커뮤니티 | platform-optimization, content-calendar |
| 11–15 | (추가 콘텐츠 하네스) | 세부 콘텐츠 워크플로우 | — |

**적용 프레임워크**: AIDA, Pattern Interrupt, CURVE Formula

---

### 2. 소프트웨어 개발 & DevOps (16–30)

| # | 하네스 | 주요 기능 | 핵심 스킬 |
|---|--------|-----------|-----------|
| 16 | Fullstack Web App | 설계 → 프론트 → 백엔드 → QA → 배포 | component-patterns, api-security-checklist |
| 17 | Mobile App Builder | 설계 → iOS → Android → QA | mobile-ui-patterns, cross-platform-testing |
| 18 | API Designer | 요구사항 → 아키텍처 → 구현 → 보안 | rest-design-patterns, graphql-patterns |
| 19 | Database Architect | 요구사항 → 스키마 → 최적화 → 보안 | schema-design-patterns, query-optimization |
| 20 | CI/CD Pipeline | 파이프라인 설계 → 인프라 → 모니터링 → 보안 게이트 | deployment-strategies, pipeline-security |
| 21 | Code Reviewer | 스타일 → 패턴 → 테스트 → 보안 코드리뷰 | refactoring-patterns, code-quality-metrics |
| 22 | Legacy Modernizer | 레거시 분석 → 전략 → 마이그레이션 → 회귀 테스트 | strangler-fig-patterns, dependency-analysis |
| 23 | Microservice Designer | 분해 → 서비스 설계 → 오케스트레이션 | domain-driven-design, service-mesh-patterns |
| 24 | Test Automation | 단위 → 통합 → E2E → 테스트 데이터 | test-pyramid-patterns, selenium-patterns |
| 25 | Incident Postmortem | 타임라인 → RCA → 액션아이템 | root-cause-analysis, blameless-culture |
| 26 | Infra as Code | 아키텍처 → Terraform → 설정 → 보안 | terraform-patterns, ansible-patterns |
| 27 | Data Pipeline | ETL 설계 → 품질 → 오케스트레이션 | etl-design-patterns, dbt-patterns |
| 28 | Security Audit | 취약점 스캔 → 코드 분석 → 침투테스트 | owasp-testing-guide, threat-modeling |
| 29 | Performance Optimizer | 프로파일링 → 병목 분석 → 최적화 | profiling-tools-guide, benchmarking |
| 30 | Open Source Launcher | 프로젝트 → 문서 → 커뮤니티 → 거버넌스 | license-selection, community-building |

**적용 프레임워크**: SOLID, DDD, OWASP Top 10, Test Pyramid, DORA Metrics

---

### 3. 데이터 & AI/ML (31–42)

| # | 하네스 | 주요 기능 | 핵심 스킬 |
|---|--------|-----------|-----------|
| 31 | ML Experiment | 데이터 → 모델 → 학습 → 평가 | feature-engineering-cookbook, model-selection |
| 32 | Data Analysis | EDA → 통계 → 시각화 → 인사이트 | statistical-methods-guide, data-viz-patterns |
| 33 | Text Processor | 전처리 → 분류 → 추출 → 감성분석 | nlp-preprocessing-toolkit, sentiment-lexicon |
| 34 | Data Migration | 전략 → ETL → 검증 → 성능 | data-validation-frameworks, migration-patterns |
| 35 | API Client Generator | API 스펙 → SDK 설계 → 코드 생성 → 테스트 | code-generation-patterns, sdk-design |
| 36 | Design System | 컴포넌트 → 디자인 스펙 → 코드 → 브랜딩 | component-library-patterns, design-tokens |
| 37 | Web Scraper | 타겟 분석 → 스크래퍼 설계 → 클리닝 → 검증 | scraping-patterns, anti-scraping-detection |
| 38 | Chatbot Builder | 인텐트 → 다이얼로그 플로우 → 통합 | intent-recognition-patterns, nlu-integration |
| 39 | Changelog Generator | 릴리즈 분류 → 작성 → 버전 관리 | semver-guide, changelog-templates |
| 40 | CLI Tool Builder | 명령 설계 → 도움말 → 테스트 | command-design-patterns, cli-best-practices |
| 41 | LLM App Builder | 기획 → 프롬프트 → 통합 → 테스트 | prompt-engineering-techniques, rag-patterns |
| 42 | BI Dashboard | 요구사항 → 데이터 모델 → 대시보드 → 성능 | dashboard-design-patterns, data-viz-best-practices |

**적용 프레임워크**: Feature Engineering, SHAP/LIME, Star Schema, Great Expectations

---

### 4. 비즈니스 & 전략 (43–55)

| # | 하네스 | 주요 기능 | 핵심 스킬 |
|---|--------|-----------|-----------|
| 43 | Startup Launcher | 시장 → 비즈니스 모델 → MVP → 피치 | pitch-deck-framework, unit-economics |
| 44 | Market Research | 시장 규모 → 트렌드 → 경쟁사 → 소비자 | market-sizing-methodology, competitive-analysis |
| 45 | Gov Funding Plan | 보조금 리서치 → 제안서 → 예산 → 규정 | grant-writing-framework, gov-compliance |
| 46 | Product Manager | 로드맵 → 요구사항 → 우선순위 → 지표 | roadmap-templates, feature-prioritization |
| 47 | Strategy Framework | 전략 분석 → 프레임워크 → 실행 계획 | ogsm-framework, balanced-scorecard |
| 48 | Sales Enablement | 세일즈 교육 → 콘텐츠 → 피치 → 이의 처리 | sales-methodology, objection-handling |
| 49 | Customer Support | 분석 → 응답 → KB → 교육 | support-templates, knowledge-base-design |
| 50 | Pricing Strategy | 시장분석 → 가치 → 가격 모델 → 경쟁 | value-based-pricing, psm-methodology |
| 51 | Investor Report | 재무 → 커뮤니케이션 → 시각화 | investor-communication, financial-reporting |
| 52 | Scenario Planner | 시나리오 → 영향 → 위험 → 권고안 | scenario-planning-methodology, risk-assessment |
| 53 | Financial Modeler | 매출 → 비용 → 시나리오 → 밸류에이션 | sensitivity-analysis, dcf-valuation |
| 54 | Grant Writer | 리서치 → 제안서 → 예산 → 검토 | grant-writing-framework, proposal-structure |
| 55 | RFP Responder | 요구사항 분석 → 작성 → 준수 검토 | rfp-response-templates, compliance-checklist |

**적용 프레임워크**: BMC, TAM/SAM/SOM, Porter's 5 Forces, RICE, DCF

---

### 5. 교육 & 학습 (56–65)

| # | 하네스 | 주요 기능 | 핵심 스킬 |
|---|--------|-----------|-----------|
| 56 | Language Tutor | 수준 평가 → 커리큘럼 → 연습 → 진도 | cefr-framework, language-learning-methodology |
| 57 | Exam Prep | 분석 → 학습 가이드 → 모의시험 → 취약점 보완 | exam-strategy-guide, practice-test-design |
| 58 | Thesis Advisor | 리서치 → 구조 → 초안 → 검토 | research-methodology, thesis-structure-guide |
| 59 | Coding Bootcamp | 커리큘럼 → 개념 → 프로젝트 → 코드리뷰 | coding-curriculum-design, bootcamp-project-templates |
| 60 | Debate Simulator | 구조 → 논거 → 반론 → 피드백 | argumentation-framework, toulmin-logic |
| 61 | Competency Modeler | 분석 → 역량 설계 → 평가 → 개발 계획 | competency-framework-design, skill-assessment |
| 62 | ADR Writer | 컨텍스트 → 대안 → 트레이드오프 → 결정 | quality-attribute-analyzer, madr-template |
| 63 | Research Assistant | 문헌 → 개념 맵 → 분석 → 종합 | literature-review-methodology, citation-management |
| 64 | Knowledge Base Builder | 기획 → 콘텐츠 → 분류 → 검색 | knowledge-architecture, search-optimization |
| 65 | Personal Branding | 전략 → 콘텐츠 → 포트폴리오 → SNS | personal-brand-framework, portfolio-design |

**적용 프레임워크**: Bloom's Taxonomy, ADDIE, CEFR, SM-2 Spaced Repetition

---

### 6. 법률 & 컴플라이언스 (66–72)

| # | 하네스 | 주요 기능 | 핵심 스킬 |
|---|--------|-----------|-----------|
| 66 | Contract Analyzer | 조항 분석 → 위험 평가 → 협상 | clause-risk-database, negotiation-playbook |
| 67 | Compliance Checker | 분석 → 통제 → 테스트 → 시정 | compliance-framework-guide, control-testing |
| 68 | Patent Drafter | 발명 분석 → 청구항 → 명세서 → 선행기술 | patent-claim-patterns, prior-art-research |
| 69 | Privacy Engineer | 영향 평가 → 통제 → 설계 → 시정 | privacy-impact-assessment, dpia-framework |
| 70 | Legal Research | 판례 → 선례 분석 → 법률 브리프 | legal-research-methodology, precedent-analysis |
| 71 | Service Legal Docs | 템플릿 → 커스터마이징 → 컴플라이언스 | legal-document-templates, document-automation |
| 72 | Regulatory Filing | 분석 → 서식 → 준수 → 제출 | regulatory-requirements-guide, submission-checklist |

**적용 프레임워크**: IRAC, GDPR/PIPA, IPC/CPC, DPIA

---

### 7. 건강 & 라이프스타일 (73–80)

| # | 하네스 | 주요 기능 | 핵심 스킬 |
|---|--------|-----------|-----------|
| 73 | Meal Planner | 영양 → 식단 설계 → 레시피 → 쇼핑 | nutrition-calculator, ingredient-substitution |
| 74 | Fitness Program | 평가 → 프로그램 → 운동 → 추적 | exercise-prescription-guide, periodization |
| 75 | Tax Calculator | 분석 → 공제 → 시나리오 → 최적화 | tax-code-guide, tax-optimization-strategies |
| 76 | Travel Planner | 목적지 리서치 → 일정 → 예산 → 조율 | itinerary-design-guide, travel-budget-framework |
| 77 | Space Concept Board | 공간 설계 → 레이아웃 → 가구 → 조명 | space-design-principles, layout-templates |
| 78 | Personal Finance | 예산 → 투자 → 부채 → 재정 계획 | budgeting-framework, debt-management-guide |
| 79 | Side Project Launcher | 기획 → 스코핑 → 리소스 → 런칭 | project-scoping-guide, launch-checklist |
| 80 | Wedding Planner | 기획 → 예산 → 벤더 → 타임라인 | wedding-planning-checklist, vendor-management |

**적용 프레임워크**: BMR/TDEE, ACSM Guidelines, Compound Interest

---

### 8. 커뮤니케이션 & 문서화 (81–88)

| # | 하네스 | 주요 기능 | 핵심 스킬 |
|---|--------|-----------|-----------|
| 81 | Technical Writer | 구조 → 작성 → 다이어그램 → 검토 | diagram-patterns, api-doc-standards |
| 82 | Report Generator | 기획 → 분석 → 작성 → 디자인 | report-structure-guide, executive-summary-templates |
| 83 | SOP Writer | 프로세스 분석 → 작성 → 일러스트 → 준수 검토 | sop-template, process-documentation-guide |
| 84 | Meeting Strategist | 목표 → 아젠다 → 퍼실리테이션 → 액션 | meeting-design-framework, facilitation-guide |
| 85 | Public Speaking | 스피치 작성 → 스토리텔링 → 딜리버리 → 비주얼 | speech-writing-framework, presentation-design |
| 86 | Proposal Writer | 기획 → 솔루션 → 작성 → 디자인 | persuasion-framework, proposal-templates |
| 87 | Crisis Communication | 위기 분석 → 메시지 → 응답 → 이해관계자 | crisis-response-framework, message-design |
| 88 | Risk Register | 리스크 평가 → 완화 → 모니터링 | risk-assessment-framework, risk-mitigation-templates |

**적용 프레임워크**: Diataxis, PREP, STAR, Mermaid Diagrams, SemVer

---

### 9. 운영 & 프로세스 (89–95)

| # | 하네스 | 주요 기능 | 핵심 스킬 |
|---|--------|-----------|-----------|
| 89 | Event Organizer | 범위 → 벤더 → 타임라인 → 예산 | event-planning-checklist, timeline-templates |
| 90 | Hiring Pipeline | JD → 소싱 → 스크리닝 → 인터뷰 → 오퍼 | competency-model, interview-scorecard |
| 91 | Onboarding System | 기획 → 콘텐츠 → 타임라인 → 성공 추적 | onboarding-template-library, knowledge-transfer |
| 92 | Operations Manual | 분석 → 문서화 → 템플릿 → 준수 | process-documentation-guide, template-library |
| 93 | Feedback Analyzer | 수집 → 테마 → 인사이트 → 액션 | feedback-analysis-methodology, theme-extraction |
| 94 | Audit Report | 기획 → 통제 테스트 → 발견사항 → 권고 | audit-methodology-guide, finding-classification |
| 95 | Procurement Docs | 분석 → RFQ → 벤더 평가 → 계약 | rfq-template-library, vendor-evaluation |

**적용 프레임워크**: SIPOC, RACI, SMART, NPS/CSAT, BARS

---

### 10. 특화 도메인 (96–100)

| # | 하네스 | 주요 기능 | 핵심 스킬 |
|---|--------|-----------|-----------|
| 96 | Real Estate Analyst | 시장 → 부동산 분석 → 가치평가 → 투자 | cap-rate-analysis, investment-return |
| 97 | E-commerce Launcher | 상품 → 리스팅 → 마케팅 → 운영 | product-listing-optimization, conversion-optimization |
| 98 | Academic Paper | 문헌 → 연구 → 작성 → 편집 | academic-writing-standards, citation-formatting |
| 99 | Sustainability Audit | ESG 분석 → 평가 → 지표 → 권고안 | esg-framework, impact-assessment-guide |
| 100 | IP Portfolio | 특허 → 상표 → 라이선싱 → 전략 | patent-portfolio-management, licensing-agreement |

**적용 프레임워크**: GHG Protocol, Cap Rate/IRR, IMRaD, Georgia-Pacific 15 Factors

---

## 하네스 사용 방법

### 1. 하네스 복사

원하는 하네스를 프로젝트에 복사합니다:

```bash
# 예: YouTube Production 하네스 복사 (한국어)
cp -r harness-100/ko/01-youtube-production/.claude/ /your-project/.claude/
```

### 2. 스킬 실행

```
/youtube-production "채널명: TechTalk, 주제: AI 트렌드 2026, 대상: 직장인"
```

### 3. 실행 모드 선택

| 모드 | 설명 |
|------|------|
| **전체 파이프라인** | 모든 에이전트 투입, 완전한 워크플로우 실행 |
| **도메인 집중 모드** | 특정 에이전트만 사용 |
| **기존 파일 모드** | 이미 있는 자료를 기반으로 특정 단계만 실행 |
| **리뷰 모드** | 리뷰어 에이전트만 사용해 기존 작업물 QA |

### 4. 산출물 확인

실행 후 `_workspace/` 디렉토리에 결과가 저장됩니다:

```
_workspace/
├── 00_input.md          # 정리된 사용자 입력
├── 01_strategy.md       # 첫 번째 에이전트 산출물
├── 02_script.md         # 두 번째 에이전트 산출물
├── 03_thumbnail.md      # 세 번째 에이전트 산출물
├── 04_seo.md            # 네 번째 에이전트 산출물
└── 05_review_report.md  # 최종 검토 보고서
```

---

## 에이전트 팀 커뮤니케이션 방식

- **SendMessage 직접 통신** — 에이전트 간 구조화된 메시지 전달
- **교차 검증** — 리뷰어 에이전트가 모든 에이전트 결과 검증
- **반복 개선** — `🔴 Must Fix` 항목 발견 시 최대 2라운드 수정
- **의존성 DAG** — 병렬 실행 가능한 태스크는 동시 처리

---

## 품질 기준

모든 하네스에 적용되는 공통 기준:

1. **실제 산업 프레임워크** 내장 (AIDA, SOLID, Porter's 5 Forces 등)
2. **구조화된 산출물** — 에이전트별 도메인 특화 템플릿
3. **에러 처리** — 재시도, 스킵, 폴백 전략 정의
4. **태스크 의존성** — 병렬 실행 가능한 명시적 DAG
5. **테스트 시나리오** — 일반 / 기존파일 / 오류 케이스 문서화
6. **범위 유연성** — 하네스별 다중 실행 모드

---

## 도메인별 빠른 선택 가이드

| 목적 | 추천 하네스 |
|------|-------------|
| 유튜브 영상 만들기 | `01-youtube-production` |
| 앱/웹 개발 | `16-fullstack-webapp`, `17-mobile-app-builder` |
| 데이터 분석 | `32-data-analysis`, `31-ml-experiment` |
| 창업/스타트업 | `43-startup-launcher`, `44-market-research` |
| 강의/교육자료 | `08-course-builder`, `59-coding-bootcamp` |
| 계약서/법률 | `66-contract-analyzer`, `67-compliance-checker` |
| 기술 문서화 | `81-technical-writer`, `83-sop-writer` |
| 채용/온보딩 | `90-hiring-pipeline`, `91-onboarding-system` |
| 마케팅/SNS | `10-social-media-manager`, `48-sales-enablement` |
| ESG/지속가능경영 | `99-sustainability-audit` |
| 특허/IP | `68-patent-drafter`, `100-ip-portfolio` |
| AI 앱 개발 | `41-llm-app-builder`, `38-chatbot-builder` |
