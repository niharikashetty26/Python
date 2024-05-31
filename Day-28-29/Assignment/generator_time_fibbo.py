import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result

    return wrapper


@timing_decorator
def first_n_fibonacci(n):
    def fibonacci_generator():
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    return list(fibonacci_generator())


# Using the decorated function
result = first_n_fibonacci(10)
print(f"Fibonacci numbers: {result}")
