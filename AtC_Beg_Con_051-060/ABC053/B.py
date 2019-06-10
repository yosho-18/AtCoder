s = input()
start = 0
goal = 0
p = 0
for i in range(len(s)):
    if s[i] == "A" and p == 0:
        start = i
        p = 1
    if s[i] == "Z":
        goal = i
print(goal - start + 1)
