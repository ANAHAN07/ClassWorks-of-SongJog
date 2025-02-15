import tkinter as tk

root = tk.Tk()
root.title("PanedWindow")       # Title
root.geometry("360x300")        # Screen size
root.resizable(False, False)    # You can't resize the UI.

pane = tk.PanedWindow(root, orient=tk.HORIZONTAL)
pane.pack(fill=tk.BOTH, expand=True)

left = tk.Label(pane, text="Left Pane", bg="lightblue")
pane.add(left)

right = tk.Entry(pane)
pane.add(right)

root.mainloop()
