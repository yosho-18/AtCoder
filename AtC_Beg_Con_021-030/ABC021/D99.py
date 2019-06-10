from itertools import accumulate
n = int(input())
k = int(input())

mod = 10 ** 9 + 7
if n <= 1000 and k <= 1000:
    dp = [[0] * 1001 for _ in range(1001)]

    for j in range(1001):
        if j != 0:
            dp[1][j] = 1

    accudp = []
    for i in range(2, k + 1):
        accudp.append(list(accumulate(dp[i - 1])))
        for j in range(1, n + 1):
            dp[i][j] = accudp[i - 2][j]
            dp[i][j] %= mod

    print(sum(dp[k]) % mod)

else:
    print("nan")