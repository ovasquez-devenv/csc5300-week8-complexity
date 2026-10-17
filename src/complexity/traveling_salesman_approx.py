"""TSP: Nearest Neighbor heuristic and exact brute force for small n."""

Point = tuple[float, float]


def tour_length(points: list[Point], tour: list[int]) -> float:
    """Total length including the return to the start."""
    raise NotImplementedError


def tsp_nearest_neighbor(points: list[Point], start: int = 0) -> list[int]:
    """Always go to the closest unvisited city. O(n^2)."""
    raise NotImplementedError


def tsp_exact(points: list[Point]) -> list[int]:
    """Try every tour that starts at 0. O(n!). Keep n around 9 or less."""
    raise NotImplementedError
