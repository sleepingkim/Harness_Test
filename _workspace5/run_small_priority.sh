#!/usr/bin/env bash
# 소형 모델 4개 우선 실행 (improved only, 용량 작은 순)
# deepseek-r1:1.5b → exaone3.5:2.4b → granite4.1:3b → gemma4:e2b

PYTHON="/home/neohc/miniconda3/bin/python"
BASE="/mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5"
LOG_DIR="$BASE"

exec > "$LOG_DIR/run_small_priority.log" 2>&1

log() { echo "[$(date '+%H:%M:%S')] $*"; }

log "===== 소형 모델 4개 우선 실행 시작 ====="

# ── S1: deepseek-r1:1.5b improved ────────────────────────────────────
log "=== deepseek-r1:1.5b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "deepseek-r1:1.5b" \
    > "$LOG_DIR/deepseek_r1_1_5b_improved_log.txt" 2>&1
log "deepseek-r1:1.5b improved 완료."

# ── S2: exaone3.5:2.4b improved ──────────────────────────────────────
log "=== exaone3.5:2.4b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "exaone3.5:2.4b" \
    > "$LOG_DIR/exaone35_2_4b_improved_log.txt" 2>&1
log "exaone3.5:2.4b improved 완료."

# ── S3: granite4.1:3b improved ───────────────────────────────────────
log "=== granite4.1:3b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "granite4.1:3b" \
    > "$LOG_DIR/granite4_1_3b_improved_log.txt" 2>&1
log "granite4.1:3b improved 완료."

# ── S4: gemma4:e2b improved ──────────────────────────────────────────
log "=== gemma4:e2b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "gemma4:e2b" \
    > "$LOG_DIR/gemma4_e2b_improved_log.txt" 2>&1
log "gemma4:e2b improved 완료."

# ── 소형 모델 비교 리포트 ─────────────────────────────────────────────
log "=== 소형 모델 비교 리포트 생성 ==="
$PYTHON -u "$BASE/generate_small_report.py" \
    > "$LOG_DIR/generate_small_report.log" 2>&1
log "소형 모델 비교 리포트 완료."

log "===== 소형 모델 4개 완료 ====="
touch "$BASE/.small_priority_done"
