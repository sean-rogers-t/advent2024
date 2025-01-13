file_path = "Day9.txt"

lines = []

with open(file_path,"r") as file:
    for line in file:
        disk_map =line.strip()

disk_list = []
files_list  = []
is_space = 0
file_number = 0
open_space = 0
index = 0
disk_schema = []
files = {}
space = {}
disk_size = 0
for i in range(len(disk_map)):
    number = int(disk_map[i])
    disk_size+=number
    if i%2==0:
        disk_list += [str(file_number)]*number
        files_list+=[str(file_number)]*number
        disk_schema.append([file_number,number])
        files[file_number] = [index,number]
        file_number+=1
        
    else:
        disk_list+=["."]*number
        disk_schema.append([-1,number])
        open_space+=number if i!= (len(disk_map)-1) else open_space
        if number>0:
            space[index]=number
    index+=number
print("".join(disk_list))
#pt1
count=0
for i in range(len(files_list)):
    if disk_list[i] == ".":
        disk_list[i] = files_list[-1-count]
        count+=1
        
disk_list[len(files_list):] = "."*open_space
refragmented_disk = "".join(disk_list)
print(refragmented_disk)
check_sum = 0
for i in range(len(files_list)):
    check_sum += i*int(disk_list[i])

print(check_sum)
        
#pt2
x=1
#going from largest file ID to smallest
#adjust space and files
# fixed_blocks = ["."]*disk_size
# for key,value in files.items():
#     fixed_blocks[value[0]:value[0]+value[1]] = [str(key)]*value[1]
# print("".join(fixed_blocks))
for i in range(len(disk_map)//2,0,-1):

    space_needed = files[i][1]
    start_index = files[i][0]
    min_index = min((key for key,value in space.items() if value>=space_needed),default=None)
    if min_index is not None:
        if min_index < start_index:
            size = space.pop(min_index)
            space[files[i][0]]=space_needed
            if size>space_needed:
                space[min_index+space_needed] = size-space_needed
            files[i][0] = min_index
    # fixed_blocks = ["."]*disk_size
    # for key,value in files.items():
    #     fixed_blocks[value[0]:value[0]+value[1]] = [str(key)]*value[1]
    # print("".join(fixed_blocks))
x=1
check_sum2 = 0
for key,value in files.items():
    index = value[0]
    block_size = value[1]
    for i in range(block_size):
        check_sum2+=key*(index+i)
print(check_sum2)

        

    





