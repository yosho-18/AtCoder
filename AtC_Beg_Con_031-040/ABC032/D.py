n, w = map(int, input().split())
vw = []
maxv = 0
for i in range(n):#h:高さ
    vw.append([int(m) for m in input().split()])
    maxv = max(maxv, vw[i][0])

#w <= 10 ** 3
if w <= 10 ** 3:
    dp = [[0] * (w + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(w + 1):
            dp[i][j] = max(dp[i - 1][j - w[i - 1][1]] + vw[i - 1][0], dp[i - 1][j])
    ans = max(dp[n])
    print(ans)

#v <= 10 ** 3
elif maxv <= 10 ** 3:
    dp = [[0] * (n * (maxv + 1)) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(n * (maxv + 1)):
            dp[i][j] = min(dp[i - 1][j - vw[i - 1][0]] + vw[i - 1][1], dp[i - 1][j])
    for j in range(n * (maxv + 1)):
        if dp[n][j] <= w and dp[n][j] != 0:
            ans = j
    print(ans)
#n <= 30
else:
    