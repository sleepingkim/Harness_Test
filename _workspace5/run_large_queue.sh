#!/usr/bin/env bash
# 대형 모델(27B~33B) improved 순차 실행
# 현재 run_queue.sh 완료 후 자동 호출됨

PYTHON="/home/neohc/miniconda3/bin/python"
BASE="/mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5"
LOG_DIR="$BASE"

log() { echo "[$(date '+%H:%M:%S')] $*"; }

log "===== 대형 모델 실험 시작 ====="

# ── L1: deepseek-r1:32b improved ─────────────────────────────────────
log "=== deepseek-r1:32b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "deepseek-r1:32b" \
    > "$LOG_DIR/deepseek_r1_32b_improved_log.txt" 2>&1
log "deepseek-r1:32b improved 완료."

# ── L2: granite4.1:30b improved ──────────────────────────────────────
log "=== granite4.1:30b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "granite4.1:30b" \
    > "$LOG_DIR/granite4_1_30b_improved_log.txt" 2>&1
log "granite4.1:30b improved 완료."

# ── L3: SKIP placeholder (qwen3.5:27b은 맨 마지막으로 이동)

# ── L4: EXAONE-4.5-33B improved ──────────────────────────────────────
log "=== EXAONE-4.5-33B improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "hf.co/LGAI-EXAONE/EXAONE-4.5-33B-GGUF:Q4_K_M" \
    > "$LOG_DIR/exaone45_33b_improved_log.txt" 2>&1
log "EXAONE-4.5-33B improved 완료."

# ── L5: gemma4:31b improved ──────────────────────────────────────────
log "=== gemma4:31b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "gemma4:31b" \
    > "$LOG_DIR/gemma4_31b_improved_log.txt" 2>&1
log "gemma4:31b improved 완료."

# ── L5: deepseek-r1:32b improved (재실행 — num_predict:800 적용) ────────
log "=== deepseek-r1:32b improved 재실행 (num_predict:800) ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "deepseek-r1:32b" \
    > "$LOG_DIR/deepseek_r1_32b_improved_log.txt" 2>&1
log "deepseek-r1:32b improved 완료."

# ── L6: qwen3.5:27b improved (최하위 — 마지막, thinking 모드라 느림) ────
log "=== qwen3.5:27b improved 시작 (최하위 순위) ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "qwen3.5:27b" \
    > "$LOG_DIR/qwen35_27b_improved_log.txt" 2>&1
log "qwen3.5:27b improved 완료."

log "===== 모든 대형 모델 실험 완료 ====="
touch "$BASE/.large_queue_done"
