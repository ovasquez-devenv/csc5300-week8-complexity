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
from statistics import mean, stdev
from src.utils.timer import time_call
from src.utils.graph_utils import random_graph, random_points
from src.complexity.subset_sum_backtracking import subset_sum_backtracking, subset_sum_greedy
from src.complexity.satisfiability_solver import solve_sat, random_walk_sat, random_3cnf
from src.complexity.vertex_cover_approx import vertex_cover_2approx, vertex_cover_exact
from src.complexity.traveling_salesman_approx import tsp_exact, tsp_nearest_neighbor, tour_length
from src.utils import visualization as viz

TRIALS = 5

RESULTS = Path(__file__).parent / "results"
SUBSET_SIZES = [10, 12, 14, 16, 18, 20]      # TODO Omar: adjust after a first run
SAT_VARS = [8, 10, 12, 14, 16]
VC_SIZES = [8, 10, 12, 14]                   # exact solver limits this
TSP_SIZES = [5, 6, 7, 8, 9]                  # exact solver limits this
CSV_FIELDS = ["problem", "algorithm", "n", "seconds_mean", "seconds_std", "ratio_mean", "ratio_std"]


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    rng = make_rng(SEED)
    rows: list[dict] = []
    def add(problem, algo, n, secs, ratios):
        rows.append({"problem": problem, "algorithm": algo, "n": n,
                     "seconds_mean": mean(secs), "seconds_std": stdev(secs),
                     "ratio_mean": mean(ratios), "ratio_std": stdev(ratios)})

    for n in SUBSET_SIZES:
        es, gs, gr = [], [], []
        for _ in range(TRIALS):
            nums = [rng.randint(1, 1000) for _ in range(n)]
            target = sum(rng.sample(nums, n // 2))
            t, _ = time_call(subset_sum_backtracking, nums, target, repeats=1); es.append(t)
            t, g = time_call(subset_sum_greedy, nums, target, repeats=1); gs.append(t)
            gr.append(sum(g) / target)
        add("subset_sum", "backtracking", n, es, [1.0] * TRIALS)
        add("subset_sum", "greedy", n, gs, gr)
        print("subset sum done n =", n)
    for n in SUBSET_SIZES:
        ws = []
        for _ in range(TRIALS):
            nums = [2 * rng.randint(1, 500) for _ in range(n)]
            target = sum(nums) // 2 + 1
            if target % 2 == 0:
                target += 1
            t, ans = time_call(subset_sum_backtracking, nums, target, repeats=1)
            assert ans is None
            ws.append(t)
        add("subset_sum_worst", "backtracking", n, ws, [1.0] * TRIALS)
        print("subset sum worst case done n =", n)
    for n in SAT_VARS:
        es, ws, wr = [], [], []
        for _ in range(TRIALS):
            clauses = random_3cnf(n, round(4.26 * n), rng)
            t, exact = time_call(solve_sat, n, clauses, repeats=1); es.append(t)
            t, walk = time_call(random_walk_sat, n, clauses, rng, repeats=1); ws.append(t)
            wr.append(1.0 if (walk is not None or exact is None) else 0.0)
        add("sat", "backtracking", n, es, [1.0] * TRIALS)
        add("sat", "random_walk", n, ws, wr)
        print("sat done n =", n)

    for n in VC_SIZES:
        es, as_, ar = [], [], []
        for _ in range(TRIALS):
            edges = random_graph(n, 0.4, rng)
            t, ex = time_call(vertex_cover_exact, n, edges, repeats=1); es.append(t)
            t, ap = time_call(vertex_cover_2approx, edges, repeats=1); as_.append(t)
            ar.append(len(ap) / len(ex) if ex else 1.0)
        add("vertex_cover", "exact", n, es, [1.0] * TRIALS)
        add("vertex_cover", "2approx", n, as_, ar)
        print("vertex cover done n =", n)

    for n in TSP_SIZES:
        es, ns, nr = [], [], []
        for _ in range(TRIALS):
            pts = random_points(n, rng)
            t, ex = time_call(tsp_exact, pts, repeats=1); es.append(t)
            t, nn = time_call(tsp_nearest_neighbor, pts, repeats=1); ns.append(t)
            nr.append(tour_length(pts, nn) / tour_length(pts, ex))
        add("tsp", "exact", n, es, [1.0] * TRIALS)
        add("tsp", "nearest_neighbor", n, ns, nr)
        print("tsp done n =", n)
    with open(RESULTS / "comparison_table.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        w.writeheader()
        w.writerows(rows)
    viz.plot_runtime_growth(rows, RESULTS / "runtime_growth.png")
    viz.plot_approximation_quality(rows, RESULTS / "approximation_quality.png")
    viz.plot_tradeoff(rows, RESULTS / "tradeoff.png")
    print("saved CSV and charts to", RESULTS)


if __name__ == "__main__":
    main()
