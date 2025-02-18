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

#build graph from rules
graph = {}
for rule in rules:
    if rule[0] not in graph:
        graph[rule[0]] = []
    graph[rule[0]].append(rule[1])

# build in-degrees
in_degrees ={}
for X,Y in rules:
    if X not in in_degrees:
        in_degrees[X]=0
    if Y not in in_degrees:
        in_degrees[Y] = 0
    in_degrees[Y]+=1

# implement Kahn's algorithm
queue = []
for node in in_degrees:
    if in_degrees[node]==0:
        queue.append(node)

sorted_order = []

while queue:
    node = queue.pop(0)
    sorted_order.append(node)

    if node in graph:
        for child in graph[node]:
            in_degrees[child]-=1
            if in_degrees[child]==0:
                queue.append(child)

if len(sorted_order) == len(in_degrees):
    print(sorted_order)

#create function to determine validity

def is_valid_update(update,graph):
    index_map = {page:i for i,page in enumerate(update)}

    for X in update:
        if X in graph:
            for Y in graph[X]:
                if Y in update:
                    if index_map[X] > index_map[Y]:
                        return False
    return True

# function to sort invalid updates using Kahn's algorithm
def sort_update(update,graph):
    sorted_order = []
    sub_graph = {}
    sub_degree = {}
    
    for X in update:        
        sub_graph[X] = []
        sub_degree[X] =0

    for X in update:
        if X in graph:
            for Y in graph[X]:
                if Y in update:
                    sub_graph[X].append(Y)
                    sub_degree[Y] += 1
    queue = [node for node in update if sub_degree[node]==0]

    while queue:
        node = queue.pop(0)
        sorted_order.append(node)
        if node in sub_graph:
            for child in sub_graph[node]:
                sub_degree[child] -= 1
                if sub_degree[child]==0:
                    queue.append(child)
    return sorted_order

middle_sum_good_updates = 0
middle_sum_bad_updates = 0

for update in updates:
    if is_valid_update(update,graph):
        middle_sum_good_updates += update[len(update)//2]
    else:
        new_update = sort_update(update,graph)
        middle_sum_bad_updates += new_update[len(new_update)//2]

print(f"Good Updates : {middle_sum_good_updates}, Bad Updates :{middle_sum_bad_updates}")
