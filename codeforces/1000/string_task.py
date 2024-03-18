
s = input()
s = s.lower()
data = []
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
for i in s: 
    if i not in vowels: 
        data.append('.')
        data.append(i)

print("".join(data))
    
