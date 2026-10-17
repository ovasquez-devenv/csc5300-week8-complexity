"""Small DFS / backtracking SAT solver for small CNF formulas."""
import random

Clause = tuple[int, ...]


def solve_sat(num_vars: int, clauses: list[Clause]) -> dict[int, bool] | None:
    """Return a satisfying assignment or None. Worst case O(2^n * m)."""
    raise NotImplementedError


def random_walk_sat(num_vars: int, clauses: list[Clause], rng: random.Random, max_flips: int = 1000) -> dict[int, bool] | None:
    """Fast heuristic for comparison. May miss a solution. Never claims unsat."""
    raise NotImplementedError


def random_3cnf(num_vars: int, num_clauses: int, rng: random.Random) -> list[Clause]:
    """Random 3-CNF formula with distinct variables in each clause."""
    raise NotImplementedError
