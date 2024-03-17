n = int(input())
x = 0

for _ in range(n): 
    line = input()

    if line[0] == "+" or line[-1] == "+":
        x += 1
    else: 
        x -= 1
    
print(x)

