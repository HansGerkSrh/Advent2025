"""
Task description: https://adventofcode.com/2025/day/3

Implemented much cleaner solution, can now take arbitrary numbers 

"""

import math 
import re

with open(r'day03/Input.txt', 'r') as text_file:
    rows = text_file.read().splitlines()
    input = []
    for row in rows:
        input.append([int(char) for char in row])

    text_file.close()


numbers = 12 #Set this to 2 to get solution for Part 1 
voltages = []
bank: list
for bank in input: 
    index = 0
    joltages = []
    for i in range (numbers):
        sliced = bank[index:-(numbers-(i+1))] if numbers-(i+1) != 0 else bank[index:]
        val = max(sliced)
        index += sliced.index(val)
        index += 1
        joltages.append(val)
       
    voltages.append("".join(str(i) for i in joltages))
    sum = 0
for voltage in voltages:
    sum += int(voltage)

print(voltages)
print(sum)
