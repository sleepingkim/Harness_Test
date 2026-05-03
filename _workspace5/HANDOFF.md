# 공구 이름 표준화 LLM 프로젝트 — 핸드오프 문서

> 이 문서를 읽으면 현재까지의 작업 맥락과 다음 단계를 즉시 파악할 수 있습니다.
> Claude Code에서 "HANDOFF.md를 읽고 이어서 진행해줘"라고 말하면 됩니다.

---

## 1. 프로젝트 목표

서울시 공구대여 데이터의 **비정형 공구 이름**(3,289개 고유명)을 오픈소스 LLM이 표준화된 형태로 분류할 수 있도록:
1. ✅ 정답지(Ground Truth) 데이터 구축
2. ⬜ RAG 벡터DB 구축 (정답지 임베딩)
3. ⬜ 오픈소스 LLM으로 더티데이터 정제 실행
4. ⬜ 분류 정확도(Accuracy) + 생성 시간(Cost) 측정
5. ⬜ 트레이드오프 분석 및 최적 모델 선정

---

## 2. 완료된 작업 (2026-05-03)

### 2-1. 프렉티컴보고서 분석
- 이전 연구(1년 전)의 방법론 파악 완료
- RAG 방식이 Few-Shot 대비 압도적 (97.88% vs 39.17%)
- 11개 오픈소스 모델 비교 (Llama, Gemma, Exaone, Deepseek)
- 최적 모델: Gemma3:1b (속도↑정확도↑), EXAONE-4.0-1.2B (균형)

### 2-2. 정답지 데이터 V2 구축
- **파일**: `standard_tool_names_ground_truth_v2.csv` (457개 엔트리)
- **구조** (6칼럼):

| 칼럼 | 설명 | 규칙 |
|------|------|------|
| original_name | 원본 더티데이터 그대로 | 서울시 CSV의 공구이름 or 표준 레퍼런스명 |
| standard_name | 정제된 표준 공구명 | 기능적 표준명으로 통일 |
| brand | 브랜드 | **original_name에서 직접 읽을 수 있을 때만** 기입 |
| power_source | 동력원 | 유선/충전식(무선)/에어/수동/배터리/가스 |
| specification | 규격 | mm, 인치, V, W, PCS, 모델번호 등 |
| usage_note | 용도/특성 | 세트, 접이식, 가정용, 콘크리트용, 소모품 등 |

### 2-3. 명칭 통일 규칙 (적용됨)
| 비표준/동의어 | → 표준명 | 이유 |
|--------------|----------|------|
| 해머, 함마, 햄머 | 망치 | 카탈로그 기준 수공구=망치 |
| 랜턴, 후레쉬 | 손전등 | 동일 공구, 표준어 통일 |
| 기리 | 드릴비트 | 일본어 잔재 순화 |
| 뺀치, 빤치 | 펜치 | 일본어 잔재 순화 |
| 헤라 | 스크레퍼 | 동일 공구 |
| 강력절단기 | 볼트컷터 | 동일 공구 |
| 셋트, 센트 | 세트 | 오표기 |
| 렌지 | 렌치 | 오표기 |
| 갓다 | 커터 | 일본어 잔재 |

**주의**: `해머드릴`은 전동공구 복합어이므로 "해머드릴" 유지 (망치드릴로 바꾸지 않음)

---

## 3. 파일 구조

```
_workspace5/
├── 서울시 대여 공구 찾기 정보.csv              ← 원본 (CP949 인코딩, 11,525행)
├── 공구 카탈로그_sangbo.pdf                   ← 상보 종합카탈로그
├── 프렉티컴보고서_최종본.pdf                  ← 1차 연구 보고서
├── 프렉티컴보고서.txt                         ← PDF→TXT (2,714줄)
├── 공구카탈로그.txt                           ← PDF→TXT (248,510줄)
├── standard_tool_names_ground_truth_v2.csv    ← ★ 정답지 (457개)
├── standard_tool_names_ground_truth.csv       ← (v1, 폐기됨)
├── 참고자료_정리.md                           ← 참고자료 출처/경로 정리
└── HANDOFF.md                                 ← 이 문서
```

---

## 4. 다음 단계 (이 컴퓨터에서 진행)

### Step 1: 환경 구축
```bash
# Ollama 설치 (LLM 로컬 실행)
# Python 3.9+ 환경
pip install sentence-transformers faiss-cpu pandas
```

### Step 2: RAG 벡터DB 구축
- `standard_tool_names_ground_truth_v2.csv`를 임베딩
- 모델: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- FAISS 벡터DB 저장

### Step 3: LLM 프롬프트 설계
- 입력: 더티 공구이름 1개
- 출력: JSON `{standard_name, brand, power_source, specification, usage_note}`
- RAG에서 유사 사례 3개 검색하여 프롬프트에 주입

### Step 4: 모델 실행 및 측정
- 대상 모델 (이전 연구 기준):
  - Gemma3:1b, Gemma3:4b
  - EXAONE-4.0-1.2B, EXAONE-Deep-2.4B, EXAONE-Deep-7.8B
  - Llama-3.2-Korean-3B
  - Deepseek-r1:1.5b
- 측정 항목: 정확도(%), 코사인유사도, 총 생성시간(sec)

### Step 5: 결과 분석
- Trade-Off Score = α × 정확도 - (1-α) × 비용
- α = 0.25(속도), 0.5(균형), 0.75(정확도)

---

## 5. 핵심 기술 사양 (이전 연구 참고)

| 항목 | 값 |
|------|-----|
| Python | 3.9.13 |
| LLM 런타임 | Ollama |
| 임베딩 모델 | paraphrase-multilingual-MiniLM-L12-v2 |
| 벡터DB | FAISS |
| RAG 유사 사례 수 | 3개 |
| 대상 데이터 | 3,289개 고유 공구명 (중복 제거) |
| CSV 인코딩 | CP949 (원본), UTF-8-sig (정답지) |

---

## 6. 원본 데이터 읽기 코드

```python
import csv

# 서울시 데이터 읽기
with open('서울시 대여 공구 찾기 정보.csv', 'r', encoding='cp949') as f:
    reader = csv.reader(f)
    header = next(reader)  # 28개 칼럼
    for row in reader:
        tool_name = row[5].strip()  # '공구 이름' 칼럼 (index 5)

# 정답지 읽기
with open('standard_tool_names_ground_truth_v2.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    header = next(reader)  # original_name, standard_name, brand, power_source, specification, usage_note
    for row in reader:
        original, standard, brand, power, spec, usage = row
```

---

## 7. 주의사항
- 원본 CSV는 **CP949** 인코딩 (utf-8 아님)
- brand 칼럼은 **original_name에서 직접 읽을 수 있는 경우만** 기입
- 정답지에 없는 공구가 원본에 있을 수 있음 (정답지 457개 < 고유명 3,289개)
- 정답지는 RAG 참고 맥락이지, 1:1 매핑표가 아님
