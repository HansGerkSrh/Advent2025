"""
Task description: https://adventofcode.com/2025/day/4

"""

import math 
import re

with open(r'day04/Input.txt', 'r') as text_file:
    rows = text_file.read().splitlines()
    input = []
    for row in rows:
        input.append([char for char in row])

    text_file.close()

directions = [[-1,-1],[-1,0],[-1,1],
              [0,-1],        [0,1],
              [1,-1], [1,0], [1,1]]
possibles = 0

y = 0
while y < len(input):
    x = 0 
    while x < len(input[y]):
        if input[y][x] == '@':
            count = 0
            for dy, dx in directions: 
                r, c = y + dy, x + dx
                if r >= 0 and c >= 0 and r <len(input) and c <len(input[r]):
                    if input[r][c] == '@':
                        count += 1 
            if count < 4: 
                possibles += 1
        x += 1
    y += 1

print(possibles)