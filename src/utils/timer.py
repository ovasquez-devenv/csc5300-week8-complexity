"""Simple timing helper for the benchmarks."""
import time
from statistics import median
from typing import Any, Callable


def time_call(fn: Callable[..., Any], *args: Any, repeats: int = 5) -> tuple[float, Any]:
    """Run fn(*args) `repeats` times. Return (median seconds, last result)."""
    times: list[float] = []
    result: Any = None
    for _ in range(repeats):
        start = time.perf_counter()
        result = fn(*args)
        times.append(time.perf_counter() - start)
    return median(times), result
