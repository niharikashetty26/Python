def decorator_1(func):
    def wrapper_function1(a, b):
        print("This is the wrapper_function 1")
        result = func(a, b)
        return result
    return wrapper_function1

def decorator_2(func):
    def wrapper_function2(a, b):
        print("This is the wrapper_function 2")
        result = func(a, b)
        return result
    return wrapper_function2

@decorator_1
@decorator_2
def add(a, b):
    return a + b

print(add(1, 2))







