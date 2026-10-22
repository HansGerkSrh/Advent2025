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

lis = []

j = 0
while j < len(rows[0]):
    block = True
    for k in range(len(rows)-1):
        if rows[k][j] != ' ':
            block = False
    if block:
        lis.append(' ')
    else:
        lis.append(0)
    j += 1

print(lis)
print(rows[:-1])

i = 0

while i < len(rows) - 1:
    j = 0 
    while j < len(rows[0]):
        if rows[i][j] == ' ':
            j += 1
            continue
        else:
            lis[j] *= 10
            lis[j] += int(rows[i][j])
            j += 1
    i += 1


print(lis)
opslist = rows[-1].split()
print(opslist)

import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  
    '%' : operator.mod,
    '^' : operator.xor,
}

op = len(opslist) -1
i = len(lis) -1
sum = 0
while i >= 0:
    intermediate = lis[i]
    i -= 1 
    while lis[i] != ' ' and i >= 0:
        intermediate = ops[opslist[op]](intermediate,lis[i])     
        i -= 1
    i -= 1 
    op -= 1
    sum += intermediate


print(sum)
