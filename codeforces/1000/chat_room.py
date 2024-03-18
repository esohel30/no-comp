s = input()

def solve(s): 
    for i in range(len(s)): 
        if s[i] == 'h':
            for j in range(i + 1, len(s)):
                if s[j] == 'e':
                    for z in range(j + 1, len(s)):
                        if s[z] == 'l': 
                            for y in range(z + 1, len(s)): 
                                if s[y] == 'l':
                                    for a in range(y + 1, len(s)):
                                        if s[a] == 'o':
                                            return "YES"
                                            
    return "NO"

# What if given a much longer word to check. 

def solve_recursively(fast, slow, target, given): 
    if slow == len(target): 
        return "YES" 
    if fast >= len(given):
        return "NO"
    else: 
        if given[fast] == target[slow]:
            return solve_recursively(fast + 1, slow + 1, target, given)
        else: 
            return solve_recursively(fast + 1, slow, target, given)

print(solve_recursively(0,0,"hello", s))

