import re

file_path = "Day3pt1.txt"
lines = []  

with open(file_path, 'r') as file:
    for line in file:
        
        
        lines.append(line)
full_instructions = "".join(lines)
# Part 1
sum = 0
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, full_instructions)
match_starts = [match.start() for match in re.finditer(pattern, full_instructions)]
for match in matches:
    sum += int(match[0])*int(match[1])
print(sum)

# Part 2

do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
# Find all matches for "do()" and "don't()"
do_matches = list(re.finditer(do_pattern, full_instructions))
dont_matches = list(re.finditer(dont_pattern, full_instructions))
dos = [match.start() for match in do_matches]
donts = [match.start() for match in dont_matches]

dont_start = re.search(dont_pattern, full_instructions).start()
do_start=0
counter = 0
refined_sum = 0
while counter<len(full_instructions):
    matches = re.findall(pattern, full_instructions[do_start:dont_start+1])
    for match in matches:
        refined_sum+= int(match[0])*int(match[1])
    if re.search(do_pattern, full_instructions[dont_start:]):
        do_start = re.search(do_pattern, full_instructions[dont_start:]).start()+dont_start
    else:
        break
    if re.search(dont_pattern, full_instructions[do_start:]):
        dont_start = re.search(dont_pattern, full_instructions[do_start:]).start()+do_start
    else:
        break
    counter = dont_start
print(refined_sum)






