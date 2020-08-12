# Write your solution here
from array import *
def occurance(array_num,element):
    count = 0
    for i in array_num:
        if i == element:
            count +=1
    return count 
# array_num = array("i", [1, 3, 5, 3, 7, 9]) 
# print(occurance(array_num,3))