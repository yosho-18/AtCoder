n = int(input())
mod = 10 ** 9 + 7
#部分点解法
dp = [[0, 0, 0] for i in range(3 * n)]
dp[0][0] = 1
dp[0][1] = 1

for i in range(1, 3 * n):
    dp[i][0] += dp[i - 1][1] % mod
    dp[i][0] += dp[i - 1][2] % mod
    dp[i][1] += dp[i - 1][0] % mod
    dp[i][1] += dp[i - 1][2] % mod
    if i % 3 != 0:
        dp[i][2] += dp[i - 1][0] % mod
        dp[i][2] += dp[i - 1][1] % mod

ans = 0
for i in range(3):
    ans += dp[3 * n - 1][i] % mod
print(ans % mod)