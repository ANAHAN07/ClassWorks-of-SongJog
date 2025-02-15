file = open("unit_2_class_10\info_write.txt", "w")

with open("unit_2_class_10\info_write.txt", "w"):
    file.write("REAL MADRID FC.\n")

    file.close


with open("unit_2_class_10\info_write.txt", "a")as file:
    file.write("HALA MADRID.\t\n")
    file.close