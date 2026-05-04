#!/usr/bin/env bash
# 남은 실험 순차 실행: qwen3.5:9b baseline → improved 3종
# wsl.exe -e bash /mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5/run_queue.sh

PYTHON="/home/neohc/miniconda3/bin/python"
BASE="/mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5"
LOG_DIR="$BASE"

exec > "$LOG_DIR/run_queue.log" 2>&1

log() { echo "[$(date '+%H:%M:%S')] $*"; }

# ── Step 0: qwen3.5:9b baseline ──────────────────────────────────────
log "=== qwen3.5:9b baseline 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_full.py" "qwen3.5:9b" \
    > "$LOG_DIR/qwen35_9b_log.txt" 2>&1
log "qwen3.5:9b baseline 완료."

# ── Step 1: deepseek-r1:8b improved ──────────────────────────────────
log "=== deepseek-r1:8b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "deepseek-r1:8b" \
    > "$LOG_DIR/deepseek_r1_8b_improved_log.txt" 2>&1
log "deepseek-r1:8b improved 완료."

# ── Step 2: granite4.1:8b improved ───────────────────────────────────
log "=== granite4.1:8b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "granite4.1:8b" \
    > "$LOG_DIR/granite4_1_8b_improved_log.txt" 2>&1
log "granite4.1:8b improved 완료."

# ── Step 3: qwen3.5:9b improved ──────────────────────────────────────
log "=== qwen3.5:9b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "qwen3.5:9b" \
    > "$LOG_DIR/qwen35_9b_improved_log.txt" 2>&1
log "qwen3.5:9b improved 완료."

# ── Step 4: 대형 모델 큐 (qwen보다 우선) ────────────────────────────────
log "=== 대형 모델 큐 시작 (qwen 최하위 정책 적용) ==="
bash "$BASE/run_large_queue.sh"

# ── Step 5: qwen3.5:9b baseline 재실행 (최하위 — 대형 모델 후) ─────────
log "=== qwen3.5:9b baseline 재실행 (IS_QWEN3 수정 적용) ==="
$PYTHON -u "$BASE/run_rag_v2_full.py" "qwen3.5:9b" \
    > "$LOG_DIR/qwen35_9b_rerun_log.txt" 2>&1
log "qwen3.5:9b baseline 재실행 완료."

# ── Step 6: 추가 모델 4종 (improved only) — gemma3:4b → exaone3.5:7.8b → gemma3:27b → exaone3.5:32b
log "=== 추가 모델 4종 큐 시작 (improved only) ==="
bash "$BASE/run_extra_queue.sh"
log "=== 추가 모델 4종 큐 완료 ==="

# ── Step 7: 최종 리포트 자동 생성 ────────────────────────────────────────
log "=== 성능 비교 리포트 생성 ==="
$PYTHON -u "$BASE/generate_report.py" \
    > "$LOG_DIR/generate_report.log" 2>&1
log "성능 비교 리포트 완료."

log "=== 추가 4개 모델 비교 리포트 생성 ==="
$PYTHON -u "$BASE/generate_extra_report.py" \
    > "$LOG_DIR/generate_extra_report.log" 2>&1
log "추가 4개 모델 비교 리포트 완료."

log "=== 프렉티컴 보고서 생성 ==="
$PYTHON -u "$BASE/generate_practicum_update.py" \
    > "$LOG_DIR/generate_practicum.log" 2>&1
log "프렉티컴 보고서 완료."

log "=== 전체 파이프라인 완료 ==="
touch "$BASE/.queue_done"
