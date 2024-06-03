class InsufficientFundsError(Exception):
    pass


class NegativeAmountError(Exception):
    pass


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountError("Cannot deposit a negative amount.")
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountError("Cannot withdraw a negative amount.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for this withdrawal.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}.")

    def get_balance(self):
        return self.balance


def main():
    account = BankAccount("John Doe", 100.0)

    try:
        account.deposit(500)
        account.withdraw(300)
        account.withdraw(150)
        account.withdraw(300)

    except InsufficientFundsError as e:
        print(f"Error: {e}")

    except NegativeAmountError as e:
        print(f"Error: {e}")

    finally:
        print(f"Final balance: {account.get_balance()}")


if __name__ == "__main__":
    main()
