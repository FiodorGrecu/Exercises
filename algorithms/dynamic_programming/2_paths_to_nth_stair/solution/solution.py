def paths_nth_stair(n):
    if n < 2:
        return n
    else:
        memo = [-1 for i in range(n+1)]
        memo[1] = 1
        memo[2] = 2 
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]

print(paths_nth_stair(4))

# def paths_nth_stair(n):
#     if n <= 1: 
#         return n 
#     else:
#         return paths_nth_stair(n-1) + paths_nth_stair(n-2)

# def count_ways(steps): 
#     return paths_nth_stair(steps + 1)

# # print(count_ways(10))



# print(paths_nth_stair(3))