#どうやってもTLEする（C系じゃないと無理）(numpy,scipyを使えばいけるっぽい)
n, k = map(int, input().split())
a = input().split()
h = [int(m) for m in a]
#dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]))
dp = [float("INF")] * (n + 1)
dp[0] = 0
dp[1] = 0
dp[2] = abs(h[1] - h[0])
for i in range(3, n + 1):
    for j in range(k):
        if i - 2 - j >= 0:
            if dp[i] > dp[i - 1 - j] + abs(h[i - 1] - h[i - 2 - j]):
                dp[i] = dp[i - 1 - j] + abs(h[i - 1] - h[i - 2 - j])
        else:
            break

print(dp[n])