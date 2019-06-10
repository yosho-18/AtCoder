n, m = map(int, input().split())
a = [int(m) for m in input().split()]
b = [int(m) for m in input().split()]
mod = 10 ** 9 + 7
fig = []
for i in range(n * m + 1):
    fig.append(i)
al = []
tmp = 1
p = []
for i in range(n):
    for j in range(m):
        if a[i] >= b[j]:
            p.append(b[j])
        elif a[i] < b[j]:
            p.append(a[i])

ans = 1
p.sort()
for i in range(n * m):
    if p[i] < i + 1:
        print(0)
        exit()
    p[i] -= i

for i in range(n * m):
    ans = ans * p[i] % mod
print(ans)