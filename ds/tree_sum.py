class Node: 
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b 
a.right = c 
b.left = d 
b.right = e 
c.right = f 


def tree_sum(root): # bfs iterative 
    res = 0 
    if root == None: 
        return res 
    
    queue = [root]  
    while queue: 
        current = queue.pop()
        res += current.val 

        if current.left: 
            queue.insert(0, current.left)
        if current.right: 
            queue.insert(0, current.right)

    return res 

print(tree_sum(a))


def tree_sum1(root): 
    if root == None: 
        return 0
    
    return root.val + tree_sum(root.left) + tree_sum(root.right)

print(tree_sum1(a))


