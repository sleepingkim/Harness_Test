#!/usr/bin/env python3
"""
LLM-only Zero-shot 공구명 표준화 실험
RAG 없이 LLM 자체 지식만으로 표준화 성능 측정

대상 모델: gemma4:e4b, exaone3.5:7.8b, gemma3:4b, deepseek-r1:1.5b
평가 기반: standard_tool_names_ground_truth_v2.csv (457쌍)
출력 파일: llm_only_zeroshot_{model}.csv
"""

import pandas as pd
import requests
import os
import re
import difflib
import time

DIR = r'C:\Users\neohc\Desktop\ClaudeCode\_workspace5'
GT_PATH = os.path.join(DIR, 'standard_tool_names_ground_truth_v2.csv')
OLLAMA_URL = 'http://localhost:11434/api/generate'

MODELS = [
    'gemma4:e4b',
    'exaone3.5:7.8b',
    'gemma3:4b',
    'deepseek-r1:1.5b',
]

# ── 더티데이터 유형 분류 (analyze_by_type.py 동일 로직) ──────────────────
BRANDS   = ['보쉬','BOSCH','디월트','DEWALT','아임삭','AIMSAK','마끼다','MAKITA',
            '계양','KEYANG','밀워키','MILWAUKEE','히타치','HIKOKI','히코키','메보',
            'MEBO','세신','TAJIMA','KNIPEX','TOOLSTAR']
JAPANESE = ['기리','뺀치','빤치','함마','빠루','구루마','니빠','오함마','겐나와',
            '사시가네','란마']
POWER    = ['유선','충전','무선','에어','배터리','전동','충전식','코드리스',
            'gas','가스','engine','엔진']
SPECIAL  = ['.','&','+','/','?','"','!','@','#','%']
ENG_ABR  = ['L렌치','T렌치','HSS','SDS','PCS','PC','SET','mm','cm','inch',
            'V ','W ','rpm','Ah','LED','USB','AC','DC']
META_PAT = re.compile(r'^\([^)]*\)|^\d+[\)\.]\s|^\(?\d+,?\d*\)')

def classify(name):
    n = str(name)
    if '?' in n or '▯' in n:                                          return '인코딩 오류'
    if any(k in n for k in ['원)','원/','예약','전화','문의','추가 시','개당']): return '운영용 텍스트'
    if META_PAT.match(n) or any(k in n for k in ['(불가)','(상자)','(수리)','(고장)']): return '메타데이터'
    if any(j in n for j in JAPANESE):                                  return '일본어 잔재'
    if any(b.lower() in n.lower() for b in BRANDS):                   return '브랜드 혼입'
    if any(p in n for p in POWER):                                     return '동력원 명시'
    if any(e.lower() in n.lower() for e in ENG_ABR) or re.search(r'[A-Za-z]{3,}', n): return '영문/약어'
    if any(s in n for s in SPECIAL):                                   return '특수기호'
    if any(k in n for k in ['세트','set','SET','&','＆','구성','키트']): return '세트/구성품'
    if re.search(r'\d+\s*(mm|cm|m|인치|V|W|A|T|kg|g|호|날|단|개|pc|pcs)', n, re.I): return '속성 기입'
    if '/' in n or ('+' in n and len(n) > 5):                         return '복합명사'
    if re.search(r'[가-힣]{2,}[가-힣ㄱ-ㅣㅏ-ㅣ]', n) and len(n) <= 15: return '오탈자'
    return '기타'

# ── 프롬프트 ──────────────────────────────────────────────────────────────
PROMPT_TEMPLATE = """당신은 공구명 표준화 전문가입니다.
비표준 공구명을 표준 한국어 공구명으로 변환하세요.
반드시 표준 공구명 단어만 출력하고, 다른 설명은 출력하지 마세요.

공구명: {name}
표준 공구명:"""

# ── 유틸리티 함수 ─────────────────────────────────────────────────────────
def clean_output(text: str) -> str:
    """LLM 원시 출력에서 표준 공구명만 추출"""
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    text = text.strip()
    for prefix in ['표준 공구명:', '표준공구명:', '답:', '정답:', '변환:', '→', '-']:
        if text.startswith(prefix):
            text = text[len(prefix):].strip()
    # 첫 번째 비어있지 않은 줄만 취함
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    return lines[0] if lines else text

