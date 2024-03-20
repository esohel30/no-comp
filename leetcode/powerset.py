nums = [1,2,3]

# combinatorics 101 

storage = []
def power_set(nums, index, temp):
    
    if index == len(nums):
        storage.append(temp) # why copy ? 
        return 
    
    power_set(nums, index + 1, temp[:])
    temp.append(nums[index])
    power_set(nums, index + 1, temp[:])


power_set(nums, 0, [])
print(storage)



for i in range(1, 41):
    temp = "*" * i 
    print(temp)

