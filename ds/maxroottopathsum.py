class Node: 
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 


a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b 
a.right = c 
b.left = d 
b.right = e 
c.right = f 


def sum(root):
    if root == None:
        return -float('inf')
    if root.left == None and root.right == None: 
        return root.val 

    minimum = max(sum(root.left), sum(root.right))
    return minimum + root.val

print(sum(a))