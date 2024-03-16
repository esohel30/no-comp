def good_game(data): 
    id = int(data[1][: -1])
        
    for i in range(len(data)):
        if data[i][0] == 'g': 
            if int(data[i - 1]) > 13: 
                return 0
        elif data[i][0] == 'r': 
            if int(data[i - 1]) > 12: 
                return 0 
        elif data[i][0] == 'b': 
            if int(data[i - 1]) > 14: 
                return 0 

    return id 

with open('day2.txt', 'r') as file:
    total = 0 
    for line in file:
        game = line.split()
        total += good_game(game)
    
print(total)

