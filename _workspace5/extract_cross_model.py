#!/usr/bin/env python3
import pandas as pd, os, re, numpy as np

DIR = r'C:\Users\neohc\Desktop\ClaudeCode\_workspace5'
GT_PATH = os.path.join(DIR, 'standard_tool_names_ground_truth_v2.csv')

BRANDS = ['보쉬','BOSCH','디월트','DEWALT','아임삭','AIMSAK','마끼다','MAKITA','계양','KEYANG',
          '밀워키','MILWAUKEE','히타치','HIKOKI','히코키','메보','MEBO','세신','TAJIMA','KNIPEX','TOOLSTAR']
JAPANESE = ['기리','뺀치','빤치','함마','빠루','구루마','니빠','오함마','겐나와','사시가네','란마']
POWER = ['유선','충전','무선','에어','배터리','전동','충전식','코드리스','gas','가스','engine','엔진']
SPECIAL = ['.','&','+','/','?','"','!','@','#','%']
ENG_ABR = ['L렌치','T렌치','HSS','SDS','PCS','PC','SET','mm','cm','inch','V ','W ','rpm','Ah','LED','USB','AC','DC']
META_PAT = re.compile(r'^\([^)]*\)|^\d+[\)\.]\s|^\(?\d+,?\d*\)')

def classify(name):
    n = str(name)
    if '?' in n or '▯' in n: return '인코딩 오류'
    if any(k in n for k in ['원)','원/','예약','전화','문의','추가 시','개당']): return '운영용 텍스트'
    if META_PAT.match(n) or any(k in n for k in ['(불가)','(상자)','(수리)','(고장)']): return '메타데이터'
    if any(j in n for j in JAPANESE): return '일본어 잔재'
    if any(b.lower() in n.lower() for b in BRANDS): return '브랜드 혼입'
    if any(p in n for p in POWER): return '동력원 명시'
    if any(e.lower() in n.lower() for e in ENG_ABR) or re.search(r'[A-Za-z]{3,}', n): return '영문/약어'
    if any(s in n for s in SPECIAL): return '특수기호'
    if any(k in n for k in ['세트','set','SET','&','＆','구성','키트']): return '세트/구성품'
    if re.search(r'\d+\s*(mm|cm|m|인치|V|W|A|T|kg|g|호|날|단|개|pc|pcs)', n, re.I): return '속성 기입'
    if '/' in n or ('+' in n and len(n) > 5): return '복합명사'
    if re.search(r'[가-힣]{2,}[가-힣ㄱ-ㅣㅏ-ㅣ]', n) and len(n) <= 15: return '오탈자'
    return '기타'

gt = pd.read_csv(GT_PATH, encoding='utf-8-sig')
gt.columns = gt.columns.str.strip()
gt = gt[['original_name','standard_name']].dropna()
gt['dirty_type'] = gt['original_name'].apply(classify)

MODELS = [
    ('gemma4:e4b',       'checkpoint_improved_gemma4_e4b.csv'),
    ('gemma3:4b',        'checkpoint_improved_gemma3_4b.csv'),
    ('granite4.1:8b',    'New_RAG_v2_improved_granite4_1_8b_3352.csv'),
    ('gemma4:e2b',       'checkpoint_improved_gemma4_e2b.csv'),
    ('exaone3.5:7.8b',   'checkpoint_improved_exaone3_5_7_8b.csv'),
    ('deepseek-r1:8b',   'New_RAG_v2_improved_deepseek-r1_8b_3352.csv'),
    ('deepseek-r1:1.5b', 'checkpoint_improved_deepseek-r1_1_5b.csv'),
    ('exaone3.5:2.4b',   'checkpoint_improved_exaone3_5_2_4b.csv'),
    ('granite4.1:3b',    'checkpoint_improved_granite4_1_3b.csv'),
]

TYPE_ORDER = ['동력원 명시','메타데이터','속성 기입','오탈자','브랜드 혼입',
              '세트/구성품','영문/약어','기타','일본어 잔재']

results = {}
overall = {}
for mname, fname in MODELS:
    fpath = os.path.join(DIR, fname)
    if not os.path.exists(fpath): continue
    try:
        ck = pd.read_csv(fpath, encoding='utf-8-sig', low_memory=False)
    except Exception:
        ck = pd.read_csv(fpath, encoding='cp949', low_memory=False)
    ck.columns = ck.columns.str.strip()
    if 'Input_Name' in ck.columns:
        ck = ck.rename(columns={'Input_Name':'input_name'})
    ck = ck[['input_name','standard_name']].dropna()
    merged = gt.merge(ck, left_on='original_name', right_on='input_name', how='inner',
                      suffixes=('_gt','_pred'))
    merged['correct'] = merged['standard_name_gt'].str.strip() == merged['standard_name_pred'].str.strip()
    overall[mname] = (merged['correct'].mean()*100, int(merged['correct'].sum()), len(merged))
    grp = merged.groupby('dirty_type').agg(correct=('correct','sum'), total=('correct','count')).reset_index()
    grp['acc'] = grp['correct'] / grp['total'] * 100
    results[mname] = {r['dirty_type']: (r['acc'], int(r['correct']), int(r['total'])) for _, r in grp.iterrows()}

print('=== GT 유형 분포 ===')
dist = gt['dirty_type'].value_counts()
for t, c in dist.items():
    print(f'  {t:<15} {c:>4}건  ({c/len(gt)*100:.1f}%)')
print(f'  총계            {len(gt):>4}건')

print()
print('=== 전체 모델 정확도 ===')
for m,(a,c,n) in overall.items():
    print(f'  {m:<20} {a:.2f}%  ({c}/{n})')

print()
print('=== 유형별 × 모델별 정확도 (정확도%) ===')
model_names = list(results.keys())
print(f'{"유형":<14}', end='')
for m in model_names:
    short = m.replace('exaone3.5','ex').replace('deepseek-r1','ds').replace('granite4.1','gn')
    print(f'{short:>13}', end='')
print()
print('-'*(14 + 13*len(model_names)))
for t in TYPE_ORDER:
    n_gt = int(dist.get(t, 0))
    print(f'{t:<14}', end='')
    for m in model_names:
        if t in results[m]:
            a, c, n = results[m][t]
            print(f'  {a:5.1f}({n:>2})', end='')
        else:
            print(f'  {"—":>8}   ', end='')
    print()

print()
print('=== 유형별 상세 (gemma4:e4b 기준, 오답 사례 있는 유형) ===')
best = 'gemma4:e4b'
for t in TYPE_ORDER:
    if t in results[best]:
        a, c, n = results[best][t]
        fail = n - c
        print(f'  {t:<15}  정확도 {a:5.1f}%  ({c}/{n}, 오답 {fail}건)')
