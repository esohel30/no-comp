class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    if root is None:
        return []
    # First, visit the root node
    result = [root.val]
    # Then, traverse the left subtree
    result.extend(preorderTraversal(root.left))
    # Finally, traverse the right subtree
    result.extend(preorderTraversal(root.right))
    return result

def inorderTraversal(root):
    if root is None:
        return []
    result = []
    # First, traverse the left subtree
    result.extend(inorderTraversal(root.left))
    # Then, visit the root node
    result.append(root.val)
    # Finally, traverse the right subtree
    result.extend(inorderTraversal(root.right))
    return result

# Example usage
if __name__ == "__main__":
    # Construct a binary tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    e = TreeNode('E')
    x = TreeNode('X')
    n = TreeNode('N')
    a = TreeNode('A')
    u = TreeNode('U')
    m = TreeNode('M')
    f = TreeNode('F')

    e.left = x
    e.right = n
    x.left = a 
    x.right = u 
    a.left = m 
    a.right = f 

    preorder_result = preorderTraversal(e)
    inorder_result = inorderTraversal(e)
    print("Preorder traversal:", preorder_result)
    print("Inorder traversal:", inorder_result)
