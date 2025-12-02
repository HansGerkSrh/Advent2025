import re
import math
# Open the file in read mode

with open(r'day01\day01_text.txt', 'r') as text_file:
    line_list = text_file.read().splitlines() #einlesen des Files, dann aufteilen an jedem Zeilenumbruch
    text_file.close()

sorted_list = []
for lines in line_list:
    match = re.match(r"([A-Za-z])(\d+)", lines)
    if match:
        letter, number = match.groups()
        sorted_list.append([letter,number])

resultsum = 0
dial = 50

for entry in sorted_list:
    change = int(entry[1]) % 100
    rotations = math.floor(int(entry[1]) / 100)
    startdial = dial
    if entry[0] == "R":
        dial += change
    elif entry[0] == "L":
        dial -= change

    if dial == 0:
        resultsum += 1

    if dial < 0:
        dial += 100
        if startdial != 0:
            resultsum += 1

    if dial > 99:
        dial -= 100
        if startdial != 0:
            resultsum += 1


    resultsum += rotations
 




print("Resultsum:", resultsum)