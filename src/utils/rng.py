"""One place for the random seed so every run is repeatable."""
import random

SEED = 5300


def make_rng(seed: int = SEED) -> random.Random:
    """Return a private Random so modules never touch the global one."""
    return random.Random(seed)
