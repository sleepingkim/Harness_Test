#!/usr/bin/env bash
# granite4.1:30b 완료를 감지 → 기존 큐 종료 → 소형 4개 우선 실행 → 나머지 대형 큐
# 실행: wsl.exe -e bash /mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5/watchdog_priority.sh

PYTHON="/home/neohc/miniconda3/bin/python"
BASE="/mnt/c/Users/neohc/Desktop/ClaudeCode/_workspace5"
GRANITE_CSV="$BASE/New_RAG_v2_granite4_1_30b_improved_3352.csv"

exec > "$BASE/watchdog_priority.log" 2>&1

log() { echo "[$(date '+%H:%M:%S')] $*"; }

log "===== watchdog 시작: granite4.1:30b 완료 대기 중 ====="

# ── granite4.1:30b CSV 생성 대기 (30초 간격으로 폴링) ─────────────────
while [ ! -f "$GRANITE_CSV" ]; do
    sleep 30
done

log "granite4.1:30b 완료 감지!"

# ── 기존 큐 프로세스 종료 (granite4.1:30b는 이미 완료됨) ─────────────
log "기존 큐 프로세스 종료 중..."
pkill -f "run_queue.sh"       2>/dev/null
pkill -f "run_large_queue.sh" 2>/dev/null
pkill -f "run_rag_v2_improved.py" 2>/dev/null
pkill -f "run_rag_v2_full.py" 2>/dev/null
sleep 5
log "기존 큐 종료 완료."

# ── 소형 4개 우선 실행 ────────────────────────────────────────────────
log "===== 소형 모델 4개 우선 실행 시작 ====="
bash "$BASE/run_small_priority.sh"
log "===== 소형 모델 4개 완료 ====="

# ── 나머지 대형 큐 실행 ──────────────────────────────────────────────
log "===== 나머지 대형 큐 시작 ====="
bash "$BASE/run_remaining_queue2.sh"
log "===== 전체 파이프라인 완료 ====="
