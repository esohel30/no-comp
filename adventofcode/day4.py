with open('day4.txt', 'r') as file: 
    winners = []
    found = []
    for line in file:
        temp = line.split()
        w = temp[2:12]
        f = temp[13:]
        winners.append(w)
        found.append(f)


def findIntersection(list1, list2): 
    set1 = set(list1)
    counter = 0

    for i in list2: 
        if i in set1: 
            counter += 1
    
    return counter 

def pointsfinder(x):
    if x == 0: 
        return 0 
    else:  
        return 2 ** (x - 1)

total = 0 
for i in range(len(winners)): 
   total += pointsfinder(findIntersection(winners[i], found[i]))

print(total)