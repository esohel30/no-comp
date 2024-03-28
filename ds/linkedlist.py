class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None 
    
class LinkedList: 
    def __init__(self): 
        self.head = None 
    
    def append(self, data):
        new_node = Node(data)
        if not self.head: 
            self.head = new_node 
            return 
        last_node = self.head 
        while last_node.next: 
            last_node = last_node.next
        last_node.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node 
    
    def insert_after_node(self, prev_node, data):
        if not prev_node: 
            print("Previous node not in the list")
            return 
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node 

    def print_list(self):
        current = self.head
        while current: 
            print(current.data, end = " ")
            current = current.next
        print()

llist = LinkedList()
llist.append(3)
llist.append(4)
llist.append(5)
llist.prepend(2)
llist.print_list()