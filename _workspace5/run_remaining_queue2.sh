#!/usr/bin/env bash
# granite4.1:30b 완료 + 소형 4개 우선 실행 후 남은 대형 큐
# EXAONE-4.5-33B → gemma4:31b → deepseek-r1:32b 재실행 → qwen3.5:27b
# → qwen3.5:9b baseline 재실행 → 추가 4종(gemma3, exaone3.5) → 전체 리포트

PYTHON="/home/neohc/miniconda3/bin/python"
BASE="/mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5"
LOG_DIR="$BASE"

exec > "$LOG_DIR/run_remaining_queue2.log" 2>&1

log() { echo "[$(date '+%H:%M:%S')] $*"; }

log "===== 나머지 대형 모델 큐 시작 ====="

# ── R1: EXAONE-4.5-33B improved ──────────────────────────────────────
log "=== EXAONE-4.5-33B improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "hf.co/LGAI-EXAONE/EXAONE-4.5-33B-GGUF:Q4_K_M" \
    > "$LOG_DIR/exaone45_33b_improved_log.txt" 2>&1
log "EXAONE-4.5-33B improved 완료."

# ── R2: gemma4:31b improved ──────────────────────────────────────────
log "=== gemma4:31b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "gemma4:31b" \
    > "$LOG_DIR/gemma4_31b_improved_log.txt" 2>&1
log "gemma4:31b improved 완료."

# ── R3: deepseek-r1:32b improved 재실행 (num_predict:800 적용) ────────
log "=== deepseek-r1:32b improved 재실행 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "deepseek-r1:32b" \
    > "$LOG_DIR/deepseek_r1_32b_improved_log.txt" 2>&1
log "deepseek-r1:32b improved 재실행 완료."

# ── R4: qwen3.5:27b improved (최하위 순위) ───────────────────────────
log "=== qwen3.5:27b improved 시작 (최하위 순위) ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "qwen3.5:27b" \
    > "$LOG_DIR/qwen35_27b_improved_log.txt" 2>&1
log "qwen3.5:27b improved 완료."

# ── R5: qwen3.5:9b baseline 재실행 (IS_QWEN3 수정 적용) ──────────────
log "=== qwen3.5:9b baseline 재실행 ==="
$PYTHON -u "$BASE/run_rag_v2_full.py" "qwen3.5:9b" \
    > "$LOG_DIR/qwen35_9b_rerun_log.txt" 2>&1
log "qwen3.5:9b baseline 재실행 완료."

# ── R6: 추가 4종 (gemma3:4b, exaone3.5:7.8b, gemma3:27b, exaone3.5:32b) improved
log "=== 추가 4종 큐 시작 (improved only) ==="
bash "$BASE/run_extra_queue.sh"
log "=== 추가 4종 큐 완료 ==="

# ── R7: 전체 성능 비교 리포트 ─────────────────────────────────────────
log "=== 전체 성능 비교 리포트 생성 ==="
$PYTHON -u "$BASE/generate_report.py" \
    > "$LOG_DIR/generate_report.log" 2>&1
log "전체 성능 비교 리포트 완료."

log "=== 추가 모델 비교 리포트 생성 ==="
$PYTHON -u "$BASE/generate_extra_report.py" \
    > "$LOG_DIR/generate_extra_report.log" 2>&1
log "추가 모델 비교 리포트 완료."

log "=== 프렉티컴 보고서 생성 ==="
$PYTHON -u "$BASE/generate_practicum_update.py" \
    > "$LOG_DIR/generate_practicum.log" 2>&1
log "프렉티컴 보고서 완료."

log "===== 전체 파이프라인 완료 ====="
touch "$BASE/.queue_done"
