#!/usr/bin/env python3
"""
Differential expression analysis with PyDESeq2.

Usage:
    python run_pydeseq2.py \
        --counts  ../data/counts_matrix.csv \
        --metadata ../data/metadata.csv \
        --condition condition \
        --contrast treated control \
        --outdir ../results \
        --fdr 0.05 \
        --lfc 1.0
"""

import argparse
import os
import sys

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

try:
    from pydeseq2.dds import DeseqDataSet
    from pydeseq2.ds import DeseqStats
except ImportError:
    sys.exit("PyDESeq2 not found. Install with: pip install pydeseq2")

try:
    from adjustText import adjust_text
    HAS_ADJUSTTEXT = True
except ImportError:
    HAS_ADJUSTTEXT = False


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(description="PyDESeq2 differential expression pipeline")
    p.add_argument("--counts",    required=True, help="Counts matrix CSV (genes × samples)")
    p.add_argument("--metadata",  required=True, help="Metadata CSV (samples × variables)")
    p.add_argument("--condition", default="condition",
                   help="Column in metadata to use as design factor (default: condition)")
    p.add_argument("--contrast",  nargs=2, default=["treated", "control"],
                   metavar=("NUMERATOR", "DENOMINATOR"),
                   help="Contrast: numerator denominator (default: treated control)")
    p.add_argument("--outdir",    default="results", help="Output directory")
    p.add_argument("--fdr",       type=float, default=0.05, help="FDR threshold (default: 0.05)")
    p.add_argument("--lfc",       type=float, default=1.0,  help="|log2FC| threshold (default: 1.0)")
    p.add_argument("--top-genes", type=int,   default=50,   help="Top genes for heatmap (default: 50)")
    return p.parse_args()


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_data(counts_file, metadata_file, condition_col):
    counts = pd.read_csv(counts_file, index_col=0)
    meta   = pd.read_csv(metadata_file)

    # Auto-detect index column for metadata (first column that matches counts columns)
    for col in meta.columns:
        if set(meta[col]).issuperset(set(counts.columns)):
            meta = meta.set_index(col)
            break
    else:
        meta = meta.set_index(meta.columns[0])

    # Align samples
    common = [s for s in counts.columns if s in meta.index]
    if not common:
        sys.exit("No samples match between counts columns and metadata index.")
    counts = counts[common]
    meta   = meta.loc[common]

    if condition_col not in meta.columns:
        sys.exit(f"Column '{condition_col}' not found in metadata. "
                 f"Available: {list(meta.columns)}")

    print(f"Counts  : {counts.shape[0]} genes × {counts.shape[1]} samples")
    print(f"Metadata: {meta.shape}")
    print(f"Conditions: {meta[condition_col].value_counts().to_dict()}")
    return counts, meta


# ---------------------------------------------------------------------------
# Plots
# ---------------------------------------------------------------------------

def plot_library_sizes(counts, metadata, condition_col, outdir):
    lib = counts.sum(axis=0)
    cond = metadata.loc[lib.index, condition_col]
    uniq = cond.unique()
    palette = dict(zip(uniq, sns.color_palette("tab10", len(uniq))))
    colors = [palette[c] for c in cond]

    fig, ax = plt.subplots(figsize=(max(6, len(lib) * 0.8), 4))
    ax.bar(lib.index, lib.values / 1e6, color=colors)
    ax.set_ylabel("Library size (million reads)")
    ax.set_title("Library sizes per sample")
    ax.set_xticklabels(lib.index, rotation=45, ha="right")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=palette[c], label=c) for c in uniq])
    plt.tight_layout()
    fig.savefig(os.path.join(outdir, "library_sizes.png"), dpi=150)
    plt.close(fig)


def plot_pca(counts_norm, metadata, condition_col, outdir):
    log_norm = np.log2(counts_norm + 1)
    X = StandardScaler().fit_transform(log_norm.T.values)
    n_comp = min(4, X.shape[0])
    pca = PCA(n_components=n_comp)
    coords = pca.fit_transform(X)
    explained = pca.explained_variance_ratio_ * 100

    cond = metadata.loc[counts_norm.columns, condition_col]
    uniq = cond.unique()
    palette = dict(zip(uniq, sns.color_palette("tab10", len(uniq))))

    fig, ax = plt.subplots(figsize=(7, 5))
    for sample, c in zip(counts_norm.columns, cond):
        idx = list(counts_norm.columns).index(sample)
        ax.scatter(coords[idx, 0], coords[idx, 1], color=palette[c], s=100, zorder=3)
        ax.annotate(sample, (coords[idx, 0], coords[idx, 1]),
                    textcoords="offset points", xytext=(5, 4), fontsize=8)
    ax.axhline(0, color="gray", lw=0.5, ls="--")
    ax.axvline(0, color="gray", lw=0.5, ls="--")
    ax.set_xlabel(f"PC1 ({explained[0]:.1f}%)")
    ax.set_ylabel(f"PC2 ({explained[1]:.1f}%)")
    ax.set_title("PCA — log₂ normalized counts")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=palette[c], label=c) for c in uniq])
    plt.tight_layout()
    fig.savefig(os.path.join(outdir, "pca.png"), dpi=150)
    plt.close(fig)


