def binary_search_helper(lst, x, low, high):
    if high>= low:
        mid = (low + high) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            return binary_search_helper(lst, x, low, mid-1)
        else:
            return binary_search_helper(lst, x, mid+1, high)
    else:
        return -1 #f'no such number in_this_array'

def binary_search(lst, x):
    return binary_search_helper(lst, x, 0, len(lst)-1)

print(binary_search([1, 2, 4, 5, 9, 10, 11], 8))