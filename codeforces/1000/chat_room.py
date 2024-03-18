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

print(solve(s))



