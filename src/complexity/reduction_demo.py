"""3-SAT to Vertex Cover reduction (the textbook gadget construction).

For a formula with n variables and m clauses:
  * each variable x gets an edge (x, not x)          -> 2n vertices, n edges
  * each clause gets a triangle of 3 vertices        -> 3m vertices, 3m edges
  * each triangle corner is joined to its literal    -> 3m edges
The formula is satisfiable iff the graph has a vertex cover of size k = n + 2m.
The construction is polynomial: O(n + m) vertices and edges.
"""
from dataclasses import dataclass

Literal = int            # +i means x_i, -i means not x_i (DIMACS style)
Clause = tuple[Literal, Literal, Literal]


@dataclass
class VCInstance:
    vertices: list[str]
    edges: list[tuple[str, str]]
    k: int


def reduce_3sat_to_vc(num_vars: int, clauses: list[Clause], verbose: bool = False) -> VCInstance:
    """Build the Vertex Cover instance. If verbose, print each step."""
    def lit(l):
        return f"x{l}" if l > 0 else f"~x{-l}"

    vertices, edges = [], []
    for i in range(1, num_vars + 1):
        vertices += [f"x{i}", f"~x{i}"]
        edges.append((f"x{i}", f"~x{i}"))
        if verbose:
            print(f"variable x{i}: edge x{i} -- ~x{i}")
    for j, clause in enumerate(clauses):
        corners = [f"c{j}_{p}" for p in range(3)]
        vertices += corners
        edges += [(corners[0], corners[1]), (corners[1], corners[2]), (corners[0], corners[2])]
        for corner, l in zip(corners, clause):
            edges.append((corner, lit(l)))
        if verbose:
            print(f"clause {j} {clause}: triangle {corners}, linked to {[lit(l) for l in clause]}")
    k = num_vars + 2 * len(clauses)
    if verbose:
        print(f"{len(vertices)} vertices, {len(edges)} edges, k = {k}")
    return VCInstance(vertices, edges, k)


def cover_from_assignment(num_vars: int, clauses: list[Clause], assignment: dict[int, bool]) -> set[str]:
    """Turn a satisfying assignment into a cover of size k (used in tests)."""
    cover = set()
    for i in range(1, num_vars + 1):
        cover.add(f"x{i}" if assignment[i] else f"~x{i}")
    for j, clause in enumerate(clauses):
        true_spot = next(p for p, l in enumerate(clause) if assignment[abs(l)] == (l > 0))
        for p in range(3):
            if p != true_spot:
                cover.add(f"c{j}_{p}")
    return cover


def is_vertex_cover(edges: list[tuple[str, str]], cover: set[str]) -> bool:
    return all(u in cover or v in cover for u, v in edges)
