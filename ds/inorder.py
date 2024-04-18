class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder_traversal(root):
    result = []
    if root:
        result = inorder_traversal(root.left)  # Visit left subtree
        result.append(root.val)                # Visit node itself
        result += inorder_traversal(root.right) # Visit right subtree
    return result

def postorder_traversal(root):
    result = []
    if root:
        result += postorder_traversal(root.left)   # Visit left subtree
        result += postorder_traversal(root.right)  # Visit right subtree
        result.append(root.val)                    # Visit node itself
    return result

def level_order_traversal(root):
    # This function performs a level-order traversal of the tree
    # and returns the values of the nodes in the order they were visited.
    result = []
    if not root:
        return result
    queue = [root]  # Initialize the queue with the root node
    while queue:
        current = queue.pop(0)  # Dequeue the front node
        result.append(current.val)  # Visit the current node
        if current.left:
            queue.append(current.left)  # Enqueue left child
        if current.right:
            queue.append(current.right)  # Enqueue right child
    return result

# Creating the nodes
root = Node(50)
b = Node(17)
c = Node(76)
d = Node(9)
e = Node(23)
f = Node(54)
g = Node(14)
h = Node(19)
i = Node(72)
j = Node(12)
k = Node(67)

# Constructing the tree
root.left = b
root.right = c
b.left = d
b.right = e
c.left = f
d.right = g
e.left = h
g.left = j
f.right = i
i.left = k

# Performing inorder traversal
inorder_result = inorder_traversal(root)
print("Inorder traversal result:", inorder_result)

# Performing postorder traversal
postorder_result = postorder_traversal(root)
print("Postorder traversal result:", postorder_result)

# Performing level-order traversal
level_order_result = level_order_traversal(root)
print("Level-order traversal result:", level_order_result)
