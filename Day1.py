# Read the contents of "Day1pt1.txt" and split them into two lists.
file_path = "Day1pt1.txt"

# Read the file and process the data
list1 = []
list2 = []


with open(file_path, 'r') as file:
    for line in file:
        # Split each line into two parts and convert to integers
        numbers = line.split()
        if len(numbers) == 2:
            list1.append(int(numbers[0]))
            list2.append(int(numbers[1]))

# Sort the lists
list1.sort()
list2.sort()

#Part 1
#take element wise difference of the two lists
diff = [abs(x-y) for x,y in zip(list1,list2)]
answer = sum(diff)
print(answer)

#Part 2
#Compute similiarity score
similarity = [x*list2.count(x) for x in list1]
similarity_score = sum(similarity)
print(similarity_score)