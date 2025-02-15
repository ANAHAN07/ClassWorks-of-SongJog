import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("DATA")  # Title

tree = ttk.Treeview(root, columns=("ID", "Name", "Age"), show="headings")   # Headings
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
                                                        # Output:  ID  |  NAME  |  Age

tree.insert("", "end", values=(1653, "Ahnaf", 17))      # Output: 1653, "Ahnaf", 17
tree.insert("", "end", values=(2753, "Wachiu", 15))     # Output: 2753, "Wachiu", 15
tree.insert("", "end", values=(3567, "Hecky", 15))      # Output: 3567, "Hecky", 15
tree.insert("", "end", values=(4824, "Adyan", 12))      # Output: 4824, "Adyan", 12

tree.pack()

root.mainloop()