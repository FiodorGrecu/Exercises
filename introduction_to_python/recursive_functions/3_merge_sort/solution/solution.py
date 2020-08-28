# Write your solution here
def custom_sort(num_list):
    if len(num_list)>1: 
        m = len(num_list)//2
        left = num_list[:m] 
        right = num_list[m:] 
        left = custom_sort(left) 
        right = custom_sort(right) 
  
        num_list =[] 
  
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                num_list.append(left[0]) 
                left.pop(0) 
            else: 
                num_list.append(right[0]) 
                right.pop(0) 
  
        for i in left: 
            num_list.append(i) 
        for i in right: 
            num_list.append(i) 
                  
    return num_list 
alist = [12, 11, 13, 5, 6, 7]
alist = custom_sort(alist)
print(alist)