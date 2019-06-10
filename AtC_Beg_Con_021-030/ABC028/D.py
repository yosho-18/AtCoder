n, k = map(int, input().split())
print((k * (n - k + 1) * 6 - (k - 1) * 3 - (n - k) * 3 - 5) / n ** 3)