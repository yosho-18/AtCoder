n = int(input())
a = []
b = []
for i in range(n):#h:高さ
    pi, qi = map(int, input().split())
    a.append(pi)
    b.append(qi)

ans = 0
tmp = 0
for i in reversed(range(n)):
    if a[i] % b[i] != 0:
        ans += b[i] - (a[i] % b[i])
    if i != 0:
        a[i - 1] += ans
print(ans)