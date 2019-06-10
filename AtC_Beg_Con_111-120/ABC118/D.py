n, m = map(int, input().split())
a = [int(m) for m in input().split()]
a.sort(reverse=True)
dp = []
for i in range(10 * n):
    dp.append(0)

b = [0,2,5,5,4,5,6,3,7,6]
for i in range(1, n + 1):
    for j in range(len(a)):
        if i - b[a[j]] >= 0:
            if (dp[i - b[a[j]]] == 0 and i - b[a[j]] == 0) or dp[i - b[a[j]]] != 0:
                dp[i] = max(dp[i], dp[i - b[a[j]]] + a[j])
        else:
            pass
    if i != n:
        dp[i] *= 10

print(dp[n])