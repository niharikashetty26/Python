class CheckAge(Exception):
    def __init__(self, age, message="Invalid age"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.age}->{self.message}'


def check_age_function(age):
    if age < 0 or age > 120:
        raise CheckAge(age)
    else:
        print(f"Age is {age}")


try:
    check_age_function(900)
except CheckAge as e:
    print(e)

