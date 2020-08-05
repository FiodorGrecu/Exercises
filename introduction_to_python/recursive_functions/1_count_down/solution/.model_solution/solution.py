def count_down_from(num):
    if num >= 1:
        print(num)
        print(count_down_from(num-1))
