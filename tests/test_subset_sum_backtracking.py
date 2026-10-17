from src.complexity.subset_sum_backtracking import subset_sum_backtracking, subset_sum_greedy


def test_finds_subset():
    s = subset_sum_backtracking([3, 34, 4, 12, 5, 2], 9)
    assert s is not None and sum(s) == 9


def test_no_subset():
    assert subset_sum_backtracking([2, 4, 6], 5) is None


def test_greedy_never_overshoots():
    assert sum(subset_sum_greedy([8, 6, 5, 3], 12)) <= 12
