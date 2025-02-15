import tkinter as tk

root = tk.Tk()
root.title("File Manager")      # Title
root.geometry("720x720")        # Screen size
root.resizable(False, False)    # You can't resize the UI.

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="New")      # New 
file_menu.add_command(label="Open")     # Old
menu.add_cascade(label="File", menu=file_menu)  # File

edit_menu = tk.Menu(menu, tearoff=0)
edit_menu.add_command(label="Cut")      # Cut
edit_menu.add_command(label="Copy")     # Copy
menu.add_cascade(label="Edit", menu=edit_menu)      # Edit

root.mainloop()
