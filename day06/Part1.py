"""
Task description: https://adventofcode.com/2025/day/6

"""

import math 
import re

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, r'Input.txt')

with open(filename, 'r') as text_file:
    rows = text_file.read().splitlines()
    text_file.close()


i = 0
liste =[0]*len(rows)
for row in rows:
    liste[i] = row.split()
    #print(liste[i])
    i += 1
i = 0

print(liste[:-1])

i = 0
for  row in liste[:-1]:
    liste[i] = list(map(int, row))
    i += 1


import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

sum = 0
i = 0
while i < len(liste[0]):
    rowsum = 0
    op = ops[liste[-1][i]]
    j = 0
    while j < len(liste)-2 :
        rowsum = op(liste[j][i],liste[j+1][i])
        liste[j+1][i] = rowsum
        j += 1
    sum += rowsum
    i += 1

print(sum)