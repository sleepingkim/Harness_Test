"""
LLM Comparison Conclusions — Chart Generator
Output: _workspace5/charts/*.png
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['axes.unicode_minus'] = False

# ── Data ─────────────────────────────────────────────────────────
models_short = [
    'gemma4:e4b\n(9.6GB)', 'gemma3:4b\n(3.3GB)', 'granite4.1:8b\n(5.3GB)',
    'gemma4:e2b\n(7.2GB)', 'exaone3.5:7.8b\n(4.8GB)', 'ds-r1:1.5b\n(1.1GB)',
    'ds-r1:8b\n(5.2GB)', 'exaone3.5:2.4b\n(1.6GB)', 'granite4.1:3b\n(2.1GB)'
]
accuracy   = [88.47, 84.48, 82.48, 80.93, 79.16, 78.05, 77.83, 74.06, 67.85]
speed      = [1.58, 1.77, 1.21, 1.93, 1.23, 1.49, 1.40, 1.58, 1.53]
vram       = [9.6, 3.3, 5.3, 7.2, 4.8, 1.1, 5.2, 1.6, 2.1]
fallback   = [8.14, 6.50, 5.01, 6.38, 9.19, 85.20, 2.60, 13.63, 20.76]
rag_errors = [24, 25, 25, 25, 23, 25, 25, 25, 25]
llm_errors = [28, 45, 54, 61, 71, 74, 75, 92, 120]

RAG_TOP1_BASELINE = 78.0
THEORETICAL_MAX   = (451 - 25) / 451 * 100  # 94.5%

family_colors = {
    'Gemma (Google)':   '#4285F4',
    'Granite (IBM)':    '#BE95FF',
    'EXAONE (LG)':      '#FF6B35',
    'DeepSeek-R1':      '#00B4D8',
}
bar_colors = [
    '#4285F4', '#4285F4', '#BE95FF',
    '#4285F4', '#FF6B35', '#00B4D8',
    '#00B4D8', '#FF6B35', '#BE95FF',
]

output_dir = os.path.join(os.path.dirname(__file__), 'charts')
os.makedirs(output_dir, exist_ok=True)

# ════════════════════════════════════════════════════════════════
# Chart 1: Accuracy comparison with baselines
# ════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(13, 6))
x = np.arange(len(models_short))
bars = ax.bar(x, accuracy, color=bar_colors, width=0.62, zorder=3, edgecolor='white', linewidth=0.5)

ax.axhline(RAG_TOP1_BASELINE, color='#E53935', linestyle='--', linewidth=2.0, zorder=4)
ax.axhline(THEORETICAL_MAX,  color='#2E7D32', linestyle=':',  linewidth=2.0, zorder=4)
ax.axhline(55.21,            color='#9E9E9E', linestyle='-.', linewidth=1.5, zorder=4)

for bar, acc in zip(bars, accuracy):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f'{acc}%', ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(models_short, fontsize=8.5)
ax.set_ylabel('Accuracy (%)', fontsize=11)
ax.set_title('Accuracy Comparison by Model (Improved RAG)', fontsize=13, fontweight='bold', pad=12)
ax.set_ylim(48, 102)
ax.grid(axis='y', alpha=0.35, zorder=0)

patches = [mpatches.Patch(color=v, label=k) for k, v in family_colors.items()]
lines = [
    plt.Line2D([0],[0], color='#E53935', linestyle='--', linewidth=2.0, label=f'RAG top-1 est. (~{RAG_TOP1_BASELINE}%)'),
    plt.Line2D([0],[0], color='#2E7D32', linestyle=':', linewidth=2.0, label=f'Theoretical max ({THEORETICAL_MAX:.1f}%)'),
    plt.Line2D([0],[0], color='#9E9E9E', linestyle='-.', linewidth=1.5, label='Baseline (55.21%)'),
]
ax.legend(handles=patches + lines, fontsize=8, loc='lower left', ncol=2)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'chart1_accuracy.png'), dpi=150, bbox_inches='tight')
plt.close()
print("chart1_accuracy.png saved")

# ════════════════════════════════════════════════════════════════
# Chart 2: VRAM vs Accuracy — size != performance
# ════════════════════════════════════════════════════════════════
labels_plain = [
    'gemma4:e4b', 'gemma3:4b', 'granite4.1:8b',
    'gemma4:e2b', 'exaone3.5:7.8b', 'ds-r1:1.5b',
    'ds-r1:8b', 'exaone3.5:2.4b', 'granite4.1:3b'
]

fig, ax = plt.subplots(figsize=(10, 6.5))
for i, (v, a, name, color) in enumerate(zip(vram, accuracy, labels_plain, bar_colors)):
    ax.scatter(v, a, s=180, color=color, zorder=5, edgecolors='white', linewidths=1.5)
    offsets = {
        'gemma3:4b': (0.1, -1.3),
        'gemma4:e2b': (-2.2, 0.4),
        'granite4.1:8b': (0.1, -1.3),
        'ds-r1:8b': (0.1, 0.5),
    }
    ox, oy = offsets.get(name, (0.12, 0.5))
    ax.annotate(name, (v, a), xytext=(v + ox, a + oy), fontsize=8.5, color='#222222')

z = np.polyfit(vram, accuracy, 1)
p = np.poly1d(z)
x_line = np.linspace(0.5, 10.5, 100)
ax.plot(x_line, p(x_line), 'k--', alpha=0.25, linewidth=1.5)

# Annotate the key anomaly
ax.annotate('3.3GB beats 4.8GB\n(+5.3%p)', xy=(3.3, 84.48), xytext=(4.8, 87),
            arrowprops=dict(arrowstyle='->', color='#555'), fontsize=8.5, color='#555')

ax.set_xlabel('Model Size (VRAM GB)', fontsize=11)
ax.set_ylabel('Accuracy (%)', fontsize=11)
ax.set_title('VRAM vs Accuracy — Size Does Not Determine Performance', fontsize=12, fontweight='bold', pad=10)
ax.grid(alpha=0.3)
ax.set_xlim(0, 11)
ax.set_ylim(62, 93)

patches = [mpatches.Patch(color=v, label=k) for k, v in family_colors.items()]
ax.legend(handles=patches + [
    plt.Line2D([0],[0], color='k', linestyle='--', alpha=0.3, label='Linear trend (weak)')
], fontsize=8.5, loc='lower right')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'chart2_vram_vs_accuracy.png'), dpi=150, bbox_inches='tight')
plt.close()
print("chart2_vram_vs_accuracy.png saved")

# ════════════════════════════════════════════════════════════════
# Chart 3: Error breakdown — RAG failure vs LLM failure
# ════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(12, 5.5))
x = np.arange(len(models_short))
width = 0.6

p1 = ax.bar(x, rag_errors, width, label='RAG Retrieval Failure (structural)', color='#EF5350', zorder=3)
p2 = ax.bar(x, llm_errors, width, bottom=rag_errors, label='LLM Wrong Selection (reasoning)', color='#26C6DA', zorder=3)

ax.axhline(25, color='#EF5350', linestyle=':', linewidth=1.8, alpha=0.7, label='Fixed RAG ceiling (~25 cases)')

for i, (r, l) in enumerate(zip(rag_errors, llm_errors)):
    total = r + l
    ax.text(i, total + 1.8, str(total), ha='center', va='bottom', fontsize=9, fontweight='bold')
    ax.text(i, r/2, str(r), ha='center', va='center', fontsize=8.5, color='white', fontweight='bold')
    ax.text(i, r + l/2, str(l), ha='center', va='center', fontsize=8.5, color='white', fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(models_short, fontsize=8.5)
ax.set_ylabel('Wrong predictions (out of 451)', fontsize=11)
ax.set_title('Error Decomposition — RAG Failure vs LLM Failure', fontsize=12, fontweight='bold', pad=10)
ax.legend(fontsize=9.5, loc='upper left')
ax.grid(axis='y', alpha=0.3, zorder=0)
ax.set_ylim(0, 168)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'chart3_error_breakdown.png'), dpi=150, bbox_inches='tight')
plt.close()
print("chart3_error_breakdown.png saved")

# ════════════════════════════════════════════════════════════════
# Chart 4: LLM value-add over RAG top-1
# ════════════════════════════════════════════════════════════════
llm_contribution = [a - RAG_TOP1_BASELINE for a in accuracy]
colors_contrib = ['#43A047' if v > 0 else '#E53935' for v in llm_contribution]

fig, ax = plt.subplots(figsize=(11, 5.5))
x = np.arange(len(models_short))
bars = ax.bar(x, llm_contribution, color=colors_contrib, width=0.62, zorder=3,
              edgecolor='white', linewidth=0.5)

ax.axhline(0, color='black', linewidth=1.5, zorder=4)

for bar, val in zip(bars, llm_contribution):
    ypos = bar.get_height() + 0.15 if val >= 0 else bar.get_height() - 0.9
    va   = 'bottom' if val >= 0 else 'top'
    ax.text(bar.get_x() + bar.get_width()/2, ypos,
            f'{val:+.1f}%p', ha='center', va=va, fontsize=9, fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(models_short, fontsize=8.5)
ax.set_ylabel('LLM Value-Add (%p)', fontsize=11)
ax.set_title(f'LLM Value-Add over RAG top-1 Baseline (~{RAG_TOP1_BASELINE}%)', fontsize=12, fontweight='bold', pad=10)
ax.set_ylim(-13, 14)
ax.grid(axis='y', alpha=0.3, zorder=0)

green_patch = mpatches.Patch(color='#43A047', label='LLM improves accuracy')
red_patch   = mpatches.Patch(color='#E53935', label='LLM hurts accuracy')
ax.legend(handles=[green_patch, red_patch], fontsize=9.5)

ax.text(0.02, 0.96, f'RAG top-1 baseline: ~{RAG_TOP1_BASELINE}%\n(estimated from ds-r1:1.5b, 85.2% fallback)',
        transform=ax.transAxes, fontsize=8, va='top', color='#555',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#f9f9f9', alpha=0.8))

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'chart4_llm_contribution.png'), dpi=150, bbox_inches='tight')
plt.close()
print("chart4_llm_contribution.png saved")

# ════════════════════════════════════════════════════════════════
# Chart 5: Speed vs Accuracy — Pareto frontier
# ════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9.5, 6.5))

pareto = []
for i, (s, a) in enumerate(zip(speed, accuracy)):
    dominated = any(
        speed[j] >= s and accuracy[j] >= a and (speed[j] > s or accuracy[j] > a)
        for j in range(len(speed)) if j != i
    )
    if not dominated:
        pareto.append(i)

pareto_sorted = sorted(pareto, key=lambda i: speed[i])
ax.plot([speed[i] for i in pareto_sorted], [accuracy[i] for i in pareto_sorted],
        'k--', alpha=0.3, linewidth=1.5, zorder=2)

for i, (s, a, name, color) in enumerate(zip(speed, accuracy, labels_plain, bar_colors)):
    is_pareto = i in pareto
    ax.scatter(s, a, s=220 if is_pareto else 100, color=color, zorder=5,
               edgecolors='black' if is_pareto else 'white',
               linewidths=2.0 if is_pareto else 0.8)
    offsets_p = {
        'gemma4:e2b': (0.02, -1.0),
        'ds-r1:8b': (0.02, 0.4),
        'granite4.1:8b': (-0.35, -1.1),
    }
    ox, oy = offsets_p.get(name, (0.02, 0.4))
    ax.annotate(name, (s, a), xytext=(s + ox, a + oy), fontsize=8.5, color='#222222')

ax.set_xlabel('Processing Speed (items/sec)', fontsize=11)
ax.set_ylabel('Accuracy (%)', fontsize=11)
ax.set_title('Speed vs Accuracy — Pareto Frontier', fontsize=12, fontweight='bold', pad=10)
ax.grid(alpha=0.3)
ax.set_xlim(1.05, 2.1)
ax.set_ylim(63, 93)

patches = [mpatches.Patch(color=v, label=k) for k, v in family_colors.items()]
ax.legend(handles=patches + [
    plt.scatter([], [], s=180, c='gray', edgecolors='black', linewidths=2, label='Pareto optimal'),
    plt.Line2D([0],[0], color='k', linestyle='--', alpha=0.3, label='Pareto frontier'),
], fontsize=8.5, loc='lower left')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'chart5_pareto.png'), dpi=150, bbox_inches='tight')
plt.close()
print("chart5_pareto.png saved")

print(f"\nAll charts saved to: {output_dir}")
