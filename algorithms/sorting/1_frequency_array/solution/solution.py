
def frequency_array(lst):
    max_elem = -1
    for i in lst:
        if i > max_elem:
            max_elem = i
    frequency_list = [0 for i in range(max_elem+1)] 

    for i in range(len(lst)):
        frequency_list[lst[i]] += 1
    return frequency_list

lst = [1, 1, 3, 4, 4, 5, 6, 8, 8, 8, 9]
print(frequency_array(lst))