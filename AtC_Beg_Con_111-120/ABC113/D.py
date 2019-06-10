h, w, k = map(int, input().split())
if w == 1:
    print(1)
    exit()
mod = 10 ** 9 + 7

def fibo(w):
    if w == 0:
        return 1
    if w == 1:
        return 1
    elif w == 2:
        return 2
    else:
        return fibo(w - 1) + fibo(w - 2)

dp = []
for i in range(w + 1):
    dp.append([])
for i in range(w + 1):
    for j in range(h + 1):
        dp[i].append(0)
for i in range(w + 1):
    if i == 1:
        dp[i][1] = fibo(w - 1)
    elif i == 2:
        dp[i][1] = fibo(w) - fibo(w - 1)
for j in range(2, h + 1):
    for i in range(1, w + 1):
        if i == 1:
            dp[i][j] = (dp[i][j - 1] * fibo(w - 1) + dp[i + 1][j - 1] * (fibo(w) - fibo(w - 1))) % mod
        elif i == w:
            dp[i][j] = (dp[i - 1][j - 1] * (fibo(w) - fibo(w - 1)) + dp[i][j - 1] * fibo(w - 1)) % mod
        else:
            dp[i][j] = (dp[i - 1][j - 1] * (fibo(i - 2) * fibo(w - i)) + dp[i][j - 1] * (fibo(i - 1) * fibo(w - i)) + dp[i + 1][j - 1] * (fibo(i - 1) * fibo(w - i - 1))) % mod
print(dp[k][h] % mod)