def find_nearest(output: str, standard_names: list) -> tuple:
    """가장 유사한 표준명과 유사도 반환"""
    s = output.strip()
    if s in standard_names:
        return s, 1.0
    matches = difflib.get_close_matches(s, standard_names, n=1, cutoff=0.4)
    if matches:
        ratio = difflib.SequenceMatcher(None, s, matches[0]).ratio()
        return matches[0], round(ratio, 3)
    best = max(standard_names, key=lambda x: difflib.SequenceMatcher(None, s, x).ratio())
    ratio = difflib.SequenceMatcher(None, s, best).ratio()
    return best, round(ratio, 3)

def call_ollama(model: str, prompt: str, timeout: int = 90) -> str:
    """Ollama generate API 호출"""
    try:
        resp = requests.post(
            OLLAMA_URL,
            json={'model': model, 'prompt': prompt, 'stream': False,
                  'options': {'temperature': 0.0, 'num_predict': 32}},
            timeout=timeout
        )
        resp.raise_for_status()
        return resp.json().get('response', '').strip()
    except requests.exceptions.Timeout:
        return 'ERROR:TIMEOUT'
    except Exception as e:
        return f'ERROR:{e}'

# ── 메인 ─────────────────────────────────────────────────────────────────
def main():
    # GT 로드
    gt = pd.read_csv(GT_PATH, encoding='utf-8-sig')
    gt.columns = gt.columns.str.strip()
    gt = gt[['original_name', 'standard_name']].dropna()
    gt['dirty_type'] = gt['original_name'].apply(classify)
    standard_names = sorted(gt['standard_name'].unique().tolist())
    print(f'GT 로드: {len(gt)}건, 표준명 종류: {len(standard_names)}개\n')

    for model in MODELS:
        safe = model.replace(':', '_').replace('.', '_')
        out_path = os.path.join(DIR, f'llm_only_zeroshot_{safe}.csv')

        # 체크포인트 로드 (재개)
        if os.path.exists(out_path):
            done_df = pd.read_csv(out_path, encoding='utf-8-sig')
            done_names = set(done_df['input_name'].tolist())
            print(f'[{model}] 체크포인트 발견: {len(done_names)}건 완료, 재개합니다.')
        else:
            done_df = pd.DataFrame()
            done_names = set()

        remaining = gt[~gt['original_name'].isin(done_names)].reset_index(drop=True)
        total = len(remaining)
        print(f'[{model}] 처리 예정: {total}건')

        rows = []
        t0 = time.time()

        for i, row in remaining.iterrows():
            name     = row['original_name']
            gt_name  = row['standard_name']
            dtype    = row['dirty_type']

            prompt   = PROMPT_TEMPLATE.format(name=name)
            raw      = call_ollama(model, prompt)
            output   = clean_output(raw)

            exact    = (output.strip() == gt_name.strip())
            nearest, sim = find_nearest(output, standard_names)
            nearest_ok   = (nearest.strip() == gt_name.strip())

            rows.append({
                'input_name':        name,
                'standard_name_gt':  gt_name,
                'dirty_type':        dtype,
                'llm_output':        output,
                'llm_raw':           raw[:300],
                'exact_match':       exact,
                'nearest_name':      nearest,
                'nearest_sim':       sim,
                'nearest_correct':   nearest_ok,
            })

            # 10건마다 저장
            if (i + 1) % 10 == 0 or (i + 1) == total:
                chunk = pd.DataFrame(rows)
                combined = pd.concat([done_df, chunk], ignore_index=True) if not done_df.empty else chunk
                combined.to_csv(out_path, index=False, encoding='utf-8-sig')
                elapsed = time.time() - t0
                rate = (i + 1) / elapsed if elapsed > 0 else 0
                eta  = (total - i - 1) / rate if rate > 0 else 0
                print(f'  {i+1:>4}/{total}  exact={exact}  output="{output[:20]}"  '
                      f'ETA {eta/60:.1f}분')

        # 최종 결과 출력
        final = pd.read_csv(out_path, encoding='utf-8-sig')
        n = len(final)
        ea = final['exact_match'].mean() * 100
        na = final['nearest_correct'].mean() * 100
        print(f'\n[{model}] 완료')
        print(f'  exact_match   : {ea:.2f}%  ({int(final["exact_match"].sum())}/{n})')
        print(f'  nearest_match : {na:.2f}%  ({int(final["nearest_correct"].sum())}/{n})')
        print(f'  저장: {out_path}\n')
        print('-' * 60)

    print('\n=== 전체 실험 완료 ===')
    print('다음 단계: python analyze_llm_only.py 실행')

if __name__ == '__main__':
    main()
