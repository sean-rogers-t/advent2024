import re

file_path = "Day4pt1.txt"
lines = []  

with open(file_path, 'r') as file:
    for line in file:
        line = "..."+line.strip()+"..."
        
        lines.append(line)
lines_buffer  = ["."*len(lines[0]) for i in range(3)]
lines = lines_buffer + lines + lines_buffer
# Part 1
# find all instances of xmas in word search
xmas_count = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "X":
            right = lines[i][j] + lines[i][j+1] + lines[i][j+2] + lines[i][j+3]
            down = lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j]
            diag1 = lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3]
            diag2 = lines[i][j] + lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3]
            left = lines[i][j] + lines[i][j-1] + lines[i][j-2] + lines[i][j-3]
            up = lines[i][j] + lines[i-1][j] + lines[i-2][j] + lines[i-3][j]
            diag3 = lines[i][j] + lines[i-1][j+1] + lines[i-2][j+2] + lines[i-3][j+3]
            diag4 = lines[i][j] + lines[i-1][j-1] + lines[i-2][j-2] + lines[i-3][j-3]
            for word in [right, down, diag1, diag2, left, up, diag3, diag4]:
                if word == "XMAS":
                    xmas_count += 1


# Part 2
x_mas_count = 0
center_As = []
print("\n".join(lines))
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "M":
            if lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] == "MAS":
                center_As.append((i+1-3, j+1-3))
            if lines[i][j] + lines[i+1][j-1] + lines[i+2][j-2] == "MAS":
                center_As.append((i+1-3, j-1-3))
            if lines[i][j] + lines[i-1][j+1] + lines[i-2][j+2] == "MAS":
                center_As.append((i-1-3, j+1-3))
            if lines[i][j] + lines[i-1][j-1] + lines[i-2][j-2] == "MAS":
                center_As.append((i-1-3, j-1-3))
            x=1
counts={}

for A in center_As:
    if A in counts:
        counts[A] += 1
    else:
        counts[A] = 1
for item in counts:
    if counts[item] == 2:
        x_mas_count += 1
print(x_mas_count)

            
            
                    