def plot_volcano(results, fdr, lfc, contrast, outdir):
    res = results.dropna(subset=["padj", "log2FoldChange"]).copy()
    res["neg_log10_padj"] = -np.log10(res["padj"].clip(lower=1e-300))

    def cat(row):
        if row["padj"] < fdr and row["log2FoldChange"] > lfc:
            return "up"
        elif row["padj"] < fdr and row["log2FoldChange"] < -lfc:
            return "down"
        return "ns"

    res["cat"] = res.apply(cat, axis=1)
    cmap = {"up": "#e74c3c", "down": "#3498db", "ns": "#bdc3c7"}
    smap = {"up": 18, "down": 18, "ns": 6}

    fig, ax = plt.subplots(figsize=(9, 7))
    for c in ["ns", "down", "up"]:
        sub = res[res["cat"] == c]
        label = f"{c.capitalize()} ({len(sub)})" if c != "ns" else f"Not sig. ({len(sub)})"
        ax.scatter(sub["log2FoldChange"], sub["neg_log10_padj"],
                   c=cmap[c], s=smap[c], alpha=0.7, label=label, linewidths=0)

    ax.axhline(-np.log10(fdr), color="black", ls="--", lw=0.8, alpha=0.7)
    ax.axvline( lfc, color="black", ls="--", lw=0.8, alpha=0.7)
    ax.axvline(-lfc, color="black", ls="--", lw=0.8, alpha=0.7)

    top = res[res["cat"] != "ns"].nlargest(15, "neg_log10_padj")
    texts = [ax.text(r["log2FoldChange"], r["neg_log10_padj"], r.name, fontsize=7)
             for _, r in top.iterrows()]
    if HAS_ADJUSTTEXT:
        adjust_text(texts, ax=ax, arrowprops=dict(arrowstyle="-", color="gray", lw=0.5))

    ax.set_xlabel(f"log₂FC ({contrast[0]} / {contrast[1]})", fontsize=11)
    ax.set_ylabel("-log₁₀(adjusted p-value)", fontsize=11)
    ax.set_title(f"Volcano plot: {contrast[0]} vs {contrast[1]}", fontsize=12)
    ax.legend(fontsize=9)
    plt.tight_layout()
    fig.savefig(os.path.join(outdir, "volcano_plot.png"), dpi=150)
    plt.close(fig)


def plot_heatmap(results, counts_norm, fdr, lfc, top_n, outdir):
    sig = results[(results["padj"] < fdr) & (results["log2FoldChange"].abs() > lfc)]
    sig = sig.nsmallest(top_n, "padj")
    if len(sig) == 0:
        print("No significant genes for heatmap — skipping.")
        return

    log_norm = np.log2(counts_norm.loc[sig.index] + 1)
    z = log_norm.subtract(log_norm.mean(axis=1), axis=0)
    z = z.divide(log_norm.std(axis=1).replace(0, 1), axis=0)

    g = sns.clustermap(z, cmap="RdBu_r", vmin=-2.5, vmax=2.5,
                       col_cluster=False, row_cluster=True,
                       figsize=(8, min(14, 4 + len(sig) * 0.25)),
                       yticklabels=True, xticklabels=True,
                       dendrogram_ratio=(0.1, 0.05))
    g.ax_heatmap.set_title(f"Top {len(sig)} DE genes (z-score)", pad=15)
    g.figure.savefig(os.path.join(outdir, "heatmap_top_de.png"), dpi=150, bbox_inches="tight")
    plt.close(g.figure)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    os.makedirs(args.outdir, exist_ok=True)

    print("\n── Loading data ──────────────────────────────────")
    counts, metadata = load_data(args.counts, args.metadata, args.condition)

    print("\n── Library sizes ─────────────────────────────────")
    plot_library_sizes(counts, metadata, args.condition, args.outdir)

    print("\n── Size factor normalization ─────────────────────")
    counts_nz = counts[(counts > 0).all(axis=1)]
    log_c = np.log(counts_nz)
    geo_mean = np.exp(log_c.mean(axis=1))
    ratios = counts_nz.div(geo_mean, axis=0)
    size_factors = ratios.median(axis=0)
    counts_norm = counts.div(size_factors, axis=1)
    print("Size factors:", size_factors.round(4).to_dict())

    print("\n── PCA ───────────────────────────────────────────")
    plot_pca(counts_norm, metadata, args.condition, args.outdir)

    print("\n── DESeq2 ────────────────────────────────────────")
    dds = DeseqDataSet(
        counts=counts.T,
        metadata=metadata,
        design_factors=args.condition,
        refit_cooks=True,
        quiet=False
    )
    dds.deseq2()

    stat_res = DeseqStats(
        dds,
        contrast=(args.condition, args.contrast[0], args.contrast[1]),
        alpha=args.fdr
    )
    stat_res.summary()
    results = stat_res.results_df.copy()

    print("\n── Saving results ────────────────────────────────")
    results.to_csv(os.path.join(args.outdir, "deseq2_results_all.csv"))

    sig = results[
        (results["padj"] < args.fdr) &
        (results["log2FoldChange"].abs() > args.lfc)
    ].sort_values("padj")
    sig.to_csv(os.path.join(args.outdir, "deseq2_results_significant.csv"))

    print(f"\nSignificant genes (|log2FC| > {args.lfc}, FDR < {args.fdr}): {len(sig)}")
    print(f"  Up-regulated:   {(sig['log2FoldChange'] > 0).sum()}")
    print(f"  Down-regulated: {(sig['log2FoldChange'] < 0).sum()}")

    print("\n── Plots ─────────────────────────────────────────")
    plot_volcano(results, args.fdr, args.lfc, args.contrast, args.outdir)
    plot_heatmap(results, counts_norm, args.fdr, args.lfc, args.top_genes, args.outdir)

    print(f"\n✓ Done. Results in: {args.outdir}/")


if __name__ == "__main__":
    main()
