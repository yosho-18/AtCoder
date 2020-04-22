n, m = [int(m) for m in input().split()]
a = [int(m) for m in input().split()]
print(n - sum(a) if n - sum(a) >= 0 else -1)