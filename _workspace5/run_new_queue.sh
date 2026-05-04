#!/usr/bin/env bash
# 새 우선순위 큐: 소형 먼저 → 대형(qwen 제외) → qwen 마지막
# wsl.exe -e bash /mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5/run_new_queue.sh

PYTHON="/home/neohc/miniconda3/bin/python"
BASE="/mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5"
LOG_DIR="$BASE"

exec > "$LOG_DIR/run_new_queue.log" 2>&1

log() { echo "[$(date '+%H:%M:%S')] $*"; }

log "===== 새 우선순위 큐 시작 ====="
log "순서: 소형 6개 → 소형 리포트 → 대형 6개 → qwen 2개 → 전체 리포트"

# ════════════════════════════════════════════════════════════
# PART 1: 소형 모델 (용량 오름차순, improved only)
# ════════════════════════════════════════════════════════════

log "===== [PART 1] 소형 모델 6개 시작 ====="

# S1: deepseek-r1:1.5b (1.1GB)
log "=== deepseek-r1:1.5b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "deepseek-r1:1.5b" \
    > "$LOG_DIR/deepseek_r1_1_5b_improved_log.txt" 2>&1
log "deepseek-r1:1.5b improved 완료."

# S2: exaone3.5:2.4b (1.6GB)
log "=== exaone3.5:2.4b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "exaone3.5:2.4b" \
    > "$LOG_DIR/exaone35_2_4b_improved_log.txt" 2>&1
log "exaone3.5:2.4b improved 완료."

# S3: granite4.1:3b (2.1GB)
log "=== granite4.1:3b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "granite4.1:3b" \
    > "$LOG_DIR/granite4_1_3b_improved_log.txt" 2>&1
log "granite4.1:3b improved 완료."

# S4: gemma3:4b (3.3GB)
log "=== gemma3:4b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "gemma3:4b" \
    > "$LOG_DIR/gemma3_4b_improved_log.txt" 2>&1
log "gemma3:4b improved 완료."

# S5: exaone3.5:7.8b (4.8GB)
log "=== exaone3.5:7.8b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "exaone3.5:7.8b" \
    > "$LOG_DIR/exaone35_7b_improved_log.txt" 2>&1
log "exaone3.5:7.8b improved 완료."

# S6: gemma4:e2b (7.2GB)
log "=== gemma4:e2b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "gemma4:e2b" \
    > "$LOG_DIR/gemma4_e2b_improved_log.txt" 2>&1
log "gemma4:e2b improved 완료."

log "===== [PART 1] 소형 모델 6개 완료 ====="
touch "$BASE/.small_done"

# 소형 모델 중간 리포트
log "=== 소형 모델 비교 리포트 생성 ==="
$PYTHON -u "$BASE/generate_small_report.py" \
    > "$LOG_DIR/generate_small_report.log" 2>&1
log "소형 모델 비교 리포트 완료."

# ════════════════════════════════════════════════════════════
# PART 2: 대형 모델 (qwen 제외, improved only)
# ════════════════════════════════════════════════════════════

log "===== [PART 2] 대형 모델 6개 시작 (qwen 제외) ====="

# L1: granite4.1:30b (17GB)
log "=== granite4.1:30b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "granite4.1:30b" \
    > "$LOG_DIR/granite4_1_30b_improved_log.txt" 2>&1
log "granite4.1:30b improved 완료."

# L2: gemma3:27b (17GB)
log "=== gemma3:27b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "gemma3:27b" \
    > "$LOG_DIR/gemma3_27b_improved_log.txt" 2>&1
log "gemma3:27b improved 완료."

# L3: gemma4:31b (19GB)
log "=== gemma4:31b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "gemma4:31b" \
    > "$LOG_DIR/gemma4_31b_improved_log.txt" 2>&1
log "gemma4:31b improved 완료."

# L4: deepseek-r1:32b (19GB) — num_predict:800으로 속도 개선
log "=== deepseek-r1:32b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "deepseek-r1:32b" \
    > "$LOG_DIR/deepseek_r1_32b_improved_log.txt" 2>&1
log "deepseek-r1:32b improved 완료."

# L5: exaone3.5:32b (19GB)
log "=== exaone3.5:32b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "exaone3.5:32b" \
    > "$LOG_DIR/exaone35_32b_improved_log.txt" 2>&1
log "exaone3.5:32b improved 완료."

# L6: EXAONE-4.5-33B (22GB)
log "=== EXAONE-4.5-33B improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "hf.co/LGAI-EXAONE/EXAONE-4.5-33B-GGUF:Q4_K_M" \
    > "$LOG_DIR/exaone45_33b_improved_log.txt" 2>&1
log "EXAONE-4.5-33B improved 완료."

log "===== [PART 2] 대형 모델 6개 완료 ====="
touch "$BASE/.large_done"

# ════════════════════════════════════════════════════════════
# PART 3: qwen 모델 (최하위 순위)
# ════════════════════════════════════════════════════════════

log "===== [PART 3] qwen 모델 시작 (최하위 순위) ====="

# Q1: qwen3.5:9b baseline 재실행 (IS_QWEN3 수정 적용)
log "=== qwen3.5:9b baseline 재실행 ==="
$PYTHON -u "$BASE/run_rag_v2_full.py" "qwen3.5:9b" \
    > "$LOG_DIR/qwen35_9b_rerun_log.txt" 2>&1
log "qwen3.5:9b baseline 재실행 완료."

# Q2: qwen3.5:27b improved (thinking 모드라 느림)
log "=== qwen3.5:27b improved 시작 ==="
$PYTHON -u "$BASE/run_rag_v2_improved.py" "qwen3.5:27b" \
    > "$LOG_DIR/qwen35_27b_improved_log.txt" 2>&1
log "qwen3.5:27b improved 완료."

log "===== [PART 3] qwen 모델 완료 ====="
touch "$BASE/.qwen_done"

# ════════════════════════════════════════════════════════════
# PART 4: 전체 리포트 생성
# ════════════════════════════════════════════════════════════

log "===== [PART 4] 전체 리포트 생성 ====="

log "=== 전체 성능 비교 리포트 ==="
$PYTHON -u "$BASE/generate_report.py" \
    > "$LOG_DIR/generate_report.log" 2>&1
log "전체 성능 비교 리포트 완료."

log "=== 소형 모델 비교 리포트 (최종) ==="
$PYTHON -u "$BASE/generate_small_report.py" \
    > "$LOG_DIR/generate_small_report_final.log" 2>&1
log "소형 모델 비교 리포트 완료."

log "=== 추가 모델 비교 리포트 ==="
$PYTHON -u "$BASE/generate_extra_report.py" \
    > "$LOG_DIR/generate_extra_report.log" 2>&1
log "추가 모델 비교 리포트 완료."

log "=== 프렉티컴 보고서 생성 ==="
$PYTHON -u "$BASE/generate_practicum_update.py" \
    > "$LOG_DIR/generate_practicum.log" 2>&1
log "프렉티컴 보고서 완료."

log "===== 전체 파이프라인 완료 ====="
touch "$BASE/.all_done"
