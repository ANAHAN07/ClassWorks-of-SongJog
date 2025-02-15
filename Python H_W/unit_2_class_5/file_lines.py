file = open("unit_2_class_10\info.txt", "r")

content = file.readlines()
lines = ""

for line in content:
    lines += line.strip() + " "

print(lines)  # Output: HALA MADRID.15 times champion of UCL.the greatest club of all time.REAL MADRID's greatest rivalry is with BARCELONA...Real Madrid leads in head-to-head results in official competitive matcheswith 105 wins to Barcelona's 102 with 52 draws as of the match played on 12 January 2025.Along with Athletic Bilbao, they are the only clubs in La Liga to have never been relegated.

file.close()