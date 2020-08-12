# Write your answers her
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, head=None):
        self.head = head
       
    def delete_end(self):
        if self.head is None:
            return
        node = self.head
        while node.next.next is not None:
            node = node.next
        node.next = None
      
    

    # def __str__(self):
    #     if self.head:
    #         return f"<{self.head}>"
    #     else:
    #         return "<>"

# list1 == LinkedList.from_range(1,4)
# print(list1)
# sampleLL = Node(5, Node(3, Node(-1, None)))
# sampleLL.delete_end()
# sampleLL == Node(5, Node(3, None))