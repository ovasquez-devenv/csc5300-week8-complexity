"""Short walk through of each part on tiny inputs."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def main() -> None:
    # TODO: verbose 3-SAT -> VC reduction on a 2 clause formula
    # TODO: subset sum on [3, 34, 4, 12, 5, 2] target 9
    # TODO: vertex cover approx vs exact on a small graph
    # TODO: TSP nearest neighbor vs exact on 6 seeded points
    pass


if __name__ == "__main__":
    main()
