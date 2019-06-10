s = input()
t = ""
ans = 0
tmp = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        if s[j] in ["A", "G", "C", "T"]:
            t += s[j]
            if j == len(s) - 1:
                tmp = max(tmp, len(t))
                t = ""
                ans = 0
        else:
            tmp = max(tmp, len(t))
            t = ""
            ans = 0

            break
print(tmp)