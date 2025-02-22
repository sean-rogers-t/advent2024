file_path = "Day10.txt"
grid = []


with open(file_path, 'r') as file:
    for line in file:
        grid.append(list(line.strip()))

complex_grid = {(i+k*1j):int(grid[k][i]) for k in range(len(grid)) for i in range(len(grid[0]))}

trailheads = [node for node in complex_grid if complex_grid[node]==0]
trailhead_scores = {trailhead:0 for trailhead in trailheads}
trailhead_ratings = {trailhead:0 for trailhead in trailheads}
complex_directions = [1, -1, 1j, -1j]
for trailhead in trailheads:
    queue = [trailhead]
    visited = set()
    terminus = set()
    while queue:
        node = queue.pop(0)
        if node in terminus:
            continue
        visited.add(node)
        level = complex_grid[node]
        for direction in complex_directions:
            next_node = node + direction
            if next_node in complex_grid:
                if complex_grid[next_node] == level+1 and next_node not in visited and next_node not in queue:
                    queue.append(next_node)
                    if complex_grid[next_node] == 9 and next_node not in terminus:
                        terminus.add(next_node)
                        trailhead_scores[trailhead] += 1

for trailhead in trailheads:
    queue = [trailhead]
    visited = set()
    
    while queue:
        node = queue.pop(0)
        if complex_grid[node] == 9:
            continue
        visited.add(node)
        level = complex_grid[node]
        for direction in complex_directions:
            next_node = node + direction
            if next_node in complex_grid:
                if complex_grid[next_node] == level+1:
                    queue.append(next_node)
                    if complex_grid[next_node] == 9:
                        trailhead_ratings[trailhead] += 1
        
print(sum(trailhead_scores.values()))
print(sum(trailhead_ratings.values()))
""" print(trailhead_scores)
print(trailhead_ratings) """
