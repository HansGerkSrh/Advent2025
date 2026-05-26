"""
Task description: https://adventofcode.com/2025/day/5

"""

import math 
import re

with open(r'day05/Input.txt', 'r') as text_file:
    rows = text_file.read().splitlines()
    text_file.close()

i = 0 
ranges = []
ingredients = []
while rows[i] != "":
    ranges.append(rows[i].split("-"))
    i += 1
i += 1 
while i < len(rows):
    ingredients.append(int(rows[i]))
    i += 1


counter = 0
for ingredient in ingredients:
    for row in ranges:
        if ingredient >= int(row[0]) and ingredient <= int(row[1]):
            counter += 1
            break

print(ranges)
print(ingredients)
print(counter)