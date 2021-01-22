"""
Process test csv
"""

# Modules
from src.utils import csv_util


def test_csv_read_file():
    """
    Read file
    """
    file_test = 'tests/unit/utils/test_base.csv'
    data = [
        {'a': '1', 'b': '2'},
        {'a': '3', 'b': '4'},
        {'a': '5', 'b': '6'},
    ]
    read_csv = csv_util.read_file(file_test)
    assert data == read_csv
