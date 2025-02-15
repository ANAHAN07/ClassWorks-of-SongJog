import tkinter as tk

def show_text():
    text_content = txt_show.get("1.0", tk.END)
    print(text_content)

root = tk.Tk()
root.title("MULTI-LINER")       # Title
root.geometry("360x300")        # Screen size
root.resizable(False, False)    # You can't resize the UI.

txt_show = tk.Text(root, height=5, width=30)        # This is just a blank box. For inputing the text.
txt_show.pack()

button = tk.Button(root, text="Show the Text", command=show_text)       # This will show the text in the terminal.
button.pack()

root.mainloop()
