file_path = "Day2pt1.txt"

lines = []  

with open(file_path, 'r') as file:
    for line in file:
        
        numbers = [int(x) for x in line.split()]
        lines.append(numbers)
count = 0

def report_is_safe(report):
    safe = True
    level_diffs = [report[i+1]-report[i] for i in range(len(report)-1)]
    if level_diffs[0]<0:
        level_diffs = [-x for x in level_diffs]
    for diff in level_diffs:
        if diff>3 or diff<1:
            safe = False
            break
    return safe

# Part 1
# find number of valid reports. Valid reports are either monotonically increasing or monotonically decreasing by steps between 1 and 3
safe_reports = []
for report in lines:
    if report_is_safe(report):
        count+=1
        safe_reports.append(report)
    
print(count)
                
# Part 2
# find number of valid reports. Valid reports are either monotonically increasing or monotonically decreasing by steps between 1 and 3 with at most one step removed
count = 0
for report in lines:

    if report in safe_reports:
        count+=1
        continue
    else:
        for i in range(len(report)):
            new_report = report[:i]+report[i+1:]
            if report_is_safe(new_report):
                count+=1
                break

print(count)