"""
Task description: https://adventofcode.com/2025/day/3

"""

import math 
import re

with open(r'day03/Input.txt', 'r') as text_file:
    rows = text_file.read().splitlines()
    input = []
    for row in rows:
        input.append([int(char) for char in row])

    text_file.close()

joltages = []
voltages = []
bank: list
for bank in input: 
    FirstBat = 0 
    index = 0
    for i in bank[:-1]:
        if i == max(bank):
            FirstBat = max(bank)
            break
        else:
            FirstBat = max(bank[:-1])
        index += 1  
    
    bank.remove(FirstBat) 
    if index == len(bank):
        index = index-1
    SecondBat = max(bank[index:])
    
    voltages.append(str(FirstBat) + str(SecondBat))
sum = 0
for voltage in voltages:
    sum += int(voltage)

print(voltages)
print(sum)
