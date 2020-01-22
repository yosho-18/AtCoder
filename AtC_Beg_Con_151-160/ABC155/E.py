S = input()
N = len(S)
MOD = 10 ** 9 + 7
dp = [[0] * 13 for i in range(N + 1)]
dp[0][0] = 1

for i, s in enumerate(S[::-1], start=1):
    p10 = pow(10, i - 1, 13)
    if s != '?':
        for k in range(13):
            dp[i][(int(s) * p10 + k) % 13] += dp[i - 1][k]
            dp[i][(int(s) * p10 + k) % 13] %= MOD
    else:
        for j in range(10):
            for k in range(13):
                dp[i][(j * p10 + k) % 13] += dp[i - 1][k]
                dp[i][(j * p10 + k) % 13] %= MOD

print(dp[N][5] % MOD)
