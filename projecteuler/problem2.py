# Recursively 
def fib(x): 
    if x == 0 or x == 1: 
        return 1 
    return fib(x - 1) + fib(x - 2)


def find_even_fib_sum(limit): 
    i = 1 
    total = 0 
    while fib(i) < limit: 
        temp = fib(i)
        if temp % 2 == 0: 
            total += temp 
        i += 1

    return total 

# non recursively 

def fib(n): 
    if n <= 0: 
        return 0 
    elif n == 1:
        return 1    
    else:
        a, b = 0, 1
        for _ in range(1, n): # because of n ! 
            a, b = b, a + b

    return b 

for i in range(5):
    print(fib(i))