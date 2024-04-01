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

def count_leaf_nodes(root): 
    if root == None: 
        return 0
    if (root.left == None and root.right == None): 
        return 1 

    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

print(count_leaf_nodes(a))