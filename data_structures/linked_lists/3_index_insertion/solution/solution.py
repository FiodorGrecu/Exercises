#Write your answers here 
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head 
    
    def insert_at_index(self, index,  data):
        cur_index =1 
        cur_node = self.head
        while(cur_index < index):
            cur_node = cur_node.next
            cur_index += 1
        next_node = cur_node.next
        next_node = Node(data)
        next_node.next = next_node
        cur_node.next= next_node