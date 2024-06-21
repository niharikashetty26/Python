class Bank:
    def __init__(self,acc_no,balance):
        self.account=acc_no
        self.total_balance=balance

    def get_balance(self):
        return self.total_balance

    def debit(self,amount):
        self.total_balance-=amount
        print("Amount debited:", amount)
        print("Total balance: ",self.get_balance())

    def credit(self,amount):
        self.total_balance+=amount
        print("Total amount credited: ",amount)
        print("Total balance: ",self.get_balance())
m1=Bank(123456789, 10000)
m1.debit(1000)
m1.credit(2000)