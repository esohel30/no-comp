nums = [1,2,3]

# combinatorics 101 

storage = []
def power_set(nums, index, temp):
    
    if index == len(nums):
        storage.append(temp[:])
        return 
    
    
    power_set(nums, index + 1, temp)
    temp.append(nums[index])
    power_set(nums, index + 1, temp)
    temp.pop()


power_set(nums, 0, [])
print(storage)