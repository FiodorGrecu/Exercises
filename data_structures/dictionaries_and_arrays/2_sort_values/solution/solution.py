# Write your solution here
import operator

def sort_dict(my_dictionary):
    dictionary = dict(sorted(my_dictionary.items(),key=operator.itemgetter(0,1)))
    return dictionary
my_dict = {1:"z", 2: "y", 3: "a"}
print(sort_dict(my_dict))           