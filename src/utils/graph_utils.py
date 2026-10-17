"""Random graph and point builders. All take an rng so inputs are seeded."""
import math
import random

Edge = tuple[int, int]


def random_graph(n: int, p: float, rng: random.Random) -> list[Edge]:
    """Erdos Renyi style graph: each pair (u, v), u < v, is an edge with probability p."""
    return [(u, v) for u in range(n) for v in range(u + 1, n) if rng.random() < p]


def random_points(n: int, rng: random.Random, size: float = 100.0) -> list[tuple[float, float]]:
    """n random points in a size x size square, for TSP."""
    return [(rng.uniform(0, size), rng.uniform(0, size)) for _ in range(n)]


def distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    return math.dist(a, b)
