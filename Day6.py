import re

def turn_right(direction):
    if direction == (-1, 0):
        return (0, 1)
    if direction == (0, 1):
        return (1, 0)
    if direction == (1, 0):
        return (0, -1)
    if direction == (0, -1):
        return (-1, 0)
    
def print_grid(grid):
    for row in grid:
        print("".join(row))
    print("\n")

file_path = "Day6pt1.txt"
grid = []  
lines = []
starting_position = (-1,-1)

with open(file_path, 'r') as file:
    for line in file:
        grid.append(list(line.strip()))

for i in range(len(grid)):
    if "^" in grid[i]:
        starting_position = (i, grid[i].index("^"))
        break

height = len(grid)
width = len(grid[0])
direction  =  (-1, 0)
count = 0
places_visited = {}
current_position = starting_position
direction_dict = {(-1,0):"^", (0,1):">", (1,0):"v", (0,-1):"<"}

print_grid(grid) 
while True:
    if current_position[0] + direction[0] < 0 or current_position[0] + direction[0] >= height or current_position[1] + direction[1] < 0 or current_position[1] + direction[1] >= width:
        grid[current_position[0]][current_position[1]] = "X"
        if current_position not in places_visited:
            count += 1
            places_visited[current_position] = 1
        print_grid(grid)
        break
    next_y = current_position[0] + direction[0]
    next_x = current_position[1] + direction[1]
    if grid[next_y][next_x] == "#":
        direction = turn_right(direction)
        grid[current_position[0]][current_position[1]] = direction_dict[direction]
    else:
        grid[current_position[0]][current_position[1]] = "X"
        if current_position not in places_visited:
            count += 1
            places_visited[current_position] = 1
        current_position = (next_y, next_x)
        grid[current_position[0]][current_position[1]] = direction_dict[direction]
    #print_grid(grid)
    

          

print(count)
        

        

    
    
        
        

        