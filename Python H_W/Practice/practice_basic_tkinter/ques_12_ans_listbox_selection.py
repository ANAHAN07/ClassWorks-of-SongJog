import tkinter as tk

def show_selection():
    selection = listbox.get(listbox.curselection())
    label.config(text=f"Selected: {selection}")

root = tk.Tk()
root.title("Listbox")       # Title
root.geometry("300x250")        # Screen size
root.resizable(False, False)    # You can't resize the UI.

listbox = tk.Listbox(root)
for item in ["BMW", "Toyota", "Tesla", "AMG", "Audi", "Kia", "Nissan", "Porcha", "Pagani", "VolsVogen", "Konegseeg"]:       # List
    listbox.insert(tk.END, item)

listbox.pack()

button = tk.Button(root, text="Select", command=show_selection)         # Select
button.pack()

label = tk.Label(root, text="Selected: ")               # Selected: BMW
label.pack()

root.mainloop()
