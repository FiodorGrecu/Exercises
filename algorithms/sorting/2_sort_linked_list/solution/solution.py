class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def sort_ll(self):
        curr = self.head
        index = None
        
        if self.head == None:
                return
        else:
            while (curr != None):
                index = curr.next
                while (index != None):
                    if (curr.value > index.value):
                        temp = curr.value
                        curr.value = index.value
                        index.value = temp
                    index = index.next
                curr = curr.next

n1 = ListNode(5)
n2 = ListNode(6, n1)
n3 = ListNode(4, n2)
n4 = ListNode(1, n3)
llst = LinkedList(n4)

def printlst(lst):
    curr = lst.head
    while(curr != None):
        print(curr.value)
        curr = curr.next


printlst(llst)
llst.sort_ll()
print(llst.head.next.next.value)

llst.sort_ll()
# print(printlst(llst))

