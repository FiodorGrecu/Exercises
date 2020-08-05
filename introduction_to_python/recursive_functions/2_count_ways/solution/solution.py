# Write your solution here
def fibonacci(n):
    if n <= 1: 
        return n 
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def count_ways(steps): 
    return fibonacci(steps + 1)

print(count_ways(10))