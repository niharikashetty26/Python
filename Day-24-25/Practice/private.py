class Login:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
    def check_reset(self):
        print(self.__password)

s1=Login("Niharika","1234")
print(s1.username)
print(s1.check_reset())
print(s1.__password)