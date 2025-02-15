user_input = "Enter a pizza topping (or 'quit' to stop): "
while True:
    topping = input(user_input)
    if topping.lower() == 'quit':
        print("Exiting the pizza topping selection!")
        break
    print(f"I'll add {topping} to your pizza!")
