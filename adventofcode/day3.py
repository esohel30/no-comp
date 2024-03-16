# read data into 2-d array 
with open('day3.txt', 'r') as file: 
    map = []
    for line in file: 
        map.append(line.strip())

def identity(c): 
    if c == '.': 
        return 0 # if dot 
    
    temp = ord('9') - ord(c)
    if temp >= 0 and temp <= 9: 
        return 1 # if num 
    
    return 2 # if symbol 

def where_to_check(i, j): 
    res = []
    res.append([i - 1, j - 1])
    res.append([i - 1, j + 0])
    res.append([i - 1, j + 1])
    res.append([i + 0, j - 1])
    res.append([i + 0, j + 1])
    res.append([i + 1, j - 1])
    res.append([i + 1, j + 0])
    res.append([i + 1, j + 1])
    return res 

def isPartNum(cords): 
    for pair in cords: 
        if pair[0] < 0 or pair[0] >= len(map) or pair[1] < 0 or pair[1] >= len(map[0]): 
            continue
        else: 
            if identity(map[pair[0]][pair[1]]) == 2: 
                return True 
    
    return False 


