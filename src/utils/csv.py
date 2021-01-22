"""
Csv Module
"""

# Libraries
from csv import DictReader


def read_file(file_path: str, delimiter: str = ',') -> dict:
    """
    Read a File, configuration of csv
    file_path: str [required] - file complete path for read
    delimiter: str {default: ','} delimiter of csv

    return dict
    ex:
    in:
    a,b
    1,2
    3,4

    out:
    [
    {a:1,b:2},
    {a:3,b:4}
    ]
    """
    with open(file_path) as csv_file:
        return list(DictReader(csv_file, delimiter=delimiter))
