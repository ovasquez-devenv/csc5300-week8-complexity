"""TSP: Nearest Neighbor heuristic and exact brute force for small n."""
import math
from itertools import permutations

Point = tuple[float, float]


def tour_length(points: list[Point], tour: list[int]) -> float:
    """Total length including the return to the start."""
    total = 0.0
    for i in range(len(tour)):
        a = points[tour[i]]
        b = points[tour[(i + 1) % len(tour)]]
        total += math.dist(a, b)
    return total


def tsp_nearest_neighbor(points: list[Point], start: int = 0) -> list[int]:
    """Always go to the closest unvisited city. O(n^2)."""
    tour = [start]
    left = set(range(len(points))) - {start}
    while left:
        here = points[tour[-1]]
        nxt = min(left, key=lambda c: math.dist(here, points[c]))
        tour.append(nxt)
        left.remove(nxt)
    return tour


def tsp_exact(points: list[Point]) -> list[int]:
    """Try every tour that starts at 0. O(n!). Keep n around 9 or less."""
    n = len(points)
    best, best_len = None, float("inf")
    for rest in permutations(range(1, n)):
        tour = [0, *rest]
        length = tour_length(points, tour)
        if length < best_len:
            best, best_len = tour, length
    return best
