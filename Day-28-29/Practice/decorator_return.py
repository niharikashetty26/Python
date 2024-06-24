def add_operation(x):
    def add_operation2(y):
        return x+y

    return add_operation2

answer=add_operation(5)
print(answer(10))


