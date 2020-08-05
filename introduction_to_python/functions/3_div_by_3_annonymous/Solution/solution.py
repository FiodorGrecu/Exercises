# Code your solution here
def div_by_3(*args):

    return list(filter(lambda x: x % 3 == 0 ,args))
# print(div_by_3(2, 3, 5, 6, 9))