class Node: 
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 


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

#      a 
#     | \
#    b   c
#   / \   \ 
#  d  e    f  

# These are the relationships that we have established. 

# bfs only has a iterative approach and no recursive approach. 

def bfs(root): 
    if root == None: 
        return []
    
    queue = [root]
    res = []

    while queue:
        current = queue.pop()
        res.append(current.val)
        if current.left:
            queue.insert(0, current.left)
        if current.right:
            queue.insert(0, current.right) 

    return res 

# note that this bfs does not have the right time complexity of O(n) as we 
# are using a list instead of a queue. 

print(bfs(a))



