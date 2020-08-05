# Write your solution here
def count_down_from(num):
    if num >= 1:
        print(num)
        return count_down_from(num -1)
print(count_down_from(6))  