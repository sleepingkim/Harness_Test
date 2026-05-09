#!/usr/bin/env python3
"""
LLM-only vs RAG 성능 비교 분석
출력: llm_only_vs_rag_comparison.md
"""

import pandas as pd
import os
import re

DIR = r'C:\Users\neohc\Desktop\ClaudeCode\_workspace5'
GT_PATH = os.path.join(DIR, 'standard_tool_names_ground_truth_v2.csv')

# ── 비교 대상 모델 ──────────────────────────────────────────────────────
# (모델명, LLM-only 파일, RAG 파일)
MODELS = [
    ('gemma4:e4b',       'llm_only_zeroshot_gemma4_e4b.csv',         'checkpoint_improved_gemma4_e4b.csv'),
    ('exaone3.5:7.8b',   'llm_only_zeroshot_exaone3_5_7_8b.csv',     'checkpoint_improved_exaone3_5_7_8b.csv'),
    ('gemma3:4b',        'llm_only_zeroshot_gemma3_4b.csv',           'checkpoint_improved_gemma3_4b.csv'),
    ('deepseek-r1:1.5b', 'llm_only_zeroshot_deepseek-r1_1_5b.csv',   'checkpoint_improved_deepseek-r1_1_5b.csv'),
]

TYPE_ORDER = ['동력원 명시','메타데이터','속성 기입','오탈자','브랜드 혼입',
              '세트/구성품','영문/약어','기타','일본어 잔재']

# ── 더티데이터 유형 분류 ──────────────────────────────────────────────
BRANDS   = ['보쉬','BOSCH','디월트','DEWALT','아임삭','AIMSAK','마끼다','MAKITA',
            '계양','KEYANG','밀워키','MILWAUKEE','히타치','HIKOKI','히코키','메보',
            'MEBO','세신','TAJIMA','KNIPEX','TOOLSTAR']
JAPANESE = ['기리','뺀치','빤치','함마','빠루','구루마','니빠','오함마','겐나와','사시가네','란마']
POWER    = ['유선','충전','무선','에어','배터리','전동','충전식','코드리스','gas','가스','engine','엔진']
SPECIAL  = ['.','&','+','/','?','"','!','@','#','%']
ENG_ABR  = ['L렌치','T렌치','HSS','SDS','PCS','PC','SET','mm','cm','inch','V ','W ','rpm','Ah','LED','USB','AC','DC']
META_PAT = re.compile(r'^\([^)]*\)|^\d+[\)\.]\s|^\(?\d+,?\d*\)')

def classify(name):
    n = str(name)
    if '?' in n or '▯' in n:                                               return '인코딩 오류'
    if any(k in n for k in ['원)','원/','예약','전화','문의','추가 시','개당']): return '운영용 텍스트'
    if META_PAT.match(n) or any(k in n for k in ['(불가)','(상자)','(수리)','(고장)']): return '메타데이터'
    if any(j in n for j in JAPANESE):                                       return '일본어 잔재'
    if any(b.lower() in n.lower() for b in BRANDS):                        return '브랜드 혼입'
    if any(p in n for p in POWER):                                          return '동력원 명시'
    if any(e.lower() in n.lower() for e in ENG_ABR) or re.search(r'[A-Za-z]{3,}', n): return '영문/약어'
    if any(s in n for s in SPECIAL):                                        return '특수기호'
    if any(k in n for k in ['세트','set','SET','&','＆','구성','키트']):    return '세트/구성품'
    if re.search(r'\d+\s*(mm|cm|m|인치|V|W|A|T|kg|g|호|날|단|개|pc|pcs)', n, re.I): return '속성 기입'
    if '/' in n or ('+' in n and len(n) > 5):                              return '복합명사'
    if re.search(r'[가-힣]{2,}[가-힣ㄱ-ㅣㅏ-ㅣ]', n) and len(n) <= 15:  return '오탈자'
    return '기타'

