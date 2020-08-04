# Code your solution here
def factorial(n):
    total = 1
    for i in range(1,n+1):
        total *= i
        print(i)
    return total
print(factorial(3))