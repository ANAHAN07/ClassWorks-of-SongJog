# data_base = {}

# while True:
#     user_name = input("Enter Your name (Enter 'quit' to exit): ")
#     if user_name == "quit":
#         break
#     else:
#         age = int(input("Enter your age: "))
#         sch = input("Enter your school name: ")
        
#         lst = [age, sch]

#         data_base[user_name] = lst

#         print(f"Your registered data base are mentioned below")

# print(data_base)





data_base = {}

while True:
    user_name = input("Enter Your name (Enter 'quit' to exit): ")
    if user_name == "quit":
        break
    else:
       
        age = int(input("Enter your age: "))
        sch = input("Enter your school name: ")

        lst = [age, sch]

        data_base[user_name] = lst

        print(f"Your registered data base are mentioned below")

print(data_base)