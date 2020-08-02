# Code your solution here
# marks = float(input("Enter your mark: "))
mark = 80
if mark >= 90 and mark<= 100:
    print ("You recieved an A")
elif mark >=70 and mark <= 90:
    print ("You recieved a B")
elif mark >=50 and mark <= 70:
    print ("You recieved a C")
elif mark >=35 and mark <= 50:
    print ("You recieved a D")
else:
    print ("You FAIL")
grade = int(mark)
print(grade)