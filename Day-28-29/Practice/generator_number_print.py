def simple_generator():
    for i in range(1, 6):
        yield i


gen = simple_generator()
for value in gen:
    print(value)
