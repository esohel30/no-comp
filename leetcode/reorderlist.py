class Node():
    def __init__(self, val = 0): 
        self.val = val 
        self.next = None 
    
dummy = Node()
temp = dummy 
for i in range(1, 22): 
    temp.next = Node(i)
    temp = temp.next 

dummy = dummy.next 
head = dummy 

slow, fast = head, head.next 
while fast and fast.next: # the second next might be on null: careful. 
    slow = slow.next 
    fast = fast.next.next 

slow = slow.next 

while slow: 
    print(slow.val)
    slow = slow.next

# the first one always gets more. Well we do move it one afterwards.
    



