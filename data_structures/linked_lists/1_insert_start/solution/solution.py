# Write your solution here
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head
        

    def llprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def insert_at_start(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

list1 = linkedList()
list1.head = Node("a")
e2 = Node("b")
e3 = Node("c")

list1.head.next = e2
e2.next = e3

list1.insert_at_start("d")
print(list1.llprint())