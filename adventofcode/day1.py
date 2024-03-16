def isNum(x):
    diff = ord('9') - ord(x)

    if diff <= 9 and diff >= 0: 
        return True 
    else: 
        return False 
    


with open('day1.txt', 'r') as file:
    total = 0 
    for line in file: 
        first, last = 0, 0
        for c in line: 
            if isNum(c): 
                first = int(c)
                break
        
        for c in line[::-1]: 
            if isNum(c): 
                last = int(c)
                break 
        
        total += (10 * first) + last 

print(total)