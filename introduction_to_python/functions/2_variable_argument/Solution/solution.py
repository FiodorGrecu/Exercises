# Code your solution here

def concat_args(*args):
    string = ""
    for i in args:
        string += i
    return  string

print(concat_args("Hello ","There ", "how ","is ","it ", 'going '))

