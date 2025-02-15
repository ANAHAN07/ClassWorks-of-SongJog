import tkinter as tk

def say_hello():
    print("Hello")

def say_goodbye():
    print("Goodbye")

root = tk.Tk()
root.title("Greet")
root.geometry("240x144")

label = tk.Label(root, text="Click a button:")
label.pack(pady=10)

hello_button = tk.Button(root, text="Say Hello", command=say_hello)
hello_button.pack(pady=5)

goodbye_button = tk.Button(root, text="Say Goodbye", command=say_goodbye)
goodbye_button.pack(pady=5)

root.mainloop()
