class Node():
    def __init__(self, val): 
        self.val = val 
        self.left = None 
        self.right = None 
    
# setting up the nodes of the binary tree 
A = Node('A')
B = Node("B")
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

# establishing the edges 
A.left = B 
A.right = C 
B.left  = D
B.right = E
C.right = F 

def depth_first_values(root):
    if root == None:
        return []
    
    res = []
    stack = [root]

    while stack: 
        current = stack.pop()
        res.append(current.val)
        if current.right: 
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return res 

print(depth_first_values(A))