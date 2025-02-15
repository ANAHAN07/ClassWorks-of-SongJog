import tkinter as tk

def show_selection():
    option.config(text=f"Selected: {language.get()}")

root = tk.Tk()
root.title("Choice your option")    # Title
root.geometry("300x200")        # Screen size
root.resizable(False, False)    # You can't resize the UI.

language = tk.StringVar(value="None")       # This will show the selection option

tk.Radiobutton(root, text="Python", variable=language, value="Python").pack()   # Output: (selection option) Python
tk.Radiobutton(root, text="Java", variable=language, value="Java").pack()       # Output: (selection option) JAVA
tk.Radiobutton(root, text="C++", variable=language, value="C++").pack()         # Output: (selection option) C++
tk.Radiobutton(root, text="HTML", variable=language, value="HTML").pack()       # Output: (selection option) HTML

button = tk.Button(root, text="Submit", command=show_selection)     # Submit
button.pack()

option = tk.Label(root, text="Selected: None")      # Selected value will show None 
option.pack()

root.mainloop()