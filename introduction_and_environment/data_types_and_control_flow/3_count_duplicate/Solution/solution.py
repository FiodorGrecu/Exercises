# Code your solution here
list_dup = ["a","b","a","c","d","a"]
tot = []
total = 0
for char in list_dup:
    if char == "a":
        total += 1
tot.append(total)
print(tot)