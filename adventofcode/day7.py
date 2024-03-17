with open('day7.txt', 'r') as file: 
    hands = {}
    for line in file: 
        a,b = line.split()
        hands[a] = int(b)
        
def five_of_a_kind(hand):
    count = {}
    for i in hand: 
        count[i] = count.get(i, 0) + 1

    for suite in count:
        if count[suite] == 5:
            return True
        
    return False 

def four_of_a_kind(hand):
    count = {}
    for i in hand: 
        count[i] = count.get(i, 0) + 1
    
    for suite in count:
        if count[suite] == 4:
            return True 
    
    return False 

def full_house(hand): 
    count = {}
    for i in hand:
        count[i] = count.get(i, 0) + 1
    
    temp = list(count.values())
    temp.sort()

    return temp == [2,3] 

def three_of_a_kind(hand):
    count = {}
    for i in hand: 
        count[i] = count.get(i, 0) + 1

    temp = list(count.values())
    temp.sort()

    return temp == [1,1,3]

def two_pair(hand): 
    count = {}
    for i in hand: 
        count[i] = count.get(i, 0) + 1

    temp = list(count.values())
    temp.sort()

    return temp == [1,2,2]

def one_pair(hand): 
    count = {}
    for i in hand: 
        count[i] = count.get(i, 0) + 1

    temp = list(count.values())
    temp.sort()

    return temp == [1,1,1,2]

def high_card(hand):
    count = {}
    for i in hand: 
        count[i] = count.get(i, 0) + 1

    temp = list(count.values())

    return temp == [1,1,1,1,1] 

def comparison(hand1, hand2): 
    val1 = 0
    val2 = 0 

    if five_of_a_kind(hand1): 
        val1 = 7
    if five_of_a_kind(hand2): 
        val2 = 7 
    if four_of_a_kind(hand1): 
        val1 = 6
    if four_of_a_kind(hand2): 
        val2 = 6
    if full_house(hand1): 
        val1 = 5
    if full_house(hand2): 
        val2 = 5 
    if three_of_a_kind(hand1): 
        val1 = 4
    if three_of_a_kind(hand2): 
        val2 = 4
    if two_pair(hand1): 
        val1 = 3
    if two_pair(hand2): 
        val2 = 3
    if one_pair(hand1): 
        val1 = 2
    if one_pair(hand2): 
        val2 = 2
    if high_card(hand1): 
        val1 = 1
    if high_card(hand2): 
        val2 = 1
    
    if val1 > val2: 
        return 0
    elif val1 < val2: 
        return 1 
    else: 

        arr1 = []
        arr2 = []

        for card in hand1: 
            if card == 'A':
                arr1.append(14)
            elif card == 'K':
                arr1.append(13)
            elif card == 'Q':
                arr1.append(12)
            elif card == 'J': 
                arr1.append(11)
            elif card == 'T':
                arr1.append(10)
            else: 
                arr1.append(int(card))

        for card in hand2: 
            if card == 'A':
                arr2.append(14)
            elif card == 'K':
                arr2.append(13)
            elif card == 'Q':
                arr2.append(12)
            elif card == 'J': 
                arr2.append(11)
            elif card == 'T':
                arr2.append(10)
            else: 
                arr2.append(int(card))

        for i in range(len(arr1)):
            if arr1[i] > arr2[i]:
                return 0 
            elif arr1[i] < arr2[i]:
                return 1 
    
    return "wtf"
        

def ranker(hands): # monotonically increasing stack 

    stack = []
    for hand in hands: 
        if not stack: 
            stack.append(hand)
        else:       
            if comparison(stack[-1], hand) == 1: 
                stack.append(hand)
            else: 
                temp = []
                while stack and comparison(stack[-1], hand) == 0: 
                    temp.append(stack.pop())

                stack.append(hand)

                while temp: 
                    stack.append(temp.pop())

    return stack 

def calculate_points(hands): 
    rankings = ranker(hands)
    position = len(rankings)
    total = 0

    for i in rankings[::-1]:
        total += position * hands[i]
        position -= 1
    
    return total 


print(calculate_points(hands))



