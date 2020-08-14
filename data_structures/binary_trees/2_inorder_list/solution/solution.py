#Write your solutions here
class Node: 
	def __init__(self,key,left=None,right=None): 
		self.left = left
		self.right = right
		self.key = key
    
def Inorder(root):
    if not root:
        return []    
    return Inorder(root.left) + [root.key] + Inorder(root.right)
    # if root:
    #     Inorder(root.left)
    #     print(root.key)
    #     Inorder(root.right)

root = Node(6)
root.left = Node(4)
root.right = Node(7)
root.left.left = Node(3)
root.left.right = Node(5)

print(Inorder(root))