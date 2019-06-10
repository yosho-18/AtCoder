#横にn個入力
n, k = map(int, input().split())
a = [int(m) for m in input().split()]
b = []
t = 0
for i in range(n):
    t += a[i]
    b.append(t)

ans = 0
for i in range(n - k + 1):
    if i == 0:
        ans += b[k - 1]
    else:
        ans += b[k - 1 + i] - b[i - 1]
print(ans)