n, m = map(int, input().split())
p = m // 2
if p <= n:
    print(p)
else:
    print(n + (m - n * 2) // 4)