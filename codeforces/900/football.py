situation = input()
stack = []
printed = False

for i in situation: 
    if len(stack) == 0: 
        stack.append(i)
    else:
        if i != stack[-1]:
            stack.clear()
            stack.append(i)
       
        else: 
            stack.append(i)
            if len(stack) == 7:
                print("YES")
                printed = True
                break

if not printed:
    print("NO")
