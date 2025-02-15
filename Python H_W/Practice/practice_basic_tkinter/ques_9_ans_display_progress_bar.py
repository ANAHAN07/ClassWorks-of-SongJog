import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    for i in range(101):
        progress["value"] = i
        root.update_idletasks()
        time.sleep(0.05)

root = tk.Tk()
root.title("Downloading Virus")     # Title

progress = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")     # loading process
progress.pack()

button = tk.Button(root, text="Start", command=start_progress) # clicking on start the process will start.
button.pack()

root.mainloop()
