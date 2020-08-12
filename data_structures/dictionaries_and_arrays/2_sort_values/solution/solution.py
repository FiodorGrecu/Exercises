# Write your solution here
import operator

def sort_dict(my_dictionary):
    dictionary = dict(sorted(my_dictionary.items(),key=operator.itemgetter(0,0)))
    return dictionary
my_dict = {3:"a", 6: "b", 1: "c"}
print(sort_dict(my_dict))           