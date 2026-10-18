"""Short walk through of each part on tiny inputs."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def main() -> None:
    from src.utils.rng import make_rng
    from src.utils.graph_utils import random_graph, random_points
    from src.complexity.reduction_demo import reduce_3sat_to_vc, cover_from_assignment, is_vertex_cover
    from src.complexity.subset_sum_backtracking import subset_sum_backtracking, subset_sum_greedy
    from src.complexity.vertex_cover_approx import vertex_cover_2approx, vertex_cover_exact
    from src.complexity.traveling_salesman_approx import tsp_nearest_neighbor, tsp_exact, tour_length

    rng = make_rng()
    
    print("=== Part 1: 3-SAT to Vertex Cover ===")
    clauses = [(1, 2, 3), (-1, -2, 3)]
    vc = reduce_3sat_to_vc(3, clauses, verbose=True)
    assignment = {1: True, 2: False, 3: True}
    cover = cover_from_assignment(3, clauses, assignment)
    print("assignment", assignment, "gives cover", sorted(cover))
    print("size", len(cover), "k =", vc.k, "valid cover:", is_vertex_cover(vc.edges, cover))

    print("\n=== Part 2: Subset sum ===")
    nums, target = [3, 34, 4, 12, 5, 2], 9
    print("backtracking:", subset_sum_backtracking(nums, target))
    g = subset_sum_greedy(nums, target)
    print("greedy:", g, "sum =", sum(g))

    print("\n=== Part 3: Vertex cover ===")
    edges = random_graph(8, 0.4, rng)
    print("edges:", edges)
    approx = vertex_cover_2approx(edges)
    exact = vertex_cover_exact(8, edges)
    print("2-approx:", sorted(approx), "size", len(approx))
    print("exact:   ", sorted(exact), "size", len(exact))
    print("ratio:", round(len(approx) / len(exact), 2))

    print("\n=== Part 4: TSP ===")
    pts = random_points(6, rng)
    nn = tsp_nearest_neighbor(pts)
    best = tsp_exact(pts)
    print("nearest neighbor:", nn, "length", round(tour_length(pts, nn), 2))
    print("exact:           ", best, "length", round(tour_length(pts, best), 2))
    print("ratio:", round(tour_length(pts, nn) / tour_length(pts, best), 3))

if __name__ == "__main__":
    main()
