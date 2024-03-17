nums = [1,2,3,4,5]

for i in range(len(nums)): 
    for j in range(nums[i]): 
        print("hello")
    print("bye")


def find_factors(x): 

    list  = []
    for i in range(1, x + 1):
        if x % i == 0: 
            list.append(i)

    return list 

print(find_factors(90))


def find_largest_factor(x): 
    
    list = []

    for i in range(1, x + 1): 
        if x % i == 0: 
            list.append(i)

    return list[-2]

print(find_largest_factor(90))