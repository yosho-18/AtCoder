s = input()
dp = []
n = len(s)
mod = 10 ** 9 + 7
dp = [[] for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(4):
        dp[i].append(0)
dp[0][0] = 1
for i in range(n):
    for j in range(4):
        dp[i + 1][j] += dp[i][j] % mod
        if s[i] == "?":
            dp[i + 1][j] += dp[i][j] * 2 % mod
    if s[i] == "A":
        dp[i + 1][1] += dp[i][0] % mod
    elif s[i] == "B":
        dp[i + 1][2] += dp[i][1] % mod
    elif s[i] == "C":
        dp[i + 1][3] += dp[i][2] % mod
    elif s[i] == "?":
        dp[i + 1][1] += dp[i][0] % mod
        dp[i + 1][2] += dp[i][1] % mod
        dp[i + 1][3] += dp[i][2] % mod

print(dp[n][3] % mod)