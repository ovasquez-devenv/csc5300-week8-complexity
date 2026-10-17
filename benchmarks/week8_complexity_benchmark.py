"""Benchmark Parts 2 and 3 on growing inputs and save results.

Writes benchmarks/results/comparison_table.csv and the three PNG charts.
All inputs come from make_rng(SEED), so reruns build the same data.
Sizes are set below. Change them only here, and record them in the report.
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.utils.rng import SEED, make_rng  # noqa: E402

RESULTS = Path(__file__).parent / "results"
SUBSET_SIZES = [10, 12, 14, 16, 18, 20]      # TODO Omar: adjust after a first run
SAT_VARS = [8, 10, 12, 14, 16]
VC_SIZES = [8, 10, 12, 14]                   # exact solver limits this
TSP_SIZES = [5, 6, 7, 8, 9]                  # exact solver limits this
CSV_FIELDS = ["problem", "algorithm", "n", "seconds", "solution_value", "optimal_value", "ratio"]


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    rng = make_rng(SEED)
    rows: list[dict] = []
    # TODO: for each problem and size, build input with rng, time exact and heuristic
    #       with src.utils.timer.time_call, append a row per algorithm.
    with open(RESULTS / "comparison_table.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        w.writeheader()
        w.writerows(rows)
    # TODO: call the three plot helpers in src.utils.visualization


if __name__ == "__main__":
    main()
