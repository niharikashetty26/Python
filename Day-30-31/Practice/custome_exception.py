class NegativeValueError(Exception):
    pass


def check_positive(n):
    if n < 0:
        raise NegativeValueError("Negative value error")
    return n


try:
    print(check_positive(10))
    print(check_positive(-5))
except NegativeValueError as e:
    print(e)