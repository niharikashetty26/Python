class Greet:
    __name="anonymous"
    def __hello(self):
        print("hello")
    def welcome(self):
        self.__hello()
s1=Greet()
s1.welcome()