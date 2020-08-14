# Write your solutions here
class Node: 
	def __init__(self,key,left=None,right=None): 
		self.left = left
		self.right = right
		self.key = key
    
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

root = Node(6) 
root.left = Node(4) 
root.right = Node(7) 
root.left.left = Node(3) 
root.left.right = Node(5) 
  
  
print (f"Height of tree is: {height(root)}") 