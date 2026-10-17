"""Subset Sum: exact backtracking vs a greedy heuristic."""


def subset_sum_backtracking(nums: list[int], target: int) -> list[int] | None:
    """Return a subset that sums to target, or None. Worst case O(2^n).
    Plan: sort descending, prune when the running sum passes target
    or when the remaining total cannot reach it."""
    nums = sorted(nums, reverse=True)
    suffix = [0] * (len(nums) + 1)
    for i in range(len(nums) - 1, -1, -1):
        suffix[i] = suffix[i + 1] + nums[i]

    picked = []

    def go(i, total):
        if total == target:
            return True
        if i == len(nums) or total > target or total + suffix[i] < target:
            return False
        picked.append(nums[i])
        if go(i + 1, total + nums[i]):
            return True
        picked.pop()
        return go(i + 1, total)

    return list(picked) if go(0, 0) else None


def subset_sum_greedy(nums: list[int], target: int) -> list[int]:
    """Sort descending, take each number that still fits. O(n log n). Not always exact."""
    picked = []
    total = 0
    for n in sorted(nums, reverse=True):
        if total + n <= target:
            picked.append(n)
            total += n
    return picked
