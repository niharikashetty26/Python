numbers = [2, 3, 4, 16, 17, 18, 25, 26, 27, 36, 49, 50]

sum_even = 0
sum_odd = 0

for number in numbers:
    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

print(f"Sum of even numbers: {sum_even}")
print(f"Sum of odd numbers: {sum_odd}")
