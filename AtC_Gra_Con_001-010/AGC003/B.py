n = int(input())
d = []
for i in range(n):
    d.append(input())
# [d1, d2, d3, ..., dN]
a = [int(m) for m in d]#int型に直す
ans = 0
for i in range(n):
    if i == n - 1:
        ans += a[i] // 2
    else:
        ans += a[i] // 2
        ans += (a[i + 1] + a[i] % 2) // 2
        if a[i + 1] > 0:
            a[i + 1] = a[i + 1] + a[i] % 2 - ((a[i + 1] + a[i] % 2) // 2) * 2
        else:
            a[i + 1] = 0
print(ans)