s = input()
word = ""
ans = 1
for i in range(len(s)):
    if i == 0:
        word = s[i]
    else:
        if word >= s[i]:
            ans += 1
            word = s[i]
print(ans)