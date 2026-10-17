# CSC 5300 Week 8: Computational Complexity

Omar Vasquez

This project looks at problems that are easy (P) and problems we think are hard (NP complete). It has a 3-SAT to Vertex Cover reduction demo, a backtracking Subset Sum solver, a small DFS SAT solver, a 2-approximation for Vertex Cover, and a Nearest Neighbor heuristic for TSP. A benchmark script times them on growing inputs and saves charts and a CSV to `benchmarks/results/`. The write up is in `analysis/week8_report.md`.

## Install

Python 3.12 or newer.

```
python -m venv .venv
.venv\Scripts\activate          (Windows)
pip install -r requirements.txt
```

## Run

```
python examples/week8_demo.py
python benchmarks/week8_complexity_benchmark.py
```

The benchmark uses a fixed seed (`SEED = 5300` in `src/utils/rng.py`) so every run builds the same inputs.

## Tests

```
python -m pytest -q
```

## Layout

```
src/complexity/   reduction_demo, satisfiability_solver, subset_sum_backtracking,
                  vertex_cover_approx, traveling_salesman_approx
src/utils/        timer, graph_utils, visualization, rng
benchmarks/       week8_complexity_benchmark.py and results/
tests/            pytest files
analysis/         week8_report.md
examples/         week8_demo.py
```

## AI assistance

AI assistance disclosure: TODO Omar, write one line here in your own words saying what help you used and what you wrote and checked yourself.
