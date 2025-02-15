class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        try:
            if amount < 0:
                raise ValueError("Balance can't be negative!")
            self.__balance = amount
        except ValueError as e:
            print("Error:", e)

acc = BankAccount(18906800, 108800)
acc.set_balance(-5000)  # Output: Error: Balance can't be negative!