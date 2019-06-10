s = input()
li = []
for i in range(len(s)):
    if i >= 2:
        t = s[i - 2] + s[i - 1] + s[i]
        t = int(t)
        u = abs(753 - t)
        li.append(u)
print(min(li))