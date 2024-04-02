class Node: 
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

z = None
a = Node(100)
b = Node(50)
c = Node(25)
d = Node(20)
e = Node(10)
f = Node(5)

a.left = b 
b.left = c 
c.left = d 
d.left = e 
e.left = f

def findmin(root, min_val): 
    if root == None: 
        return min_val
    
    min_val = min(min_val, root.val)
    return findmin(root.left, min_val)


print(findmin(z, float('inf')))
