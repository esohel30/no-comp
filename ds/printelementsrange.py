class Node(): 
    def __init__(self, val): 
        self.val = val
        self.right = None 
        self.left = None 


a = Node(8)
b = Node(3)
c = Node(10)
d = Node(1)
e = Node(6)
f = Node(14)
g = Node(4)
h = Node(7)
i = Node(13)

a.left = b 
a.right = c 
b.left = d
b.right = e 
c.right = f
e.left = g
e.right = h 
f.left = i 
 
temp = []

def printelementsrange(root, a, b): 
    if root == None: 
        return 
    
    if a <= root.val and root.val <= b: 
        print(root.val)

    if root.val < b: 
        printelementsrange(root.right, a, b)
    if root.val > a: 
        printelementsrange(root.left, a, b)
    

printelementsrange(a, 4, 10)    

