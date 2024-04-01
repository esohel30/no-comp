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


class Solution:
    def isValidBST(self, root: Optional[Node]) -> bool:
        
        def helper(node, left, right): 
            if node == None: 
                return True 
            

            if node.val < right and node.val > left:
                return helper(node.left, left, node.val) and helper(node.right, node.val, right)
             
            return False 

            
        
        return helper(root, float("-inf"), float("inf"))