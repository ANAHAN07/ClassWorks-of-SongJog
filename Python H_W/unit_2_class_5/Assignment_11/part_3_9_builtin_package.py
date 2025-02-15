import os

files = os.listdir(".")
with open("file_list.txt", "w") as file:
    for f in files:
        file.write(f + "\n")
