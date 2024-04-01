class Node: 
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

z = None
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b 
a.right = c 
b.left = d 
b.right = e 
c.right = f 


def countNodes(curr): 
    if curr == None: 
        return 0 
    
    return 1 + countNodes(curr.left) + countNodes(curr.right)

print(countNodes(z))
