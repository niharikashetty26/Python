class NegativeNumber(Exception):
    def __init__(self, number, message="Negative number found"):
        self.number = number
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.number} -> {self.message}"


def check_list(l):
    try:
        for i in l:
            if i < 0:
                raise NegativeNumber(i)
            print(f"{i} is valid.")
    except NegativeNumber as e:
        print(e)


check_list([2, 1, 9, -9])