n = int(input())
a = [int(m) for m in input().split()]
b = [int(abs(a[i] - a[i - 1])) for i in range(1, n)]
dp = [float("INF") for _ in range(n)]
dp[0] = 0
dp[1] = abs(a[0] - a[1])
for i in range(2, n):
    dp[i] = min(dp[i - 1] + abs(a[i] - a[i - 1]), dp[i - 2] + abs(a[i] - a[i - 2]))

print(dp[n - 1])