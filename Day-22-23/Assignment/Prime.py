def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 16, 17, 18, 25, 26, 27, 36, 49, 50]

for number in numbers:
    if is_prime(number):
        print(f"{number} is a prime number.")
