#!/usr/bin/env python3
"""
Poster Figure Generator — LLM+RAG Semantic Standardization
Outputs 5 publication-quality PNG figures to _workspace5/figures/
Run: python generate_figures.py
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.gridspec as gridspec
import numpy as np
import os

# ── Font & style ───────────────────────────────────────────────────────────────
plt.rcParams['font.family']       = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi']         = 300

# ── Color palette (matches generate_poster.py) ────────────────────────────────
C_DARK_BLUE   = '#1A3A6B'
C_MID_BLUE    = '#2E70BF'
C_LIGHT_BLUE  = '#D6E8F7'
C_ORANGE      = '#E8722A'
C_GREEN       = '#2D9C4F'
C_RED         = '#C0392B'
C_GRAY        = '#95A5A6'
C_YELLOW      = '#F39C12'
C_PANEL       = '#FDFDFF'
C_ALT_ROW     = '#E8F1FB'

DPI    = 300
OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figures')
os.makedirs(OUTDIR, exist_ok=True)


# ══════════════════════════════════════════════════════════════════════════════
# FIG 1 — RAG Pipeline Architecture  (Methods)
# ══════════════════════════════════════════════════════════════════════════════
def fig1_pipeline():
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    fig.patch.set_facecolor(C_PANEL)

    configs = [
        {
            'title': 'Baseline',
            'title_color': C_GRAY,
            'border': C_GRAY,
            'steps': [
                ('Dirty Tool Name\n(input)', '#ECF0F1', 'black'),
                ('Embedding\nMiniLM-L12\n(384-dim)', '#D5E8D4', C_DARK_BLUE),
                ('FAISS Retrieval\nTop-k = 5', '#D5E8D4', C_DARK_BLUE),
                ('LLM Classification\n(Ollama local)', '#DAE8FC', C_DARK_BLUE),
                ('Fallback\n(top-1 override)', '#FFF2CC', C_DARK_BLUE),
                ('Standard Name\n(output)', '#F8CECC', 'black'),
            ],
            'note': 'Accuracy: ~55%',
        },
        {
            'title': 'Improved  ★',
            'title_color': C_MID_BLUE,
            'border': C_MID_BLUE,
            'steps': [
                ('Dirty Tool Name\n(input)', '#ECF0F1', 'black'),
                ('Embedding ★\nBGE-m3-ko\n(1024-dim, Korean #1)', '#D5E8D4', C_DARK_BLUE),
                ('Hybrid Retrieval ★\nBM25 (40%) + FAISS (60%)\nTop-k = 15', '#D5E8D4', C_DARK_BLUE),
                ('LLM Classification ★\n+ Category Injection\n(Ollama local)', '#DAE8FC', C_DARK_BLUE),
                ('Fallback\n(top-1 override)', '#FFF2CC', C_DARK_BLUE),
                ('Standard Name\n(output)', '#D5E8D4', 'black'),
            ],
            'note': 'Accuracy: up to 88.47%  (+33.3 pp)',
        },
    ]

    for ax, cfg in zip(axes, configs):
        ax.set_facecolor(C_PANEL)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        # border
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_edgecolor(cfg['border'])
            spine.set_linewidth(2)

        # title
        ax.text(0.5, 0.97, cfg['title'], ha='center', va='top',
                fontsize=16, fontweight='bold', color=cfg['title_color'],
                transform=ax.transAxes)

        n = len(cfg['steps'])
        box_h = 0.10
        gap   = (0.88 / n)
        bx    = 0.1
        bw    = 0.8

        for i, (label, bg, tc) in enumerate(cfg['steps']):
            y = 0.88 - i * gap
            # box
            fancy = FancyBboxPatch((bx, y - box_h / 2), bw, box_h,
                                   boxstyle='round,pad=0.01',
                                   facecolor=bg, edgecolor='#B0B0B0', linewidth=1,
                                   transform=ax.transAxes, zorder=2)
            ax.add_patch(fancy)
            ax.text(bx + bw / 2, y, label,
                    ha='center', va='center', fontsize=9.5,
                    color=tc, fontweight='bold' if '★' in label else 'normal',
                    transform=ax.transAxes, zorder=3)
            # arrow
            if i < n - 1:
                ax.annotate('', xy=(bx + bw / 2, y - box_h / 2 - 0.002),
                            xytext=(bx + bw / 2, y - gap + box_h / 2 + 0.002),
                            xycoords='axes fraction', textcoords='axes fraction',
                            arrowprops=dict(arrowstyle='->', color='#606060', lw=1.5),
                            zorder=4)

        # note at bottom
        ax.text(0.5, 0.01, cfg['note'], ha='center', va='bottom',
                fontsize=10, fontstyle='italic',
                color=C_MID_BLUE if '88' in cfg['note'] else C_GRAY,
                transform=ax.transAxes)

    fig.suptitle('RAG Pipeline Architecture: Baseline vs. Improved',
                 fontsize=15, fontweight='bold', color=C_DARK_BLUE, y=1.01)

    plt.tight_layout(pad=1.5)
    out = os.path.join(OUTDIR, 'fig1_rag_pipeline.png')
    fig.savefig(out, dpi=DPI, bbox_inches='tight', facecolor=C_PANEL)
    plt.close(fig)
    print(f'  saved: {out}')


# ══════════════════════════════════════════════════════════════════════════════
# FIG 2 — Full Model Accuracy  (Results 3.1)
# ══════════════════════════════════════════════════════════════════════════════
def fig2_model_accuracy():
    models_improved = [
        ('gemma4:e4b',        88.47),
        ('gemma3:4b',         84.48),
        ('granite4.1:8b',     82.48),
        ('gemma4:e2b',        80.93),
        ('exaone3.5:7.8b',    79.16),
        ('deepseek-r1:1.5b',  78.05),
        ('deepseek-r1:8b',    77.83),
        ('exaone3.5:2.4b',    74.06),
        ('granite4.1:3b',     67.85),
    ]
    models_baseline = [
        ('deepseek-r1:8b\n(baseline)', 55.21),
        ('granite4.1:8b\n(baseline)',  55.21),
        ('qwen3.5:9b\n(baseline)',     0.00),
    ]

    labels  = [m[0] for m in models_improved] + [m[0] for m in models_baseline]
    accs    = [m[1] for m in models_improved] + [m[1] for m in models_baseline]
    colors  = [C_DARK_BLUE if a >= 80 else C_ORANGE for a in [m[1] for m in models_improved]] \
            + [C_GRAY] * len(models_baseline)
    hatches = [''] * len(models_improved) + ['//'] * len(models_baseline)

    y = np.arange(len(labels))

    fig, ax = plt.subplots(figsize=(11, 8))
    fig.patch.set_facecolor(C_PANEL)
    ax.set_facecolor('#F7F9FC')

    bars = ax.barh(y, accs, height=0.65, color=colors, zorder=2)
    for bar, hatch in zip(bars, hatches):
        bar.set_hatch(hatch)
        bar.set_edgecolor('white')

    # 80% threshold line
    ax.axvline(80, color='#E74C3C', linestyle='--', linewidth=1.4, zorder=3,
               label='80% threshold')

    # value labels
    for i, (bar, acc) in enumerate(zip(bars, accs)):
        if acc > 0:
            ax.text(acc + 0.8, bar.get_y() + bar.get_height() / 2,
                    f'{acc:.1f}%', va='center', fontsize=9.5, color='#2C3E50')

    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel('Accuracy (%)', fontsize=11)
    ax.set_xlim(0, 100)
    ax.set_title('Overall Accuracy by Model\n(RAG v2, GT v2, n=451 valid)',
                 fontsize=13, fontweight='bold', color=C_DARK_BLUE, pad=10)

    legend_handles = [
        mpatches.Patch(color=C_DARK_BLUE, label='Improved ≥ 80%'),
        mpatches.Patch(color=C_ORANGE,    label='Improved < 80%'),
        mpatches.Patch(color=C_GRAY,      hatch='//', label='Baseline'),
        plt.Line2D([0], [0], color='#E74C3C', linestyle='--', linewidth=1.4,
                   label='80% threshold'),
    ]
    ax.legend(handles=legend_handles, loc='lower right', fontsize=9.5,
              framealpha=0.9)
    ax.grid(axis='x', linestyle=':', alpha=0.5, zorder=1)
    ax.spines[['top', 'right']].set_visible(False)

    plt.tight_layout()
    out = os.path.join(OUTDIR, 'fig2_model_accuracy_full.png')
    fig.savefig(out, dpi=DPI, bbox_inches='tight', facecolor=C_PANEL)
    plt.close(fig)
    print(f'  saved: {out}')


# ══════════════════════════════════════════════════════════════════════════════
# FIG 3 — Type Accuracy + Distribution  (Results 3.2)
# ══════════════════════════════════════════════════════════════════════════════
def fig3_type_accuracy():
    types = [
        ('Japanese-derived\nterms',     47.1,  4.6,  '#C0392B'),
        ('Other',                        66.7,  5.9,  '#E67E22'),
        ('English abbr. /\nAcronyms',   82.5,  9.0,  C_ORANGE),
        ('Set / Kit items',              84.6,  5.0,  C_ORANGE),
        ('Brand inclusion',              87.5, 15.5,  C_MID_BLUE),
        ('Typos / non-\nstandard',       93.8, 33.9,  C_DARK_BLUE),
        ('Attribute-\nembedded',         95.0,  8.8,  C_DARK_BLUE),
        ('Metadata tags',                95.5,  4.8,  C_DARK_BLUE),
        ('Power source\nspecified',      96.4, 10.9,  C_DARK_BLUE),
        ('Special\ncharacters',         100.0,  1.3,  C_GREEN),
    ]

    labels = [t[0] for t in types]
    accs   = [t[1] for t in types]
    freqs  = [t[2] for t in types]
    colors = [t[3] for t in types]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6),
                                    gridspec_kw={'width_ratios': [2.5, 1]})
    fig.patch.set_facecolor(C_PANEL)

    # ─ Left: accuracy bars ───────────────────────────────────────────────────
    ax1.set_facecolor('#F7F9FC')
    y = np.arange(len(labels))
    bars = ax1.barh(y, accs, height=0.65, color=colors, zorder=2)
    for bar in bars:
        bar.set_edgecolor('white')

    ax1.axvline(80, color='#E74C3C', linestyle='--', linewidth=1.4, zorder=3,
                label='80% threshold')
    for bar, acc in zip(bars, accs):
        ax1.text(acc + 0.5, bar.get_y() + bar.get_height() / 2,
                 f'{acc:.1f}%', va='center', fontsize=9.5, color='#2C3E50')

    ax1.set_yticks(y)
    ax1.set_yticklabels(labels, fontsize=10)
    ax1.set_xlabel('Accuracy (%)', fontsize=11)
    ax1.set_xlim(0, 110)
    ax1.set_title('Accuracy by Dirty Data Type\n(gemma4:e4b, best model)',
                  fontsize=12, fontweight='bold', color=C_DARK_BLUE)
    ax1.legend(fontsize=9, loc='lower right')
    ax1.grid(axis='x', linestyle=':', alpha=0.5, zorder=1)
    ax1.spines[['top', 'right']].set_visible(False)

    # ─ Right: frequency distribution ─────────────────────────────────────────
    ax2.set_facecolor('#F7F9FC')
    freq_colors = [C_RED if t[1] < 60 else C_ORANGE if t[1] < 80 else C_MID_BLUE
                   for t in types]
    bars2 = ax2.barh(y, freqs, height=0.65, color=freq_colors, zorder=2)
    for bar in bars2:
        bar.set_edgecolor('white')
    for bar, f in zip(bars2, freqs):
        ax2.text(f + 0.3, bar.get_y() + bar.get_height() / 2,
                 f'{f}%', va='center', fontsize=9, color='#2C3E50')

    ax2.set_yticks(y)
    ax2.set_yticklabels([])
    ax2.set_xlabel('Frequency in GT (%)', fontsize=11)
    ax2.set_xlim(0, 45)
    ax2.set_title('GT Distribution', fontsize=12, fontweight='bold',
                  color=C_DARK_BLUE)
    ax2.grid(axis='x', linestyle=':', alpha=0.5, zorder=1)
    ax2.spines[['top', 'right']].set_visible(False)

    fig.suptitle('Dirty Data Type Analysis  (457 GT pairs)',
                 fontsize=13, fontweight='bold', color=C_DARK_BLUE, y=1.02)
    plt.tight_layout(pad=1.5)
    out = os.path.join(OUTDIR, 'fig3_type_accuracy_clean.png')
    fig.savefig(out, dpi=DPI, bbox_inches='tight', facecolor=C_PANEL)
    plt.close(fig)
    print(f'  saved: {out}')


# ══════════════════════════════════════════════════════════════════════════════
# FIG 4 — LLM-only vs RAG  (Results 3.3)
# ══════════════════════════════════════════════════════════════════════════════
def fig4_llm_rag():
    models = ['gemma4:e4b', 'gemma3:4b', 'exaone3.5:7.8b', 'deepseek-r1:1.5b']
    exact   = [27.4,  23.0,  9.4,  0.0]
    nearest = [63.2,  60.8, 60.4,  0.7]
    rag     = [88.5,  84.5, 79.2, 78.4]
    contrib = [61.1,  61.5, 69.7, 78.4]   # RAG contribution over exact

    x   = np.arange(len(models))
    w   = 0.25

    fig, ax = plt.subplots(figsize=(11, 6))
    fig.patch.set_facecolor(C_PANEL)
    ax.set_facecolor('#F7F9FC')

    b1 = ax.bar(x - w, exact,   width=w, label='LLM-only Exact',   color='#BDC3C7', zorder=2)
    b2 = ax.bar(x,     nearest, width=w, label='LLM-only Nearest', color=C_ORANGE,  zorder=2)
    b3 = ax.bar(x + w, rag,     width=w, label='RAG v2 Improved',  color=C_DARK_BLUE, zorder=2)

    for bar in [*b1, *b2, *b3]:
        bar.set_edgecolor('white')

    # value labels
    for bar, v in [(b, v) for b, v in zip(b1, exact)]:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.8,
                f'{v}%', ha='center', va='bottom', fontsize=8.5, color='#5D6D7E')
    for bar, v in zip(b2, nearest):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.8,
                f'{v}%', ha='center', va='bottom', fontsize=8.5, color='#784212')
    for bar, v, c in zip(b3, rag, contrib):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.8,
                f'{v}%', ha='center', va='bottom', fontsize=8.5, color=C_DARK_BLUE,
                fontweight='bold')
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 4,
                f'+{c}pp', ha='center', va='bottom', fontsize=8, color=C_GREEN,
                fontweight='bold')

    # 80% line
    ax.axhline(80, color='#E74C3C', linestyle='--', linewidth=1.3, zorder=3,
               label='80% practical threshold')

    ax.set_xticks(x)
    ax.set_xticklabels(models, fontsize=11)
    ax.set_ylabel('Accuracy (%)', fontsize=11)
    ax.set_ylim(0, 102)
    ax.set_title('LLM-only vs. RAG v2 — Accuracy Comparison\n'
                 '(Zero-shot without retrieval vs. RAG pipeline, same 457 GT pairs)',
                 fontsize=12, fontweight='bold', color=C_DARK_BLUE, pad=10)
    ax.legend(fontsize=10, loc='upper right', framealpha=0.9)
    ax.grid(axis='y', linestyle=':', alpha=0.5, zorder=1)
    ax.spines[['top', 'right']].set_visible(False)

    # annotation: deepseek case
    ax.annotate('Korean generation\nimpossible without RAG\n(0% → 78.4%)',
                xy=(x[-1] + w, rag[-1]),
                xytext=(x[-1] + w + 0.5, rag[-1] - 15),
                fontsize=8.5, color='#922B21',
                arrowprops=dict(arrowstyle='->', color='#922B21', lw=1.2))

    plt.tight_layout()
    out = os.path.join(OUTDIR, 'fig4_llm_rag_comparison.png')
    fig.savefig(out, dpi=DPI, bbox_inches='tight', facecolor=C_PANEL)
    plt.close(fig)
    print(f'  saved: {out}')


# ══════════════════════════════════════════════════════════════════════════════
# FIG 5 — Type × Model Heatmap  (Results 3.2 cross-analysis)
# ══════════════════════════════════════════════════════════════════════════════
def fig5_heatmap():
    model_labels = [
        'gemma4\n:e4b', 'gemma3\n:4b', 'granite4.1\n:8b', 'gemma4\n:e2b',
        'exaone3.5\n:7.8b', 'deepseek-r1\n:8b', 'deepseek-r1\n:1.5b',
        'exaone3.5\n:2.4b', 'granite4.1\n:3b',
    ]
    type_labels = [
        'Power source\n(n=55)', 'Metadata\n(n=22)', 'Attribute\n(n=40)',
        'Typos\n(n=145)', 'Brand\n(n=72)', 'Set/kit\n(n=26)',
        'English abbr.\n(n=40)', 'Other\n(n=27)', 'Japanese\n(n=17)',
    ]
    data = np.array([
        [96.4, 85.5, 87.3, 83.6, 78.2, 81.8, 81.1, 78.2, 74.5],
        [95.5, 86.4, 90.9, 86.4, 90.9, 86.4, 77.3, 68.2, 90.9],
        [95.0, 92.5, 82.5, 92.5, 85.0, 80.0, 85.0, 80.0, 50.0],
        [93.8, 88.3, 93.1, 80.7, 82.1, 85.5, 88.3, 86.2, 71.7],
        [87.5, 84.7, 76.4, 86.1, 73.6, 73.6, 72.2, 68.1, 70.8],
        [84.6, 88.5, 84.6, 84.6, 96.2, 80.8, 84.6, 84.6, 61.5],
        [82.5, 82.5, 72.5, 85.0, 75.0, 70.0, 72.5, 67.5, 67.5],
        [66.7, 63.0, 59.3, 66.7, 70.4, 63.0, 59.3, 44.4, 63.0],
        [47.1, 52.9, 41.2, 23.5, 47.1, 29.4, 35.3, 23.5, 23.5],
    ])

    fig, ax = plt.subplots(figsize=(13, 7))
    fig.patch.set_facecolor(C_PANEL)

    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list(
        'rag', ['#C0392B', '#E67E22', '#F1C40F', '#2ECC71', '#1A3A6B'])

    im = ax.imshow(data, cmap=cmap, vmin=20, vmax=100, aspect='auto')

    ax.set_xticks(np.arange(len(model_labels)))
    ax.set_xticklabels(model_labels, fontsize=8.5)
    ax.set_yticks(np.arange(len(type_labels)))
    ax.set_yticklabels(type_labels, fontsize=9.5)
    ax.set_xlabel('Model', fontsize=11)
    ax.set_ylabel('Dirty Data Type', fontsize=11)

    # cell annotations
    for i in range(len(type_labels)):
        for j in range(len(model_labels)):
            val = data[i, j]
            tc  = 'white' if val < 55 else 'black'
            ax.text(j, i, f'{val:.0f}', ha='center', va='center',
                    fontsize=8, color=tc, fontweight='bold' if val == data[i].max() else 'normal')

    cbar = plt.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
    cbar.set_label('Accuracy (%)', fontsize=10)

    ax.set_title('Accuracy Heatmap: Dirty Data Type × Model\n'
                 '(RAG v2 Improved; bold = row maximum)',
                 fontsize=12, fontweight='bold', color=C_DARK_BLUE, pad=10)

    # draw a red rectangle around Japanese row (structural failure)
    rect = mpatches.FancyBboxPatch((-0.5, 7.5), len(model_labels),  1,
                                    boxstyle='round,pad=0.05',
                                    linewidth=2, edgecolor='#E74C3C',
                                    facecolor='none')
    ax.add_patch(rect)
    ax.text(len(model_labels) - 0.3, 8, 'Structural\nfailure',
            ha='left', va='center', fontsize=8, color='#C0392B', fontweight='bold')

    ax.spines[['top', 'right', 'left', 'bottom']].set_visible(False)
    ax.tick_params(top=False, bottom=True, left=True, right=False)

    plt.tight_layout()
    out = os.path.join(OUTDIR, 'fig5_type_heatmap.png')
    fig.savefig(out, dpi=DPI, bbox_inches='tight', facecolor=C_PANEL)
    plt.close(fig)
    print(f'  saved: {out}')


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print('\nGenerating poster figures...\n')
    fig1_pipeline()
    fig2_model_accuracy()
    fig3_type_accuracy()
    fig4_llm_rag()
    fig5_heatmap()
    print(f'\nAll figures saved to: {OUTDIR}\n')
