from src.complexity.vertex_cover_approx import vertex_cover_2approx, vertex_cover_exact
from src.utils.graph_utils import random_graph
from src.utils.rng import make_rng


def covers(edges, c):
    return all(u in c or v in c for u, v in edges)


def test_approx_is_cover_and_within_2x():
    rng = make_rng()
    for n in (6, 8, 10):
        edges = random_graph(n, 0.4, rng)
        approx = vertex_cover_2approx(edges)
        exact = vertex_cover_exact(n, edges)
        assert covers(edges, approx) and covers(edges, exact)
        assert len(approx) <= 2 * len(exact)
