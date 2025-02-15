def log_message(fun):
    def wrapper(*args, **kwargs):
        print(f"Calling function {fun.__name__}")   # Output: Calling function greet
        return fun(*args, **kwargs)
    return wrapper

class Greeter:
    def __init__(self, name):
        self.name = name

    @log_message
    def greet(self):
        print(f"Hello, {self.name}!")       # Output: Hello, Obito Uchiha!

greeter = Greeter("Obito Uchiha")
greeter.greet()