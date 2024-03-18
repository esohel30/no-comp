with open('day9.txt', 'r') as file: 
    hist = []
    for line in file: 
        temp = [int(x) for x in line.split()]   
        hist.append(temp)

def identifier(nums): 
    for i in nums: 
        if i != 0: 
            return False 
    return True 

def find_differences(nums): 
    temp = []
    for i in range(1, len(nums)): 
        temp.append(nums[i] - nums[i - 1])
    return temp 

def func(nums): 
    temp = []
    temp.append(nums)
    while not identifier(nums): 
        nums = find_differences(nums)
        temp.append(nums)
    return temp 

def append_to_end(nums): 
    temp = func(nums)
    for i in range(len(temp) - 2, -1, -1):
        temp[i].append(temp[i + 1][-1] + temp[i][-1])
    return temp 

def find_history(nums):
    temp = append_to_end(nums)
    return temp[0][-1]

def sum_history(list1): 
    total = 0
    for i in list1: 
        x = find_history(i)
        total += x 
    return total 

print(sum_history(hist))

