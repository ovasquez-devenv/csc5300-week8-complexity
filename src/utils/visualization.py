"""Plot helpers. Each one saves a PNG into benchmarks/results/."""
from pathlib import Path


def plot_runtime_growth(rows: list[dict], out: Path) -> None:
    """Line chart: input size vs median seconds, one line per algorithm, log y axis."""
    raise NotImplementedError


def plot_approximation_quality(rows: list[dict], out: Path) -> None:
    """Line chart: input size vs approximation ratio (heuristic / optimal)."""
    raise NotImplementedError


def plot_tradeoff(rows: list[dict], out: Path) -> None:
    """Scatter: runtime vs approximation ratio."""
    raise NotImplementedError
