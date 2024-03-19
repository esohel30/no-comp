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


# immutable objects in python are pass-by-value 
# mutable objects in python are pass-by-refrence 

power_set(nums, 0, [])
print(storage)
