"""
Task description: https://adventofcode.com/2025/day/7

"""

import math 
import re

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, r'Input.txt')

with open(filename, 'r') as text_file:
    rows = text_file.read().splitlines()
    text_file.close()


for row in rows:
    print(row)

i = 0
while i < len(rows[0]):
    if rows[0][i] != 'S':
        i += 1
    else:
        startingPos = i
        break

pos = (0,startingPos)

beams = 0
hitspliter = set()

from functools import lru_cache

@lru_cache(maxsize=None)
def calcBeams(positon):
    y, x = positon
    while rows [y][x] != '^':
        y += 1
        if y == len(rows):
            return 1

    if (y,x) not in hitspliter:
        hitspliter.add((y,x))


    return calcBeams((y,x + 1)) + calcBeams((y,x-1))


x = calcBeams(pos)


print("Part 1: " + str(len(hitspliter)))
print("Part 2: " + str(x))