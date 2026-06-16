# 현장연구보고서 LaTeX 빌드 안내

- **파일**: [`main.tex`](main.tex) — 단일 자체완결 파일(참고문헌 `thebibliography` 내장, 별도 `.bib` 불필요)
- **저자**: 신홍철 (Hongchul Shin), KIST

## 컴파일 방법 (한글 포함 → XeLaTeX 권장)

한글이 포함되어 있어 `kotex` 패키지를 사용합니다. **XeLaTeX 또는 LuaLaTeX**를 권장합니다.

```bash
# 권장
xelatex main.tex
xelatex main.tex      # 목차·상호참조(\ref, \cite) 갱신을 위해 2회 실행

# 또는
lualatex main.tex
lualatex main.tex
```

상호참조(표 번호, 인용 [n])가 처음엔 `??`로 보일 수 있으므로 **반드시 2회 컴파일**하세요.

## Overleaf 사용 시

1. [overleaf.com](https://www.overleaf.com)에서 새 프로젝트 → `main.tex` 업로드
2. 좌측 상단 **Menu → Compiler 를 `XeLaTeX`** 로 변경
3. Recompile

## 로컬 환경 설치 (선택)

- **Windows**: [MiKTeX](https://miktex.org/) 또는 [TeX Live](https://tug.org/texlive/) 설치 시 `xelatex`·`kotex` 포함
- 폰트: kotex 기본 나눔/은 글꼴 사용. 시스템에 한글 폰트가 없으면 `\setmainhangulfont{...}`로 지정 가능

## 비고

- `pdflatex`로도 kotex가 대부분 처리하나, 일부 유니코드 기호·폰트 이슈를 피하려면 XeLaTeX를 사용하세요.
- 본 `.tex`는 원본 마크다운 보고서([`../현장연구보고서_PCOS_디지털바이오마커.md`](../현장연구보고서_PCOS_디지털바이오마커.md))와 내용이 동일하며, 논문(IMRaD) 형식으로 재구성한 것입니다.
