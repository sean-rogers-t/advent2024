import copy
import math
file_path = "Day8.txt"
lines = []
with open(file_path,"r") as file:
    for line in file:
        lines.append(list(line.strip()))

grid  ={i+k*1j: lines[k][i] for k in range(len(lines)) for i in range(len(lines[0]))}

antennae = {}
for key,item in grid.items():
    if item != ".":
        if item not in antennae:
            antennae[item] = {key}
        else:
            antennae[item].add(key)

#pt1
antipodes = set()
for key,item in antennae.items():
    pairs = {frozenset((a,b)) for a in item for b in item if a!=b}
    for a,b in pairs:
        distance = a-b
        gcd =math.gcd(int(distance.real),int(distance.imag))
        distance_reduced = distance.real/gcd + distance.imag/gcd*1j
        current_spot = a
        while grid.get(current_spot):
            antipodes.add(current_spot)
            current_spot += distance_reduced
        current_spot = a
        while grid.get(current_spot):
            antipodes.add(current_spot)
            current_spot -= distance_reduced
        
       
print(len(antipodes))

#pt2
