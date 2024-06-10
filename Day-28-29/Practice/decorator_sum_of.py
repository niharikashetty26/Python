def operation(func):
    print("Addition")
    def execute_the_function(a,b):
        func(a,b)
    return execute_the_function
@operation
def sum(a,b):
    print(a+b)

ans=sum(9,10)