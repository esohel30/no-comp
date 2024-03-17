#find all multiples of 3 or 5 under 1000 
total = 0 
for i in range(1000): 
    if i % 3 == 0 or i % 5 == 0: 
        print(i)
        total += i 

print(total)