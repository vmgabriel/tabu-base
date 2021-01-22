"""
Test Input Control for Exception
"""

# Modules
from src.exceptions import input_exception


def test_module_invalidinput():
    """Test control for class exception"""
    valid_control = ['t', 'f']
    mocks_control = [
        ('t', True),
        ('f', True),
        ('n', False),
        ('7', False),
    ]

    def module_control_input(data: str) -> bool:
        """Control for Use of exception"""
        if data not in valid_control:
            raise input_exception.InvalidInput(data)
        return True

    for data, wait_response in mocks_control:
        return_valid = True
        try:
            return_valid = module_control_input(data)
        except input_exception.InvalidInput:
            return_valid = False
        assert return_valid == wait_response


def test_module_message_invalidinput():
    """Test control for class message"""
    expect = '[Input-Error] - test not valid.'

    def gen_invalid_input(gen_exception: bool) -> bool:
        """Control for Use of exception"""
        if gen_exception:
            raise input_exception.InvalidInput('test')
        return True

    try:
        gen_invalid_input(True)
    except input_exception.InvalidInput as exc:
        assert str(exc) == expect
