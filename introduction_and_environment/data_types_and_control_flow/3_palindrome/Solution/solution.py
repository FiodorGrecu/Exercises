# Code your solution here
# line = input("Enter a word and I will tell you if is polindrome!: ")
line = "malayalam"
is_palindrome = []
if line == line[-1::-1]:
    is_palindrome.append(line[-1::-1])  
    # print("is palindrome! ")    
else:
    pass

print(is_palindrome)