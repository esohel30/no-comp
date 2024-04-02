arr = [None, 8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13, None]



def validate(nums): 
    return helper(nums, 1, float("-inf"), float("inf"))

def helper(nums, i, left, right): 
    if i > len(nums): 
        return True
    if nums[i] == None: 
        return True 

    if left < nums[i] and nums[i] < right: 
        return helper(nums, 2 * i, left, nums[i]) and helper(nums, 2 * i + 1, nums[i], right)
    
    return False 
    
print(validate(arr))