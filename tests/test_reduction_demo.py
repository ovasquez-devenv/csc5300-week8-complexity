from src.complexity.reduction_demo import cover_from_assignment, is_vertex_cover, reduce_3sat_to_vc

CLAUSES = [(1, 2, 3), (-1, -2, 3)]


def test_sizes_match_construction():
    inst = reduce_3sat_to_vc(3, CLAUSES)
    assert len(inst.vertices) == 2 * 3 + 3 * 2
    assert len(inst.edges) == 3 + 6 * 2
    assert inst.k == 3 + 2 * 2


def test_satisfying_assignment_gives_cover_of_size_k():
    inst = reduce_3sat_to_vc(3, CLAUSES)
    cover = cover_from_assignment(3, CLAUSES, {1: True, 2: False, 3: True})
    assert len(cover) == inst.k
    assert is_vertex_cover(inst.edges, cover)
