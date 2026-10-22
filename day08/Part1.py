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

