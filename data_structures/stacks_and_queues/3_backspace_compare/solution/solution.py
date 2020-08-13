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
            cur_node2 = other.head_node
            while (cur_node1):
                if not cur_node1.value == cur_node2.value:
                    return False
                else:
                    cur_node1 = cur_node1.next
                    cur_node2 = cur_node2.next
            return True
        return False

    def __repr__(self):
        cur_node = self.head_node
        ret_str = ''
        while (cur_node):
            ret_str += cur_node.value
            cur_node = cur_node.next 
        return ret_str

def backspace_compare(str1, str2):
    stack1 = Stack()
    stack2 = Stack()
    for chr1 in str1:
        # print(f'str1:{chr}')
        if chr1 == "#":
            if len(stack1)>= 1:
                stack1.pop()
        else:
            stack1.push(chr1)
    for chr1 in str2:
        # print(f'str2:{chr}')
        if chr1 == "#":
            if len(stack2)>= 1:
                stack2.pop()
        else:
            stack2.push(chr1)
    print(stack1)      
    return stack1 == stack2

str1 = "ab#c"
str2 = "ad#c"
print(backspace_compare(str1,str2))
str1 = "a##c"
str2 = "#a#c"
print(backspace_compare(str1,str2))
str1 = "a#c"
str2 = "c#d"  

print(backspace_compare(str1,str2))