def load_rag(fpath, gt):
    """RAG 체크포인트 → GT와 병합 → 정확도 반환"""
    try:
        ck = pd.read_csv(fpath, encoding='utf-8-sig', low_memory=False)
    except Exception:
        ck = pd.read_csv(fpath, encoding='cp949', low_memory=False)
    ck.columns = ck.columns.str.strip()
    if 'Input_Name' in ck.columns:
        ck = ck.rename(columns={'Input_Name': 'input_name'})
    ck = ck[['input_name', 'standard_name']].dropna()
    merged = gt.merge(ck, left_on='original_name', right_on='input_name', how='inner',
                      suffixes=('_gt', '_pred'))
    merged['correct'] = merged['standard_name_gt'].str.strip() == merged['standard_name_pred'].str.strip()
    return merged

def load_llm_only(fpath):
    """LLM-only zero-shot 결과 로드"""
    df = pd.read_csv(fpath, encoding='utf-8-sig')
    return df

def type_acc(df, correct_col, dtype_col='dirty_type'):
    """유형별 정확도 딕셔너리 반환"""
    grp = df.groupby(dtype_col)[correct_col].agg(['sum','count'])
    return {t: (row['sum']/row['count']*100, int(row['sum']), int(row['count']))
            for t, row in grp.iterrows()}

