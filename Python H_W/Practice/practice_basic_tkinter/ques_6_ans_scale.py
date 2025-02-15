import tkinter as tk

def show_value(val, label):
    label.config(text=f"Value: {val}")  

root = tk.Tk()
root.title("Scale Counter")     # Title
root.geometry("360x300")        # Screen size
root.resizable(False, False)    # You can't resize the UI.

label_1 = tk.Label(root, text="Horizontal Value: 0")     # Horizontal Scale
label_1.pack()

scale_1 = tk.Scale(root, from_=0, to=100, orient="horizontal",
                  command=lambda val: show_value(val, label_1))     # Horizontal Value Shower
scale_1.pack()

label_2 = tk.Label(root, text="Vertical Value: 0")      # Vertical Scale
label_2.pack()

scale_2 = tk.Scale(root, from_=0, to=100, orient="vertical",
                  command=lambda val: show_value(val, label_2))      # Vertical Value Shower
scale_2.pack()

root.mainloop()
