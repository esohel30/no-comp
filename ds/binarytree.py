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

# dfs iterative using manual stack 
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

# dfs recursive using recursive stack 

def depth_first_recursive(root, values = []): 

    if root: 
        values.append(root.val)
        depth_first_recursive(root.left, values)
        depth_first_recursive(root.right, values)

    return values

print(depth_first_recursive(A))