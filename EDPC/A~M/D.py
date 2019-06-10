#どうやってもTLEする（C系じゃないと無理）
n, w = map(int, input().split())
c = []
for i in range(n):#h:高さ
    c.append([int(m) for m in input().split()])
dp = []
for i in range(n):
    dp.append([])
for i in range(n):
    for j in range(w + 1):
        dp[i].append(0)
dp[0][c[0][0]] = c[0][1]
#dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - c[i][0](w)] + c[i][1](v))
#max(dp[n - 1])
for i in range(1, n):
    for j in range(w + 1):
        if j - c[i][0] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - c[i][0]] + c[i][1])
        else:
            dp[i][j] = dp[i - 1][j]
print(max(dp[n - 1]))