n, m, c = map(int, input().split())
b = [int(m) for m in input().split()]
a = []
for i in range(n):#h:高さ
    a.append([int(m) for m in input().split()])

tmp = 0
ans = 0
for i in range(n):
    for j in range(m):
        tmp += a[i][j] * b[j]
    if tmp > -c:
        ans += 1
    tmp = 0
print(ans)