import tkinter as tk

def check_status():
    label.config(text=f"Accepted: {var.get()}")

root = tk.Tk()
root.title("Terms and Condition")    # Title
root.geometry("700x300")        # Screen size
root.resizable(False, False)    # You can't resize the UI.

var = tk.BooleanVar()

agremment_file = tk.Label(root, text="To use the Tkinter files,\nensure you have **Python 3.x** installed.\nSave the script as a `.py` file (e.g., `scale_example.py`),\nmthen open **Command Prompt (Windows)** or **Terminal (Mac/Linux)**, navigate to the file’s directory using `cd`,\nand run `python scale_example.py` (or `python3 scale_example.py` on Mac/Linux).\nThe Tkinter GUI will open, where you can interact with widgets like scales, buttons, and text inputs.\nIf Tkinter isn't installed, use `pip install tk`.\nIf you encounter errors, check for typos or missing dependencies. 🚀")       # agrement file
agremment_file.pack()

check = tk.Checkbutton(root, text="Accept Terms", variable=var)     # checkbox
check.pack()

button = tk.Button(root, text="Check", command=check_status)        # check button
button.pack()

label = tk.Label(root, text="Accepted: False")      # Accepted: False
label.pack()

root.mainloop()
