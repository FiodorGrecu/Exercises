# Code your solution here
string = "BYTE ACADEMY"
# string = string.lower()
# string = string.replace(' ','')
data = []
vowels = ["A","E","I","O","U"]
for i in range(0,len(string),1):
    if string[i] in vowels:
        pass
    elif string[i] not in vowels:
        data.append(string[i])
print(data)
