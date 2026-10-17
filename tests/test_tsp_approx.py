from src.complexity.traveling_salesman_approx import tour_length, tsp_exact, tsp_nearest_neighbor
from src.utils.graph_utils import random_points
from src.utils.rng import make_rng


def test_square_tour_length():
    pts = [(0, 0), (0, 1), (1, 1), (1, 0)]
    assert abs(tour_length(pts, [0, 1, 2, 3]) - 4.0) < 1e-9


def test_nn_visits_every_city_and_not_better_than_exact():
    pts = random_points(7, make_rng())
    nn = tsp_nearest_neighbor(pts)
    assert sorted(nn) == list(range(7))
    assert tour_length(pts, nn) >= tour_length(pts, tsp_exact(pts)) - 1e-9
