n = int(input())
a = input().split()
a = [int(m) for m in a]
ans = float("INF")

for i in range(-100, 101):
    tmp = 0
    for j in range(n):
        tmp += (a[j] - i) ** 2
    if ans > tmp:
        ans = tmp
print(ans)