# Write your solution here
def is_leaf(heap, index): 
        if index >= (len(heap)// 2) and index < len(heap):
                return True
        return False


print(is_leaf([1, 2, 3, 4, 5, 6], 1))