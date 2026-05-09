import pandas as pd, requests, os, re, difflib, time

DIR = "/mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5"
GT_PATH = os.path.join(DIR, "standard_tool_names_ground_truth_v2.csv")
OLLAMA_URL = "http://localhost:11434/api/generate"

MODELS = ["gemma4:e4b", "exaone3.5:7.8b", "gemma3:4b", "deepseek-r1:1.5b"]

BRANDS   = ["보쉬","BOSCH","디월트","DEWALT","아임삭","AIMSAK","마끼다","MAKITA","계양","KEYANG","밀워키","MILWAUKEE","히타치","HIKOKI","히코키","메보","MEBO","세신","TAJIMA","KNIPEX","TOOLSTAR"]
JAPANESE = ["기리","뺀치","빤치","함마","빠루","구루마","니빠","오함마","겐나와","사시가네","란마"]
POWER    = ["유선","충전","무선","에어","배터리","전동","충전식","코드리스","gas","가스","engine","엔진"]
SPECIAL  = [".","&","+","/","?",'"',"!","@","#","%"]
ENG_ABR  = ["L렌치","T렌치","HSS","SDS","PCS","PC","SET","mm","cm","inch","V ","W ","rpm","Ah","LED","USB","AC","DC"]
META_PAT = re.compile(r"^\([^)]*\)|^\d+[\)\.]\s|^\(?\d+,?\d*\)")

def classify(name):
    n = str(name)
    if "?" in n or "▯" in n: return "인코딩 오류"
    if any(k in n for k in ["원)","원/","예약","전화","문의","추가 시","개당"]): return "운영용 텍스트"
    if META_PAT.match(n) or any(k in n for k in ["(불가)","(상자)","(수리)","(고장)"]): return "메타데이터"
    if any(j in n for j in JAPANESE): return "일본어 잔재"
    if any(b.lower() in n.lower() for b in BRANDS): return "브랜드 혼입"
    if any(p in n for p in POWER): return "동력원 명시"
    if any(e.lower() in n.lower() for e in ENG_ABR) or re.search(r"[A-Za-z]{3,}", n): return "영문/약어"
    if any(s in n for s in SPECIAL): return "특수기호"
    if any(k in n for k in ["세트","set","SET","&","＆","구성","키트"]): return "세트/구성품"
    if re.search(r"\d+\s*(mm|cm|m|인치|V|W|A|T|kg|g|호|날|단|개|pc|pcs)", n, re.I): return "속성 기입"
    if "/" in n or ("+" in n and len(n) > 5): return "복합명사"
    if re.search(r"[가-힣]{2,}[가-힣ㄱ-ㅣㅏ-ㅣ]", n) and len(n) <= 15: return "오탈자"
    return "기타"

PROMPT = ("당신은 공구명 표준화 전문가입니다.\n"
          "비표준 공구명을 표준 한국어 공구명으로 변환하세요.\n"
          "반드시 표준 공구명 단어만 출력하고, 다른 설명은 출력하지 마세요.\n\n"
          "공구명: {name}\n표준 공구명:")

def clean_output(text):
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    for p in ["표준 공구명:","표준공구명:","답:","정답:","변환:","→","-"]:
        if text.startswith(p): text = text[len(p):].strip()
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    return lines[0] if lines else text

def find_nearest(output, standard_names):
    s = output.strip()
    if s in standard_names: return s, 1.0
    matches = difflib.get_close_matches(s, standard_names, n=1, cutoff=0.4)
    if matches:
        return matches[0], round(difflib.SequenceMatcher(None, s, matches[0]).ratio(), 3)
    best = max(standard_names, key=lambda x: difflib.SequenceMatcher(None, s, x).ratio())
    return best, round(difflib.SequenceMatcher(None, s, best).ratio(), 3)

def call_ollama(model, prompt):
    try:
        r = requests.post(OLLAMA_URL,
            json={"model": model, "prompt": prompt, "stream": False,
                  "options": {"temperature": 0.0, "num_predict": 32}},
            timeout=90)
        return r.json().get("response", "").strip()
    except Exception as e:
        return f"ERROR:{e}"

gt = pd.read_csv(GT_PATH, encoding="utf-8-sig")
gt.columns = gt.columns.str.strip()
gt = gt[["original_name","standard_name"]].dropna()
gt["dirty_type"] = gt["original_name"].apply(classify)
standard_names = sorted(gt["standard_name"].unique().tolist())
print(f"GT: {len(gt)}건, 표준명 종류: {len(standard_names)}개", flush=True)

for model in MODELS:
    safe = model.replace(":","_").replace(".","_")
    out_path = os.path.join(DIR, f"llm_only_zeroshot_{safe}.csv")
    done_df = pd.read_csv(out_path, encoding="utf-8-sig") if os.path.exists(out_path) else pd.DataFrame()
    done_names = set(done_df["input_name"].tolist()) if not done_df.empty else set()
    remaining = gt[~gt["original_name"].isin(done_names)].reset_index(drop=True)
    print(f"=== {model} | 잔여 {len(remaining)}건 ===", flush=True)
    rows = []; t0 = time.time()
    for i, row in remaining.iterrows():
        raw = call_ollama(model, PROMPT.format(name=row["original_name"]))
        out = clean_output(raw)
        exact = (out.strip() == row["standard_name"].strip())
        near, sim = find_nearest(out, standard_names)
        rows.append({
            "input_name": row["original_name"],
            "standard_name_gt": row["standard_name"],
            "dirty_type": row["dirty_type"],
            "llm_output": out,
            "llm_raw": raw[:300],
            "exact_match": exact,
            "nearest_name": near,
            "nearest_sim": sim,
            "nearest_correct": near.strip() == row["standard_name"].strip()
        })
        if (i+1) % 10 == 0 or (i+1) == len(remaining):
            chunk = pd.DataFrame(rows)
            combined = pd.concat([done_df, chunk], ignore_index=True) if not done_df.empty else chunk
            combined.to_csv(out_path, index=False, encoding="utf-8-sig")
            el = time.time()-t0; rate = (i+1)/el if el>0 else 1
            eta = (len(remaining)-i-1)/rate/60
            print(f"  {i+1:>4}/{len(remaining)} | exact={str(exact):<5} | {repr(out[:15])} | ETA {eta:.1f}분", flush=True)
    final = pd.read_csv(out_path, encoding="utf-8-sig")
    ea = final["exact_match"].mean()*100
    na = final["nearest_correct"].mean()*100
    print(f"[{model}] exact={ea:.2f}%  nearest={na:.2f}%  ({len(final)}건)", flush=True)

print("=== 전체 완료 ===", flush=True)