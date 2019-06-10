s = input()
n = len(s)
ans = 0
for i in range(n):
    if s[i] == "U":
        ans += 1 * (n - (i + 1))
        ans += 2 * i
    else:
        ans += 2 * (n - (i + 1))
        ans += 1 * i
print(ans)