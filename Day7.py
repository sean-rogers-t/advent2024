file_name = "Day7.txt"
answers = []
components = []
with open(file_name,"r") as file:
    for line in file:
        answers.append(int(line.split(":")[0].strip()))
        components.append(list(map(int, line.split(":")[1].strip().split(" "))))

def to_ternary(num, length):
    # Generate ternary representation
    ternary = ""
    while num > 0:
        ternary = str(num % 3) + ternary
        num //= 3
    # Pad with leading zeros to ensure the desired length
    return ternary.zfill(length)

test_sum =0

for i in range(len(answers)):
    n = len(components[i])
    for j in range(2**(n-1)):
        temp = components[i][0]
        j_bin = bin(j)[2:].zfill(n-1)
        for k in range(n-1):
            if j_bin[k] == "0":
                temp += components[i][k+1]
            else:
                temp *= components[i][k+1]
            if temp>answers[i]:
                break
        if temp == answers[i]:
            test_sum += answers[i]
            break
print(test_sum)        

test_sum =0

for i in range(len(answers)):
    n = len(components[i])
    for j in range(3**(n-1)):
        j_tern = to_ternary(j, n-1)
        temp = components[i][0]
        j_bin = bin(j)[2:].zfill(n-1)
        for k in range(n-1):
            if j_tern[k] == "0":
                temp += components[i][k+1]
            elif j_tern[k] == "1":
                temp *= components[i][k+1]
            else:
                temp = int(str(temp) + str(components[i][k+1]))
            if temp>answers[i]:
                break
        if temp == answers[i]:
            test_sum += answers[i]
            break
print(test_sum) 


