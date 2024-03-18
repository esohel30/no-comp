temp = []

def gen_recursively(length, current = ""):
    if length == 0: 
        temp.append(current)
    else: 
        gen_recursively(length - 1, current + '4')
        gen_recursively(length - 1, current + '7' )

def gen_all(length):
    for i in range(length): 
        gen_recursively(i + 1)
    
c = input()

def solve_puzzle(x):
    length = len(x)
    gen_all(length) 
    if x in temp: 
        return "YES" 

    var = [int(a) for a in temp]
    x = int(x)
    
    for i in var: 
        if x % i == 0:
            return "YES" 

    return "NO" 

print(solve_puzzle(c))


