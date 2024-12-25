import re
import copy


    
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


original_grid = copy.deepcopy(grid)
print_grid(grid)



height = len(grid)
width = len(grid[0])
direction  =  (-1, 0)
count = 0
loop_count = 0
places_visited = {}
xvs = {}
current_position = starting_position
direction_dict = {(-1,0):"^", (0,1):">", (1,0):"v", (0,-1):"<"}
turn_right = {(-1,0):(0,1), (0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0)}

while True:
    if current_position[0] + direction[0] < 0 or current_position[0] + direction[0] >= height or current_position[1] + direction[1] < 0 or current_position[1] + direction[1] >= width:
        grid[current_position[0]][current_position[1]] = direction_dict[direction]
        if current_position not in places_visited:
            count += 1
            places_visited[current_position] = 1
        print_grid(grid)
        break
    next_y = current_position[0] + direction[0]
    next_x = current_position[1] + direction[1]
    if grid[next_y][next_x] == "#":
        direction = turn_right[direction]
        grid[current_position[0]][current_position[1]] = direction_dict[direction]
    else:
        if grid[current_position[0]][current_position[1]] != "+":
            grid[current_position[0]][current_position[1]] = direction_dict[direction]
        if current_position not in places_visited:
            count += 1
            places_visited[current_position] = 1
        else:
            places_visited[current_position] += 1
            grid[current_position[0]][current_position[1]] = "+"
            
        #Test if obstacle would cause a loop
        obstacle_direction = turn_right[direction]
        obstacle_position = (next_y, next_x)
        fake_position = copy.deepcopy(current_position)
        xvs_obstacle = copy.deepcopy(xvs)
        while True:
            
            if fake_position[0] < 0 or fake_position[0] >= height or fake_position[1] < 0 or fake_position[1] >= width:
                break
            if grid[fake_position[0]][fake_position[1]] == "#":
                obstacle_direction = turn_right[obstacle_direction]
            xv = (fake_position[0], fake_position[1], obstacle_direction[0], obstacle_direction[1])
            if xv in xvs_obstacle:
                loop_count += 1
                grid[obstacle_position[0]][obstacle_position[1]] = "O"
                #print_grid(grid)
                break
            else:
                xvs_obstacle[xv] = 1
            fake_position = (fake_position[0] + obstacle_direction[0], fake_position[1] + obstacle_direction[1])
        if tuple(current_position+direction) in xvs:
            print(tuple(current_position+direction))
            x=1
        else:
            xvs[tuple(current_position+direction)] = 1
        current_position = (next_y, next_x)
        grid[current_position[0]][current_position[1]] = direction_dict[direction]
    #print_grid(grid)
pt1_grid = copy.deepcopy(grid)
print(count)
print(loop_count)
        




            



    
    
        
        

        