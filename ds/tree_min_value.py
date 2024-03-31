class Node: 
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 


a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(15)
f = Node(12)

a.left = b 
a.right = c 
b.left = d 
b.right = e 
c.right = f 


def tree_min_value(root):
    if root == None: return None 
    queue = [root]
    minimum = root.val
    while queue: 
        current = queue.pop()
        minimum = min(current.val, minimum)

        if current.left:
            queue.insert(0, current.left)
        if current.right:
            queue.insert(0, current.right)
    
    return minimum

print(tree_min_value(a))

def tree_min_values(root): 
    if root == None: 
        return float('inf')
    return min(root.val, tree_min_value(root.left), tree_min_value(root.right))

print(tree_min_value(a))