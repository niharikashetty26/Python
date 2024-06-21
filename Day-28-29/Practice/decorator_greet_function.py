def greet(func):
    def wrapper_hello(name):
        name="abcd"
        func(name)
    return wrapper_hello

@greet
def hello(name):
    print("Hello ",name)

hello("Niharika")