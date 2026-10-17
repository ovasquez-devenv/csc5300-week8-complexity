"""Plot helpers. Each one saves a PNG into benchmarks/results/."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def _lines(rows, key, ylabel, title, out, log=False):
    fig, ax = plt.subplots(figsize=(8, 5))
    pairs = sorted({(r["problem"], r["algorithm"]) for r in rows})
    for p, a in pairs:
        pts = sorted((r["n"], r[key], r[key.replace("_mean", "_std")]) for r in rows
                     if r["problem"] == p and r["algorithm"] == a)
        ax.errorbar([x[0] for x in pts], [x[1] for x in pts], yerr=[x[2] for x in pts],
                    marker="o", capsize=3, label=f"{p} {a}")
    if log:
        ax.set_yscale("log")
    ax.set_xlabel("input size n")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(out, dpi=120)
    plt.close(fig)


def plot_runtime_growth(rows: list[dict], out: Path) -> None:
    """Line chart: input size vs median seconds, one line per algorithm, log y axis."""
    _lines(rows, "seconds_mean", "seconds (log scale)", "Runtime growth, exact vs heuristic", out, log=True)


def plot_approximation_quality(rows: list[dict], out: Path) -> None:
    """Line chart: input size vs approximation ratio (heuristic / optimal)."""
    heur = [r for r in rows if r["algorithm"] in ("greedy", "random_walk", "2approx", "nearest_neighbor")]
    _lines(heur, "ratio_mean", "heuristic / optimal", "Approximation quality", out)


def plot_tradeoff(rows: list[dict], out: Path) -> None:
    """Scatter: runtime vs approximation ratio."""
    fig, ax = plt.subplots(figsize=(8, 5))
    for r in rows:
        ax.scatter(r["seconds_mean"], r["ratio_mean"], s=15 + r["n"] * 2)
        ax.annotate(f'{r["algorithm"]} {r["n"]}', (r["seconds_mean"], r["ratio_mean"]), fontsize=6)
    ax.set_xscale("log")
    ax.set_xlabel("seconds (log scale)")
    ax.set_ylabel("ratio")
    ax.set_title("Speed vs quality tradeoff")
    fig.tight_layout()
    fig.savefig(out, dpi=120)
    plt.close(fig)
