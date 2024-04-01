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
g = Node('g')
h = Node('h')
i = Node('i')
j = Node('j')
k = Node('k')
l = Node('l')

a.left = b 
a.right = c 
b.left = d 
b.right = e 
c.right = f 
d.left = g 
d.right = h 
e.left = i 
f.left = j
f.right = k
k.right = l 


def findheight(curr): 
    if curr == None: 
        return 0 
    
    return 1 + max(findheight(curr.left), findheight(curr.right))


print(findheight(a))