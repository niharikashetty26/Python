class Negative_numbers(Exception):
    def __init__(self,number,message="Negative number found"):
        self.number=number
        self.message=message
        super().__init__(self.message)
    def __str__(self):
        return f"{self.number} -> {self.message}"

def check_list(L):
    try:
        for i in L:
            if i < 0:
                raise Negative_numbers(i)
            print(f"{i} is valid.")
    except Negative_numbers as e:
        print(e)

check_list([2,1,9,-9])