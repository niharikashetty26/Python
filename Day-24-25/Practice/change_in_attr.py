class Car:
    def __init__(self):
        self.clutch=False
        self.acc=False

    def start(self):
        self.clutch=True
        self.acc=True
        print('Car has been started')

s1=Car()
s1.start()