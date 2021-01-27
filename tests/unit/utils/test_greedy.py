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
