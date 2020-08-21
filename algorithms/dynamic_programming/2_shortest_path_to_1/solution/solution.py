def shortest_path_to_1(n):
    if n == 1:
        return 0
    if  n == 2 or n == 3:
        return 1
    memo = [-1 for i in range(n+1)]
    memo[1] = 0
    memo[2] = 1
    memo[3] = 1
    for i in range(4, n+1):
        if memo[i] == -1:
            if i%3 == 0 and 1%2 ==0:
                memo[i] = 1 + min(memo[i-1], memo[i//3], memo[i//2])
            elif i%3 == 0:
                memo[i] = 1 + min(memo[i-1], memo[i//3])
            elif i%2 == 0:
                memo[i] = 1 + min(memo[i-1], memo[i//2])
            else:
                memo[i] =1 + memo[i-1]
    return memo[n]

print(shortest_path_to_1(10))

        
            
# def shortest_path_to_1(n):
# 	count = 0
# 	while n > 1:
# 		if n % 2 == 0:             
# 			n = n // 2
# 		elif n == 3 or n % 4 == 1: 
# 			n = n - 1
# 		else:
# 			n = n + 1              
# 		count += 1
# 	return count
# print(shortest_path_to_1(1))

