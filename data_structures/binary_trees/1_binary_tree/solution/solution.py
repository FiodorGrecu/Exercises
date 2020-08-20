#Write your solutions here
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

# smaple_tree_list = []
leftN = Node(4)
rightN = Node(7)

sample_tree = Node(5, leftN, rightN)

print(sample_tree.key)
print(sample_tree.left.key)
print(sample_tree.right.key)





