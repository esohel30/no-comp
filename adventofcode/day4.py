with open('day4.txt', 'r') as file: 
    winners = []
    found = []
    for line in file:
        temp = line.split()
        w = temp[2:12]
        f = temp[13:]
        winners.append(w)
        found.append(f)


def find_intersection(list1, list2): 
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
   total += pointsfinder(find_intersection(winners[i], found[i]))

## Part two 

def find_winnings(game_number): # return the cards won in a list form. 
    match_count = find_intersection(winners[game_number], found[game_number])
    return [game_number + i for i in range(1, match_count + 1)]


def find_tot(game_numbers):
    if not game_numbers:
        return

    new_games = []
    for game_number in game_numbers:
        winnings = find_winnings(game_number)
        for won_game in winnings:
            amounts[won_game] += 1  
            new_games.append(won_game)  
    
    find_tot(new_games) # this way leads to less amount of recursion used. 

amounts = [1] * len(winners)

find_tot(list(range(len(winners))))

total_cards = sum(amounts)

print(total_cards)