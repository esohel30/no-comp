from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.middle = None
        self.right = None

# Create nodes
m = Node("m")
n = Node("n")
o = Node("o")
p = Node("p")
q = Node("q")
r = Node("r")
s = Node("s")
t = Node("t")
u = Node("u")
v = Node("v")
w = Node("w")
x = Node("x")
y = Node("y")
z = Node("z")

# Connect nodes as per the user's specification
m.left = q
m.middle = r
m.right = x

n.left = o
n.middle = q
n.right = u

o.left = r
o.middle = s
o.right = v

p.left = o
p.middle = s
p.right = z

q.left = t

r.left = u
r.middle = y

s.left = r

u.left = t

v.left = w

w.left = z

y.left = v

def bfs_corrected(start_node):
    queue = deque([start_node])
    visited = []
    seen = set()  # Using a set to track seen nodes to prevent re-enqueueing

    while queue:
        current_node = queue.popleft()
        if current_node.val not in seen:
            visited.append(current_node.val)
            seen.add(current_node.val)
            for node in [current_node.left, current_node.middle, current_node.right]:
                if node and node.val not in seen:
                    queue.append(node)
    return visited

# Start BFS from node 'm' with corrected duplicate handling
bfs_corrected_output = bfs_corrected(m)
print(bfs_corrected_output)


def dfs(node, visited=None):
    if visited is None:
        visited = []
    # Visit the node
    if node and node.val not in visited:
        visited.append(node.val)  # Add node to visited list
        # Recursively visit each child that hasn't been visited
        for next_node in [node.left, node.middle, node.right]:
            dfs(next_node, visited)
    return visited

# Start DFS from node 'm'
dfs_output = dfs(m)
print(dfs_output)