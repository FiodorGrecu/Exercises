# Code your solution here
def count_even(*args):
    return len([n for n in args if n%2 == 0])
print(count_even(1,2,3,4,5,6,7))