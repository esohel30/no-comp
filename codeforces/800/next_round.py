n,k = [int(x) for x in input().split()]
ranks = [int(x) for x in input().split()]
k_score = ranks[k - 1]

count = 0 
for i in ranks: 
    if i >= k_score and i > 0: 
        count += 1

print(count)