class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = amount

acc = BankAccount(1269000, 2000000)
print(acc.get_balance())        # Output: 2000000
acc.set_balance(10000)
print(acc.get_balance())        # Output: 10000

# acc.set_balance(-800)              # Output:        Traceback (most recent call last):
                                                     # File "d:\Ahnaf Doc\Python H_W\unit_3_class_3\Assignment_15\task_2_getter_setter.py", line 19, in <module>
                                                            # acc.set_balance(-800)  
                                                            # ^^^^^^^^^^^^^^^^^^^^^
                                                            # File "d:\Ahnaf Doc\Python H_W\unit_3_class_3\Assignment_15\task_2_getter_setter.py", line 11, in set_balance
                                                                   # raise ValueError("Balance cannot be negative!")
                                                                    #ValueError: Balance cannot be negative!
