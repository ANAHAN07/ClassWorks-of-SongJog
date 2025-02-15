file = open("unit_2_class_10\info.txt", "r")

content = file.readlines() # Output: ['HALA MADRID\n', '\n', '15 times champion of UCL.\n', '\n', 'the greatest club of all time. \n', '\n', "REAL MADRID's greatest rivalry is with BARCELONA..."]
print(content)

file.close()