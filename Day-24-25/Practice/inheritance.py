class Car:
    @staticmethod
    def start():
        print("Start")
    @staticmethod
    def stop():
        print("Stop")

class Tata(Car):
    def __init__(self,name):
        self.name=name

s1=Tata("ABC")
print(s1.name)
print(s1.start())
