s = input()
n = len(s)
ans = 0
tmp = 0
for i in range(n):
    if s[i] == "+":
        if tmp == 0:
            ans += 1
        tmp = 0
    elif s[i] == "*":
        pass
    else:
        if s[i] == "0":
            tmp += 1
if tmp == 0:
    ans += 1
print(ans)