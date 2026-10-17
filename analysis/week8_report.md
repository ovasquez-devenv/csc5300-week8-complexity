# Week 8 Technical Report: Computational Complexity

Omar Vasquez, CSC 5300

Target length: 1200 to 1500 words. Fill every number from `benchmarks/results/comparison_table.csv` after you run the benchmark. Do not type numbers that did not come from your run.

## Executive Summary
- What I built (five parts).
- Two or three key findings from my run. TODO after benchmark.

## Methodology
- Machine and Python version: TODO.
- Seed: 5300, set in `src/utils/rng.py`.
- Input sizes for each problem (copy from the benchmark script).
- How inputs are made: random graphs with edge probability p, random points in a 100 by 100 square, random 3-CNF, random integers for subset sum.
- Timing: median of 5 runs with `time.perf_counter`.
- Metric for quality: approximation ratio = heuristic value / exact value.

## Results
- Table: runtime by n for each algorithm (from the CSV).
- Figure: `benchmarks/results/runtime_growth.png`.
- Figure: `benchmarks/results/approximation_quality.png`.
- Figure: trade off chart.
- One or two sentences under each that say what the chart shows.

## Discussion
- P, NP, NP-hard, NP-complete in my own words.
- Why no polynomial algorithm is known for NP-complete problems, and what P vs NP asks.
- What the 3-SAT to Vertex Cover reduction shows and why it runs in polynomial time.
- Why the exponential curves explode: compare my measured growth to O(2^n) and O(n!).
- Vertex Cover ratio vs the proven bound of 2. TSP nearest neighbor has no constant bound in general.
- Limits: small n, one machine, one seed.

## Conclusion
- How knowing a problem is NP-complete changes how I would pick an algorithm.
- What I would improve next time.

## References
- Only sources I actually used. TODO.
