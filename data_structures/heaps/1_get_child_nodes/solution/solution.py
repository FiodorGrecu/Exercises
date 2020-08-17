# Write your solution here
def get_child_nodes(heap, index):
    left_index = 2*index + 1
    right_index = 2* index + 2 
    chil_lst = []
    if left_index < len(heap):
        chil_lst.append(heap[left_index])
    if right_index < len(heap):
        chil_lst.append(heap[right_index])
    return chil_lst

print(get_child_nodes([2,3,4,5,10], 0))
print(get_child_nodes([2, 3, 4, 5, 10], 1))

    