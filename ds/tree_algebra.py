class Node: 
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 


a = Node('-')
b = Node('/')
c = Node('+')
d = Node('*')
e = Node('+')
f = Node('*')
g = Node(6)
h = Node('+')
i = Node(3)
j = Node('-')
k = Node(2)
l = Node(3)
m = Node('-')
n = Node(3)
o = Node(1)
p = Node(9)
q = Node(5)
r = Node(7)
s = Node(4)

#                 a
#           /          \ 
#         b            c
#       /   \         /  \
#     d      e       f    g  
#    / \    / \      /\
#   h   i  j   k    l  m 
#  /\     /\           /\ 
# n o     p q         r s 


a.left = b 
a.right = c 
b.left = d 
b.right = e 
c.left = f 
c.right = g
d.left = h 
d.right = i 
e.left = j 
e.right = k 
f.left = l 
f.right = m 
h.right = n
h.left = o 
j.left = p 
j.right = q 
m.left = r 
m.right = s 




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

