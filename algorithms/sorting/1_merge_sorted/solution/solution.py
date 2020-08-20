def merge_sorted(lst1, lst2): 
    def merge_helper(lst1, lst2, merged_lst):
        if len(lst1) == 0:
            merged_lst.extend(lst2)
            return merged_lst
        elif len(lst2) == 0:
            merged_lst.extend(lst1)
            return merged_lst
        elif lst1[0] <= lst2[0]:
            merged_lst.append(lst1[0])
            return merge_helper(lst1[1:], lst2, merged_lst)
        else: 
            merged_lst.append(lst2[0])
            return merge_helper(lst1, lst2[1:], merged_lst)
    return merge_helper(lst1, lst2, [])

lst1 = [-1, 1, 4, 6]
lst2 = [0, 1, 2, 5, 7]
print(merge_sorted(lst1, lst2))

#     final_list = list1 + list2 
#     final_list.sort() 
#     return(final_list) 
  
# # Driver Code 
# list1 = [1,3, 9, 10, 26, 31] 
# list2 = [-1, 3, 4, 5, 15, 20] 
# print(merge_sorted(list1, list2))       