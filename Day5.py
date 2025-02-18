import re

file_path = "Day5pt1.txt"
lines = []  
rules = []
updates = []
with open(file_path, 'r') as file:
    for line in file:
        if "|" in line.strip():
            rule = line.strip().split("|")
            rules.append([int(x) for x in rule])
        elif "," in line:
            update = line.strip().split(",")
            updates.append([int(x) for x in update])
        else:
            continue


middle_sum = 0
for update in updates:
    valid = True
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                valid = False
        if valid == False:
            break
    if valid == True:
        middle_sum += update[len(update)//2]
print(middle_sum)
