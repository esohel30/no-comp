# read data into 2-d array 
with open('day3.txt', 'r') as file: 
    map = []
    for line in file: 
        map.append(line.strip())

row_len = len(map)
col_len = len(map[0])

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


def numLen(i, j): 
    length = 1
    while j < col_len - 1 and identity(map[i][j + 1]) == 1: 
        length += 1
        j += 1
    
    return length 

total = 0 

for i in range(len(map)): 
    j = 0 
    while j < col_len: 
        if identity(map[i][j]) == 1: 
            length = numLen(i, j)
            if length == 3: 
                if isPartNum(where_to_check(i, j)) or isPartNum(where_to_check(i, j + 1)) or isPartNum(where_to_check(i, j + 2)): 
                    total += (100 * int(map[i][j]) + 10 * int(map[i][j + 1]) + int(map[i][j + 2]))
            elif length == 2:
                if isPartNum(where_to_check(i, j)) or  isPartNum(where_to_check(i, j + 1)):
                    total += (10 * int(map[i][j]) + int(map[i][j + 1]))
            else: 
                if isPartNum(where_to_check(i, j)): 
                    total += (int(map[i][j]))

            j = j + length

        else: 
            j += 1 
         
print(total)