s = input()
p = 0
for i in s:
    if i == "C":
        p = 1
    if i == "F" and p == 1:
        p = 2
        break
print("Yes" if p == 2 else "No")
