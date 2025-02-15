import tkinter as tk

root = tk.Tk()
root.title("Spinbox")   # Title
root.geometry("200x200")        # Screen size
root.resizable(False, False)    # You can't resize the UI.

spinbox = tk.Spinbox(root, from_=1, to=10)      # Spinning
spinbox.pack()

root.mainloop()
