---
name: camera-biomarker-paper
description: "스마트폰 카메라 기반 디지털 바이오마커 연구 전체 파이프라인 오케스트레이터. 문헌 탐색 → 할루시네이션 검증 → 합성 보고서(.md/.docx) → IEEE LaTeX 논문 작성까지 에이전트 팀으로 실행. '카메라 바이오마커 연구', '스마트폰 카메라 논문', 'IEEE 논문 작성', '카메라 기반 질병 예측 연구', '논문 파이프라인 실행' 등의 요청 시 이 스킬을 사용할 것."
---

# Camera Biomarker Paper — 파이프라인 오케스트레이터

스마트폰 카메라 기반 디지털 바이오마커 연구의 전체 워크플로우를 조율한다.

## 팀 구성

| 에이전트 | 역할 | 실행 Phase |
|---------|------|-----------|
| camera-biomarker-reviewer | 스마트폰 카메라 바이오마커 문헌 탐색 | Phase 1 |
| (내장) reference-hallucination-guard | 참고문헌 실존 여부 검증 | Phase 1.5 |
| camera-biomarker-synthesizer | 탐색 결과 합성, .md + .docx 저장 | Phase 2 |
| ieee-paper-writer | IEEE LaTeX 논문 작성 | Phase 3 |

**아키텍처**: 순차 파이프라인
`Phase 1` → `Phase 1.5 (검증)` → `Phase 2` → `Phase 3`

모든 에이전트는 `model: "opus"` 사용.

---

## Phase 0: 컨텍스트 확인

실행 전 `_workspace/camera/` 존재 여부 확인:

- **없음**: 초기 실행 → Phase 1부터 전체 실행
- **있음 + 특정 단계 재실행 요청**:
  - "논문만 다시 써줘" → Phase 3만 실행 (기존 01, 02 파일 활용)
  - "합성 보고서 수정해줘" → Phase 2 재실행 → Phase 3 재실행
  - "할루시네이션 재검증해줘" → Phase 1.5 재실행 → Phase 2, 3 재실행
- **있음 + 완전 새 실행 요청**: 기존 `_workspace/camera/`를 `_workspace/camera_prev/`로 이동 후 새 실행

```bash
# 디렉토리 준비
mkdir -p _workspace/camera/ieee_paper
```

---

## Phase 1: 문헌 탐색 (camera-biomarker-reviewer)

```
Agent(
  subagent_type: "camera-biomarker-reviewer",
  model: "opus",
  prompt: "
    연구 주제: 스마트폰 카메라를 활용한 일상 디지털 바이오마커 수집 → AI 질병 예측.
    
    참조 파일: _workspace/스마트폰 카메라 기반 질병 예측 연구.docx (존재하면 반드시 참고)
    기존 연구: _workspace/01_literature_review.md (자궁내막증/PCOS 연구, 연계 분석에 활용)
    
    탐색 범위:
    - rPPG 기반 심혈관/생체신호 (심박수, HRV, SpO2, 혈압)
    - 얼굴/피부 영상 분석 (빈혈, 황달, 당뇨, 피부암)
    - 안구/동공 분석 (인지 장애, 안과 질환)
    - 동작/보행 분석 (파킨슨, 진전증)
    - 정신건강 (우울증, 스트레스, ADHD)
    
    출력: _workspace/camera/01_camera_literature_review.md
    형식: camera-biomarker-reviewer 에이전트 정의의 출력 형식 준수
  "
)
```

완료 조건: `_workspace/camera/01_camera_literature_review.md` 생성 확인

---

## Phase 1.5: 참고문헌 할루시네이션 검증 (reference-hallucination-guard)

Phase 1 완료 직후 자동 실행.

```
# reference-hallucination-guard 스킬 적용
검증 대상: _workspace/camera/01_camera_literature_review.md

실행 순서:
1. 파일에서 모든 참고문헌 추출
2. DOI 직접 확인 (doi.org 접근)
3. Google Scholar / PubMed / IEEE Xplore 제목 검색
4. 결과 분류: ✅ / ⚠️ / ❓ / ❌
5. 검증 보고서 저장: _workspace/camera/reference_validation_report.md
6. 01_camera_literature_review.md에 검증 기호 인라인 추가

❌ 항목 처리:
- 존재 확인 불가 논문은 [UNVERIFIED] 태그 추가
- Phase 2 및 Phase 3에서 해당 항목 제외 권고
```

완료 조건: `_workspace/camera/reference_validation_report.md` 생성 확인

---

