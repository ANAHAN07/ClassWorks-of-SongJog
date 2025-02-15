import tkinter as tk

def display_name():
    name = entry.get()
    user_input.config(text=f"Hello, {name} nice to meet you!")      # Output: Hello, Ahan nice to meet you!

root = tk.Tk()
root.title("Greeting")      # title
root.geometry("240x144")        # Screen size
root.resizable(False, False)    # You can't resize the UI.

name_input = tk.Label(root, text ="Enter your name:")       # Output: Enter your name: Ahan
name_input.pack()

entry = tk.Entry(root)              # Taking the entry  (a blank box to entry the user name)
entry.pack()

button = tk.Button(root, text="Submit", command=display_name)       # Output: Submit 
button.pack()

user_input = tk.Label(root, text="")        # This will print the user inputed data.
user_input.pack()

root.mainloop()
