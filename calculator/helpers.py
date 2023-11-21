from calculator.constants import AVAILABLE_OPERATIONS
from calculator.exceptions import UnknownOperation, NotNumberError


def get_operation():
    print(str(AVAILABLE_OPERATIONS.keys()))
    entered_operation = input('Input you operation ')
    try:
        return AVAILABLE_OPERATIONS[entered_operation]
    except KeyError:
        raise UnknownOperation(entered_operation)


def get_nums():
    try:
        first_value = float(input('Enter you first value '))
        second_value = float(input('Enter you second value '))
        return first_value, second_value
    except ValueError:
        raise NotNumberError('This is not num')
