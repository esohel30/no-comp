n = int(input())
x_sum, y_sum, z_sum = 0, 0, 0

for _ in range(n): 
    x, y, z = [int(x) for x in input().split()]
    x_sum += x
    y_sum += y 
    z_sum += z 

if x_sum == 0 and y_sum == 0 and z_sum == 0: 
    print("YES")
else: 
    print("NO")


