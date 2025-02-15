class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f"{self.message}"
    
class BankAccount:
    def __init__(self, name, ac_no, balance = 500):
        self.name = name
        self.ac_no = ac_no
        self.__balance = balance

    def show_balance(self):
        print(f"Balance: {self.__balance}")

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount}BDT was deposited to your account!")

    def withdraw(self, amount):
        
        if (self.__balance - amount) < 500:
            raise CustomError("You cannot withdraw this amount, You don't have enough Money!")
        else:
            self.__balance -= amount
            print(f"{amount} BDT was withdrawed from your account")



ac_1 = BankAccount("Ahan", 23470, 10000)
# print(ac_1.balance)
print(ac_1.name)
print(ac_1.ac_no)
# print(ac_1.__balance)
ac_1.show_balance()
# ac_1.balance = 50000
# print(ac_1.balance)
ac_1.deposit(5000)
ac_1.show_balance()
ac_1.withdraw(14000)
ac_1.show_balance()
# ac_1.withdraw(600)
ac_1.show_balance()