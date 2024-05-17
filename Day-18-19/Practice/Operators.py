# Arithmetic Operators
a = 5 + 3
b = 7 - 2
c = 4 * 6
d = 10 / 2
print("Arithmetic Operators:")
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

# Assignment Operators
x = 5
x += 3
x -= 2
x *= 4
x /= 6
print("\nAssignment Operators:")
print("x:", x)

# Comparison Operators
print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Logical Operators
x = True
y = False
result_and = x and y
result_or = x or y
result_not_x = not x
result_not_y = not y
print("\nLogical Operators:")
print("x and y:", result_and)
print("x or y:", result_or)
print("not x:", result_not_x)
print("not y:", result_not_y)

# Membership Operators
list_example = [1, 2, 3, 4, 5]
result_in = 3 in list_example
result_not_in = 6 not in list_example
print("\nMembership Operators:")
print("3 in list_example:", result_in)
print("6 not in list_example:", result_not_in)

# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
result_is = x is y
result_is_not = x is not y
print("\nIdentity Operators:")
print("x is y:", result_is)
print("x is not y:", result_is_not)
