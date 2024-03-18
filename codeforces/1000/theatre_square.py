import math 

n, m, a = [int(x) for x in input().split()]

# break 2d problem into 1d problem. 
n_need = math.ceil(n/a)
m_need = math.ceil(m/a)
print(n_need * m_need)




