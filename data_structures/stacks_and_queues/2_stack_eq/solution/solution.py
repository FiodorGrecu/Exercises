class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head_node = None

    def push(self, value):
        new_head = ListNode(value)
        new_head.next = self.head_node
        self.head_node = new_head

    def pop(self):
        if self.head_node:
            value = self.head_node.value
            self.head_node = self.head_node.next
            return value
        else:
            raise IndexError

    # You may want to solve this magic method first!
    def __len__(self):
        cur_node = self.head_node
        num_nodes = 0
        while (cur_node):
            num_nodes += 1
            cur_node = cur_node.next
        return num_nodes
            

    # Fill in the code for __len__
    def __eq__(self, other):
        if (len(self) == len(other)):
            cur_node1 = self.head_node
            cur_node2 = self.head_node
            while (cur_node1):
                if not cur_node1.value == cur_node2.value:
                    return False
                else:
                    cur_node1 = cur_node1.next
                    cur_node2 = cur_node2.next
            return True
        return False

stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)

stack2 = Stack()
stack2.push(3)
stack2.push(2)
stack2.push(1) 

print(stack1 == stack2)


      