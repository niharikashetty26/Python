class Bank:
    def __init__(self,balance=0):
        self.balance=balance;
    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
            print(self.balance)
        else:
            print("Invalid money amount to be deposited")

    def withdraw(self,amount):
        if amount>0 and amount<self.balance:
            self.balance-=amount
            print(self.balance)

        else:
            print("Invalid money amount to be withdrawed")

    def get_balance(self):
        return self.balance

p1=Bank()
p1.get_balance()
p1.deposite(5000)
p1.withdraw(200)
p1.get_balance()
p1.deposite(-1)
p1.withdraw(10000)
