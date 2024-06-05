def cache_decorator(func):
    cache = {}
    print(cache)
    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for args: {args}")
            return cache[args]
        else:
            print(f"Cache miss for args: {args}")
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

@cache_decorator
def prime_numbers(n):
    def prime_generator():
        primes = []
        candidate = 2
        while len(primes) < n:
            if all(candidate % p != 0 for p in primes):
                primes.append(candidate)
                yield candidate
            candidate += 1

    return list(prime_generator())

print("First call (no cache):\n")
result1 = prime_numbers(10)
print(f"First 10 primes: {result1}\n")

print("Second call (should hit cache):\n")
result2 = prime_numbers(10)
print(f"First 10 primes: {result2}")
