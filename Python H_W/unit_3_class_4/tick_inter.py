import tkinter as tk

root = tk.Tk()
root.title("Welcome to PERSONAL OS")
root.geometry("720x400")

def catch_me():
    print("Don't touch me")

button = tk.Button(root, text="Touch ME is u can!!", command=catch_me)
button.pack()

label = tk.Label(root, text="Follow me on instagram @its.me.memebd")
label.pack()


root.mainloop()