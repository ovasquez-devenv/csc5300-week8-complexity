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
    raise NotImplementedError


def cover_from_assignment(num_vars: int, clauses: list[Clause], assignment: dict[int, bool]) -> set[str]:
    """Turn a satisfying assignment into a cover of size k (used in tests)."""
    raise NotImplementedError


def is_vertex_cover(edges: list[tuple[str, str]], cover: set[str]) -> bool:
    return all(u in cover or v in cover for u, v in edges)
