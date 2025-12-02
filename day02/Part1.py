"""
Task description: https://adventofcode.com/2025/day/2

"""

import math 
import re

with open(r'day02/Input.txt', 'r') as text_file:
    list = text_file.read().split(",")
    input = []
    for pair in list:
        input.append(pair.split("-"))
    text_file.close()

def get_integer_lenght(number):
    lenght = math.floor(math.log(number,10)) + 1  #Log10 der Nummer - Abrunden - +1 
    return lenght 

def checknumber(number):
    lenght = get_integer_lenght(number)
    number = str(number)
    if lenght % 2 == 1: 
        return True
    i = 0
    pattern = ""

    while i < lenght/2: 
        pattern += number[i]
        i += 1
    count = len(re.findall(pattern, number))
    if count > 1: 
        return False
    else:
        return True


invalids = 0
for index in input: 
    for numbers in range(int(index[0]),int(index[1])+1):
        #print("number",numbers)
        if not checknumber(numbers):
            invalids += numbers


print(invalids)
