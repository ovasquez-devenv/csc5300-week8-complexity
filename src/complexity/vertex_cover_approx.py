"""Vertex Cover: 2-approximation and exact brute force for small graphs."""

Edge = tuple[int, int]


def vertex_cover_2approx(edges: list[Edge]) -> set[int]:
    """Pick any uncovered edge, add both ends, repeat. O(V + E). Size <= 2 * optimal."""
    cover = set()
    for u, v in edges:
        if u not in cover and v not in cover:
            cover.add(u)
            cover.add(v)
    return cover


def vertex_cover_exact(n: int, edges: list[Edge]) -> set[int]:
    """Try covers of size 0, 1, 2, ... Only for small n (exponential)."""
    from itertools import combinations
    for k in range(n + 1):
        for combo in combinations(range(n), k):
            c = set(combo)
            if all(u in c or v in c for u, v in edges):
                return c
    return set(range(n))
