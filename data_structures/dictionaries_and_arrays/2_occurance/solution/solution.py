# Write your solution here
from array import *
def occurences(array_num, element):
    count = 0
    for i in array_num:
        if i in element:
            count += 1
            
    return count

# array_num =array("i", [1, 3, 5, 3, 7, 9]) 
# print(occurences(array_num, 3))