"""
Test of greedy
"""

# Modules
from src.utils import greedy_util


def test_neghbord_most_near():
    """
    Test the most near neghbord for distance
    """
    distance_matrix_test = [
        [0, 100, 200],
        [100, 0, 20],
        [30, 10, 0],
    ]
    expect = [0, 2, 1]
    assert greedy_util.neghbord_most_near(distance_matrix_test) == expect


def test_worst_solution():
    """
    Test Configuration neghbord for worst solution
    """
    distance_matrix_test = [
        [0, 100, 200],
        [100, 0, 20],
        [30, 10, 0],
    ]
    expect = [0, 2, 1]
    assert greedy_util.worst_solution(distance_matrix_test) == expect


def test_best_change_not_tabu():
    """
    Validate configuration based into tabu change
    """
    distance_matrix_test = [
        [0, 100, 200],
        [100, 0, 20],
        [30, 10, 0],
    ]
    solution = [2, 0, 1]
    expect = (30, (0, 1))
    assert greedy_util.best_change_not_tabu(
        distance_matrix_test,
        solution
    ) == expect


def test_search_local():
    """
    Generate local search
    """
    distance_matrix_test = [
        [0, 100, 200],
        [100, 0, 20],
        [30, 10, 0],
    ]
    solution = [2, 0, 1]
    expect = (3, 150, [1, 0, 2])
    assert greedy_util.generate_local_search(
        distance_matrix_test,
        solution
    ) == expect
