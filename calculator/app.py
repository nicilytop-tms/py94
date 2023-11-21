from calculator.helpers import get_operation, get_nums
from calculator.exceptions import UnknownOperation, NotNumberError


def app():
    while True:
        try:
            operation = get_operation()
            data = get_nums()

            result = operation(*data)
            print(result)
        except (ZeroDivisionError, UnknownOperation, NotNumberError) as e:
            print(e)


app()