## Phase 2: 합성 및 문서화 (camera-biomarker-synthesizer)

```
Agent(
  subagent_type: "camera-biomarker-synthesizer",
  model: "opus",
  prompt: "
    입력 파일:
    - _workspace/camera/01_camera_literature_review.md (문헌 탐색 결과)
    - _workspace/camera/reference_validation_report.md (할루시네이션 검증 결과)
    
    작업:
    1. ✅ 검증된 참고문헌 기반으로 바이오마커 분류·평가
    2. ❌/❓ 항목은 [미검증] 태그 부여 후 Tier 3 이하 배치
    3. Tier 1/2/3 우선순위 평가 (5차원 매트릭스 적용)
    4. 자궁내막증/PCOS 연구(_workspace/01_literature_review.md)와 연계 분석
    
    출력:
    - _workspace/camera/02_camera_synthesis.md
    - _workspace/camera/스마트폰_카메라_바이오마커_합성보고서.docx
    
    .docx 저장: pandoc 우선, 불가 시 python-docx 사용
  "
)
```

완료 조건:
- `_workspace/camera/02_camera_synthesis.md` 생성 확인
- `_workspace/camera/스마트폰_카메라_바이오마커_합성보고서.docx` 생성 확인

---

## Phase 3: IEEE LaTeX 논문 작성 (ieee-paper-writer)

```
Agent(
  subagent_type: "ieee-paper-writer",
  model: "opus",
  prompt: "
    입력 파일:
    - _workspace/camera/01_camera_literature_review.md
    - _workspace/camera/02_camera_synthesis.md
    - _workspace/camera/reference_validation_report.md
    
    논문 유형: IEEE conference 형식 (IEEEtran)
    언어: 영어
    
    논문 주제:
    'Smartphone Camera-Based Digital Biomarker Collection for AI-Driven Disease Prediction: A Systematic Review and Framework'
    
    핵심 contribution:
    1. 스마트폰 카메라 기반 바이오마커의 체계적 분류 프레임워크 제안
    2. 기술 성숙도 × 임상 타당성 × 실용성 3차원 평가 체계
    3. 실생활 적용을 위한 기술적 도전과제 및 해결 방향 제시
    
    참고문헌 처리:
    - reference_validation_report.md의 ✅ 항목만 references.bib에 포함
    - ⚠️ 항목: 포함하되 본문에서 주의 표기
    - ❌ 항목: 제외
    
    출력:
    - _workspace/camera/ieee_paper/main.tex
    - _workspace/camera/ieee_paper/references.bib
    - _workspace/camera/ieee_paper/README.md
  "
)
```

완료 조건:
- `_workspace/camera/ieee_paper/main.tex` 생성 확인
- `_workspace/camera/ieee_paper/references.bib` 생성 확인

---

## 최종 산출물 구조

```
_workspace/camera/
├── 01_camera_literature_review.md      — 문헌 탐색 결과 (검증 기호 포함)
├── reference_validation_report.md      — 참고문헌 할루시네이션 검증 보고서
├── 02_camera_synthesis.md              — 바이오마커 합성 보고서
├── 스마트폰_카메라_바이오마커_합성보고서.docx  — Word 형식 합성 보고서
└── ieee_paper/
    ├── main.tex                        — IEEE LaTeX 논문 본문
    ├── references.bib                  — BibTeX 참고문헌 (검증 완료)
    └── README.md                       — 컴파일 방법 안내
```

---

## 에러 핸들링

| 상황 | 처리 |
|------|------|
| Phase 1 산출물 미생성 | camera-biomarker-reviewer 1회 재실행 |
| Phase 1.5 웹 검색 불가 | 검색 가능 항목만 검증, 나머지 ❓ 처리 후 진행 |
| .docx 생성 실패 | pandoc → python-docx 순서로 재시도, 둘 다 실패 시 .md만 저장 후 보고 |
| Phase 3 LaTeX 구문 오류 | ieee-paper-writer에게 오류 메시지 전달 후 수정 재실행 |
| 참고문헌 ❌ 비율 > 30% | 사용자에게 보고 후 진행 여부 확인 |

---

## 테스트 시나리오

**정상 흐름:**
- 입력: "스마트폰 카메라 바이오마커 연구 파이프라인 실행해줘"
- 기대 출력: `_workspace/camera/` 내 5개 파일/폴더 순차 생성

**재실행 흐름:**
- "논문 Introduction 섹션만 다시 써줘" → Phase 3만 재실행
- "할루시네이션 검증 다시 해줘" → Phase 1.5 → 2 → 3 재실행
