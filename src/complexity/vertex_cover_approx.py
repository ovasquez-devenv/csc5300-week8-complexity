"""Vertex Cover: 2-approximation and exact brute force for small graphs."""

Edge = tuple[int, int]


def vertex_cover_2approx(edges: list[Edge]) -> set[int]:
    """Pick any uncovered edge, add both ends, repeat. O(V + E). Size <= 2 * optimal."""
    raise NotImplementedError


def vertex_cover_exact(n: int, edges: list[Edge]) -> set[int]:
    """Try covers of size 0, 1, 2, ... Only for small n (exponential)."""
    raise NotImplementedError
