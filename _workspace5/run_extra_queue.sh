#!/usr/bin/env bash
# 추가 모델 4종 — improved만 실행 (용량 작은 순)
# gemma3:4b → exaone3.5:7.8b → gemma3:27b → exaone3.5:32b

PYTHON="/home/neohc/miniconda3/bin/python"
BASE="/mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5"
LOG_DIR="$BASE"

log() { echo "[$(date '+%H:%M:%S')] $*"; }

log "===== 추가 모델 실험 시작 (improved only) ====="

# ── E1: gemma3:4b improved ────────────────────────────────────────────
log "=== gemma3:4b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "gemma3:4b" \
    > "$LOG_DIR/gemma3_4b_improved_log.txt" 2>&1
log "gemma3:4b improved 완료."

# ── E2: exaone3.5:7.8b improved ──────────────────────────────────────
log "=== exaone3.5:7.8b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "exaone3.5:7.8b" \
    > "$LOG_DIR/exaone35_7b_improved_log.txt" 2>&1
log "exaone3.5:7.8b improved 완료."

# ── E3: gemma3:27b improved ──────────────────────────────────────────
log "=== gemma3:27b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "gemma3:27b" \
    > "$LOG_DIR/gemma3_27b_improved_log.txt" 2>&1
log "gemma3:27b improved 완료."

# ── E4: exaone3.5:32b improved ───────────────────────────────────────
log "=== exaone3.5:32b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "exaone3.5:32b" \
    > "$LOG_DIR/exaone35_32b_improved_log.txt" 2>&1
log "exaone3.5:32b improved 완료."

log "===== 추가 모델 실험 전체 완료 ====="
touch "$BASE/.extra_queue_done"
