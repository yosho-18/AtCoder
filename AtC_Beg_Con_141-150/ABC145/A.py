n = int(input())
ans = float("INF")
for i in range(1, n):
    t = list(str(n - i))
    t = [int(m) for m in t]
    u = list(str(i))
    u = [int(m) for m in u]
    if ans > int(sum(t) + sum(u)):
        ans = int(sum(t) + sum(u))
print(ans)