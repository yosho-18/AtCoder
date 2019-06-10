n, m = map(int, input().split())
x = [int(m) for m in input().split()]
x.sort()
if m <= n:
    print(0)
else:
    dist = []
    for i in range(1, m):
        dist.append(x[i] - x[i - 1])
    tmp = 0
    dist.sort(reverse=True)
    for i in range(n - 1):
        tmp += dist[i]
    print(sum(dist) - tmp)