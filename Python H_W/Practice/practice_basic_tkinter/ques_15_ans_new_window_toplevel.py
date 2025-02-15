import tkinter as tk

def open_window():
    new_win = tk.Toplevel(root)
    new_win.title("New Window") # title
    new_win.geometry("250x100") # Screen size 
    label = tk.Label(new_win, text="New Window(unable to use)")     # New Window(unable to use)
    label.pack()

root = tk.Tk()
root.title("Opend Window")    # Title
root.geometry("250x150")        # Screen size
root.resizable(False, False)    # You can't resize the UI.

button = tk.Button(root, text="Open Window", command=open_window)   #   Open Window Button
button.pack()

root.mainloop()
