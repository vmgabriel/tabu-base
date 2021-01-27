"""
Math Test Module
"""

# Modules
from src.utils import math_util


def test_math_euclidean_vector_distance():
    """
    test data math for euclidean vector distance
    """
    vec1 = (10, 20)
    vec2 = (20, 30)
    expect = 14.142135623730951
    assert math_util.euclidean_vector_distance(vec1, vec2) == expect


def test_math_matrix_distance():
    """
    Verify the matrix of distance
    """
    data = [{'a': 14, 'b': 22}, {'a': 17, 'b': 3}]
    expect = [[0.0, 19.235384061671343], [19.235384061671343, 0.0]]
    assert math_util.matrix_distance(data, 'a', 'b') == expect


def test_math_negative_matrix():
    """
    Verify the negative convertion of matrix
    """
    data = [1, 2, 3, 4]
    expect = [-1, -2, -3, -4]
    assert math_util.list_negative(data) == expect


def test_change_position_list():
    """
    Verify the change of position in list
    """
    data = [1, 2, 3]
    expect = [1, 3, 2]
    assert math_util.invert_positions(data, 1, 2) == expect


def test_fo():
    """
    test the fo
    """
    distance_matrix_test = [
        [0, 100, 200],
        [100, 0, 20],
        [30, 10, 0],
    ]
    solution = [0, 2, 1]
    expect = 30
    assert math_util.evaluate_fo(distance_matrix_test, solution) == expect
