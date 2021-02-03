"""
Test Tabu
"""

# Modules
from src.utils import tabu_util


# def test_best_change_not_tabu():
#     """
#     Validate configuration based into tabu change
#     """
#     distance_matrix_test = [
#         [0, 100, 200],
#         [100, 0, 20],
#         [30, 10, 0],
#     ]
#     solution = [2, 0, 1]
#     expect = (30, (0, 1))
#     assert tabu_util.best_change_not_tabu(
#         distance_matrix_test,
#         solution
#     ) == expect
