class Node: 
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 


a = Node('*')
b = Node('/')
c = Node(8)
d = Node('*')
e = Node('+')
f = Node('+')
g = Node('-')
h = Node('+')
i = Node('-')
j = Node(5)
k = Node(2)
l = Node(2)
m = Node(1)
n = Node(2)
o = Node(9)
p = Node('-')
q = Node(1)
r = Node(7)
s = Node(2)


a.left = b 
a.right = c 
b.left = d 
b.right = e 
d.left = f
d.right = g 
e.left  = h 
e.right = i 
f.left = j 
f.right = k 
g.left = l 
g.right = m 
h.left = n 
h.right = o 
i.left = p 
i.right = q
p.left = r 
p.right = s


def tree_algebra(root):
    if root == None: 
        return 0 
    if root.right == None and root.left == None: 
        return root.val 
    if root.val == "+": 
        return tree_algebra(root.left) + tree_algebra(root.right)
    elif root.val == "-": 
        return tree_algebra(root.left) - tree_algebra(root.right)
    elif root.val == "*": 
        return tree_algebra(root.left) * tree_algebra(root.right)
    elif root.val == "/": 
         return tree_algebra(root.left) / tree_algebra(root.right)


print(tree_algebra(a))

