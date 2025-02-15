import tkinter as tk
from tkinter import ttk

def show_choice():
    label.config(text=f"Selected: {combobox.get()}")

root = tk.Tk()
root.title("Combobox Selection")    # Title
root.geometry("240x300")        # Screen size
root.resizable(False, False)    # You can't resize the UI.

combobox = ttk.Combobox(root, values=["Python", "Java", "C++", "HTML", "JSON", "C#", "PHP", "Ruby", "Lua"])     # List of combobox
combobox.pack()

button = tk.Button(root, text="Select", command=show_choice)    # Select
button.pack()

label = tk.Label(root, text="Selected: ")       # This will show the selected option
label.pack()

root.mainloop()