# Write your solution heref
from array import array
def insert_element(array_num,ins_pos,ins_val):
    array_num.insert(ins_pos,ins_val)
    return array_num

print(insert_element(array("i",[1,2,3]),1,0))