n = int(input())
s = input()
p = 0
ans = 0
for i in range(n - 1 , -1 ,-1):
    if s[i] == ".":
        p += 1
    elif s[i] == "#":
        ans += p
        p = 0
print(ans)