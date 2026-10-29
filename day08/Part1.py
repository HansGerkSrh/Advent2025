"""
Task description: https://adventofcode.com/2025/day/8

"""

import math 
from functools import lru_cache
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, r'Input.txt')

with open(filename, 'r') as text_file:
    rows = text_file.read().splitlines()
    text_file.close()


cords = []
for row in rows:
    cord = row.split(',')
    cords.append(cord)


def getdistance(coordinates1:tuple, coordinates2:tuple):
    x1,y1,z1 = coordinates1
    x2,y2,z2 = coordinates2
    return math.sqrt((x2-x1)**2 +(y2-y1)**2 + (z2-z1)**2) 


networks = []
i = 0
for cord in cords:
    networks.append([i,tuple(map(int,cord))])
    i += 1

for network in networks:
    print(network)


connections = set()
for k in range(1000):
    i = 0
    minval = -1
    minid = ()
    while i < len(networks):
        j = i + 1
        while j < len(networks):
            if (i,j) in connections:
                j += 1
                continue
            distance = getdistance(networks[i][1],networks[j][1])
            if minval == -1:
                minval = distance
                minid = (i,j)
            elif distance < minval:
                minval = distance
                minid = (i,j)
            j += 1
        i += 1

    #print(k)
    connections.add(minid)
    #print(networks[minid[0]],networks[minid[1]])

    newcircuit = networks[minid[0]][0] 
    oldcircuit = networks[minid[1]][0]
    m = 0
    while m < len(networks):
        if networks[m][0] == oldcircuit:
            networks[m][0] = newcircuit
        m += 1

    #print(minval)
    #print(networks[minid[0]],networks[minid[1]])

    #print("     ")

networks.sort()
for line in networks:
    print(line)
# print(getdistance((1,-5,7),(3,4,-80)))
# print(getdistance((0,0,0),(3,4,0)))

counts = {}
for element in networks:
    circuit = element[0]
    counts[circuit] = counts.get(circuit, 0) + 1

#print(counts)

i = 0
product = 1
while i < 3:
    max = 0
    key = None
    for entry in counts:
        if counts.get(entry) > max:
            max = counts.get(entry)
            key = entry
    del counts[key]
    product *= max
    i += 1




print(product)