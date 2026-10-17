"""Small DFS / backtracking SAT solver for small CNF formulas."""
import random

Clause = tuple[int, ...]


def solve_sat(num_vars: int, clauses: list[Clause]) -> dict[int, bool] | None:
    """Return a satisfying assignment or None. Worst case O(2^n * m)."""
    assign = {}

    def ok(clause):
        return any(assign.get(abs(l)) == (l > 0) for l in clause)

    def broken(clause):
        return all(abs(l) in assign and assign[abs(l)] != (l > 0) for l in clause)

    def go(v):
        if any(broken(c) for c in clauses):
            return False
        if v > num_vars:
            return all(ok(c) for c in clauses)
        for val in (True, False):
            assign[v] = val
            if go(v + 1):
                return True
        del assign[v]
        return False

    return dict(assign) if go(1) else None


def random_walk_sat(num_vars: int, clauses: list[Clause], rng: random.Random, max_flips: int = 1000) -> dict[int, bool] | None:
    """Fast heuristic for comparison. May miss a solution. Never claims unsat."""
    assign = {v: rng.random() < 0.5 for v in range(1, num_vars + 1)}
    for _ in range(max_flips):
        bad = [c for c in clauses if not any(assign[abs(l)] == (l > 0) for l in c)]
        if not bad:
            return assign
        v = abs(rng.choice(rng.choice(bad)))
        assign[v] = not assign[v]
    return None


def random_3cnf(num_vars: int, num_clauses: int, rng: random.Random) -> list[Clause]:
    """Random 3-CNF formula with distinct variables in each clause."""
    out = []
    for _ in range(num_clauses):
        vs = rng.sample(range(1, num_vars + 1), 3)
        out.append(tuple(v if rng.random() < 0.5 else -v for v in vs))
    return out
