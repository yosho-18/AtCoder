n, x = map(int, input().split())
s = input()
d = []
for i in range(n):
    d.append(input())
# [d1, d2, d3, ..., dN]
t = [int(m) for m in d]#int型に直す

ans = 0
for i in range(n):
    if s[i] == "1":
        if t[i] > x:
            ans += x
        else:
            ans += t[i]
    else:
        ans += t[i]
print(ans)