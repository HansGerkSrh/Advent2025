"""
Task description: https://adventofcode.com/2025/day/5

"""

import math 
import re

with open(r'day05/Input2.txt', 'r') as text_file:
    rows = text_file.read().splitlines()
    text_file.close()

i = 0 
ranges = []

i = 0
for row in rows:
    ranges.append(row.split("-"))
    ranges[i] = list(map(int, ranges[i]))
    i += 1
    
ranges = sorted(ranges, key=lambda x: x[0])

i = 0
while i < len(ranges)-1:
    while i+1 < len(ranges) and ranges[i][1] >= ranges[i+1][0] and ranges[i][1] > ranges[i+1][1]:
        ranges.pop(i+1)

    if i +1 < len(ranges) and ranges[i][1] >= ranges[i+1][0] and ranges[i][1] <= ranges[i+1][1]:
        ranges[i][1] = ranges[i+1][0] - 1

    i += 1 


def count():
    counter = 0
    for row in ranges:    
        counter += int(row[1]) - int(row[0]) +1 
    print(ranges)
    print(counter)


print(ranges)
count()
