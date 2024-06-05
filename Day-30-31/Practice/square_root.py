import math


def calculate_value(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(x)


def check():
    try:
        result = calculate_value(-10)
        print(f"The square root is {result}")
    except ValueError as e:
        print(e)


check()