def main():
    gt = pd.read_csv(GT_PATH, encoding='utf-8-sig')
    gt.columns = gt.columns.str.strip()
    gt = gt[['original_name','standard_name']].dropna()
    gt['dirty_type'] = gt['original_name'].apply(classify)

    # ── 결과 수집 ────────────────────────────────────────────────────────
    results = {}
    for mname, llm_file, rag_file in MODELS:
        llm_path = os.path.join(DIR, llm_file)
        rag_path = os.path.join(DIR, rag_file)

        entry = {'llm': None, 'rag': None}

        if os.path.exists(llm_path):
            llm_df = load_llm_only(llm_path)
            # GT와 inner join (평가 기반 통일)
            merged_llm = gt.merge(llm_df, left_on='original_name', right_on='input_name', how='inner')
            merged_llm['correct_exact']   = merged_llm['exact_match'].astype(bool)
            merged_llm['correct_nearest'] = merged_llm['nearest_correct'].astype(bool)
            merged_llm['dirty_type_use']  = merged_llm['dirty_type_x'] if 'dirty_type_x' in merged_llm.columns else merged_llm['dirty_type']
            entry['llm'] = merged_llm
        else:
            print(f'[경고] LLM-only 파일 없음: {llm_file}')

        if os.path.exists(rag_path):
            rag_merged = load_rag(rag_path, gt)
            entry['rag'] = rag_merged
        else:
            print(f'[경고] RAG 파일 없음: {rag_file}')

        results[mname] = entry

    # ── 마크다운 문서 생성 ────────────────────────────────────────────────
    lines = []
    lines.append('# LLM-only vs RAG 성능 비교 분석')
    lines.append('')
    lines.append('> **작성 기준:** 2026-05-09  ')
    lines.append('> **평가 기반:** standard_tool_names_ground_truth_v2.csv (457쌍)  ')
    lines.append('> **LLM-only 방식:** Zero-shot (표준명 후보 미제공, 자유 생성)')
    lines.append('> **RAG 방식:** BGE-m3-ko + BM25(40%)/FAISS(60%) hybrid, k=15, 카테고리 주입')
    lines.append('')
    lines.append('---')
    lines.append('')

    # 1. 전체 정확도 비교
    lines.append('## 1. 전체 정확도 비교')
    lines.append('')
    lines.append('| 모델 | LLM-only (exact) | LLM-only (nearest) | RAG v2 Improved | RAG 기여 (+pp) |')
    lines.append('|------|:----------------:|:------------------:|:---------------:|:--------------:|')

    for mname, entry in results.items():
        llm_exact = llm_near = rag_acc = '—'
        delta = '—'
        if entry['llm'] is not None:
            df = entry['llm']
            n = len(df)
            e = df['correct_exact'].mean() * 100
            nr = df['correct_nearest'].mean() * 100
            llm_exact = f'{e:.1f}% ({int(df["correct_exact"].sum())}/{n})'
            llm_near  = f'{nr:.1f}%'
        if entry['rag'] is not None:
            df = entry['rag']
            n = len(df)
            r = df['correct'].mean() * 100
            rag_acc = f'{r:.1f}% ({int(df["correct"].sum())}/{n})'
            if entry['llm'] is not None:
                e_val = entry['llm']['correct_exact'].mean() * 100
                delta = f'+{r - e_val:.1f}pp'
        lines.append(f'| **{mname}** | {llm_exact} | {llm_near} | {rag_acc} | {delta} |')

    lines.append('')
    lines.append('> **exact**: LLM 출력이 정답 표준명과 완전 일치  ')
    lines.append('> **nearest**: LLM 출력을 표준명 리스트에서 가장 가까운 것으로 매핑 후 일치 여부')
    lines.append('')
    lines.append('---')
    lines.append('')

    # 2. 유형별 비교 (gemma4:e4b 기준)
    lines.append('## 2. 더티데이터 유형별 비교 (gemma4:e4b 기준)')
    lines.append('')
    lines.append('| 유형 | GT 건수 | LLM-only (exact) | RAG v2 Improved | 차이 |')
    lines.append('|------|:-------:|:----------------:|:---------------:|:----:|')

    main_model = 'gemma4:e4b'
    entry = results.get(main_model, {})
    gt_dist = gt['dirty_type'].value_counts()

    if entry.get('llm') is not None and entry.get('rag') is not None:
        llm_by_type = type_acc(entry['llm'], 'correct_exact',
                               dtype_col='dirty_type_use' if 'dirty_type_use' in entry['llm'].columns else 'dirty_type')
        rag_by_type = type_acc(entry['rag'], 'correct', dtype_col='dirty_type')

        for t in TYPE_ORDER:
            n_gt = int(gt_dist.get(t, 0))
            if t in llm_by_type:
                la, lc, ln = llm_by_type[t]
                llm_str = f'{la:.1f}% ({lc}/{ln})'
            else:
                llm_str = '—'
            if t in rag_by_type:
                ra, rc, rn = rag_by_type[t]
                rag_str = f'{ra:.1f}% ({rc}/{rn})'
            else:
                rag_str = '—'
            if t in llm_by_type and t in rag_by_type:
                diff = rag_by_type[t][0] - llm_by_type[t][0]
                diff_str = f'+{diff:.1f}pp' if diff >= 0 else f'{diff:.1f}pp'
            else:
                diff_str = '—'
            lines.append(f'| {t} | {n_gt} | {llm_str} | {rag_str} | {diff_str} |')
    else:
        lines.append('| (데이터 미완료) | — | — | — | — |')

    lines.append('')
    lines.append('---')
    lines.append('')

    # 3. 유형별 비교 전체 모델 (LLM-only exact)
    lines.append('## 3. 모델별 LLM-only 전체 정확도 vs RAG 정확도')
    lines.append('')
    lines.append('```')
    lines.append(f'{"모델":<22} {"LLM-only":>10} {"RAG":>10} {"RAG 기여":>10}')
    lines.append('-' * 55)
    for mname, entry in results.items():
        llm_v = entry['llm']['correct_exact'].mean()*100 if entry['llm'] is not None else float('nan')
        rag_v = entry['rag']['correct'].mean()*100 if entry['rag'] is not None else float('nan')
        delta = rag_v - llm_v if (entry['llm'] is not None and entry['rag'] is not None) else float('nan')
        llm_s = f'{llm_v:.1f}%' if entry['llm'] is not None else '—'
        rag_s = f'{rag_v:.1f}%' if entry['rag'] is not None else '—'
        d_s   = f'+{delta:.1f}pp' if delta > 0 else (f'{delta:.1f}pp' if not pd.isna(delta) else '—')
        lines.append(f'{mname:<22} {llm_s:>10} {rag_s:>10} {d_s:>10}')
    lines.append('```')
    lines.append('')
    lines.append('---')
    lines.append('')

    # 4. 주요 오답 사례 (gemma4:e4b, LLM-only)
    lines.append('## 4. LLM-only 주요 오답 사례 (gemma4:e4b)')
    lines.append('')
    entry = results.get('gemma4:e4b', {})
    if entry.get('llm') is not None:
        df = entry['llm']
        wrong = df[~df['correct_exact']].copy()
        # 유형별로 대표 사례 1~2건씩
        lines.append('| 더티데이터 유형 | 원본 공구명 | 정답 표준명 | LLM 출력 |')
        lines.append('|------|------|------|------|')
        dtype_col = 'dirty_type_use' if 'dirty_type_use' in wrong.columns else 'dirty_type'
        for t in TYPE_ORDER:
            subset = wrong[wrong[dtype_col] == t].head(2)
            for _, r in subset.iterrows():
                orig = r['input_name']
                gt_n = r['standard_name_gt']
                out  = r.get('llm_output', '—')
                lines.append(f'| {t} | {orig} | {gt_n} | {out} |')
    else:
        lines.append('_(데이터 미완료)_')

    lines.append('')
    lines.append('---')
    lines.append('')

    # 5. 해석
    lines.append('## 5. 해석 및 시사점')
    lines.append('')
    lines.append('### 5.1 RAG 기여도 해석')
    lines.append('')
    lines.append('| 구간 | 해석 |')
    lines.append('|------|------|')
    lines.append('| RAG 기여 +20pp 이상 | RAG가 핵심. LLM 단독으로는 실용 불가 |')
    lines.append('| RAG 기여 +10~20pp  | RAG가 중요한 정밀도 보완 역할 |')
    lines.append('| RAG 기여 +5~10pp   | RAG 효과 있으나 LLM 자체도 상당한 수준 |')
    lines.append('| RAG 기여 +5pp 미만  | LLM 고유 지식이 충분. RAG의 한계 구간 존재 가능 |')
    lines.append('')
    lines.append('### 5.2 일본어 잔재 유형 특이 분석')
    lines.append('')
    lines.append('일본어 잔재 유형은 RAG 적용 후 정확도가 47.1%에 불과하다. ')
    lines.append('LLM-only 결과와 비교하면 다음 중 하나가 확인될 것이다:')
    lines.append('')
    lines.append('- **LLM-only > RAG**: BGE-m3-ko가 일본어 공구명 임베딩을 실패하여 RAG가 역효과')
    lines.append('- **LLM-only ≈ RAG**: LLM 자체의 지식 한계가 근본 원인')
    lines.append('- **LLM-only < RAG**: RAG가 어느 정도 보완했으나 둘 다 낮음')
    lines.append('')
    lines.append('이 결과에 따라 일본어 잔재 유형의 해결 방향(사전 선처리 vs 임베딩 개선 vs 더 큰 LLM)이 결정된다.')
    lines.append('')
    lines.append('### 5.3 nearest_match vs exact_match 괴리 해석')
    lines.append('')
    lines.append('nearest_match와 exact_match의 차이가 클수록, LLM이 개념은 알고 있으나 표기가 다르게 나온다는 뜻이다.')
    lines.append('이 경우 후처리 매핑 레이어를 추가하면 LLM-only 방식도 실용적일 수 있다.')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## 6. 결론')
    lines.append('')
    lines.append('_(실험 완료 후 수치 기반으로 작성 필요)_')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('**관련 파일:**')
    for mname, llm_file, _ in MODELS:
        safe = mname.replace(':', '_').replace('.', '_')
        lines.append(f'- `llm_only_zeroshot_{safe}.csv` — {mname} LLM-only 결과')
    lines.append('- `dirty_type_analysis_report.md` — RAG v2 유형별 분석')
    lines.append('- `llm_only_evaluation_rationale.md` — LLM-only 필요성 근거')

    # 저장
    out_md = os.path.join(DIR, 'llm_only_vs_rag_comparison.md')
    with open(out_md, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'저장 완료: {out_md}')

if __name__ == '__main__':
    main()
