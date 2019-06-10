n = int(input())
d = []
for i in range(n):#h:高さ
    d.append([int(m) for m in input().split()])
#dp = [None] * n
dp = []
for i in range(n + 1):
    dp.append([None, None, None])
dp[0][0] = d[0][0]#"A"
dp[0][1] = d[0][1]#"B"
dp[0][2] = d[0][2]#"C"
#dp[1][0] = d[0][0]#"A"
#dp[1][1] = d[0][1]#"B"
#dp[1][2] = d[0][2]#"C"
#dp[i] = max(dp[i - 2]["A"] + d[i - 1][1], dp[i - 2]["A"] + d[i - 1][2], dp[i - 2]["B"] + d[i - 1][0], dp[i - 2]["B"] + d[i - 1][2], dp[i - 2]["C"] + d[i - 1][0], dp[i - 2]["C"] + d[i - 1][1])
for i in range(1, n):
    dp[i][0] = max(dp[i - 1][1] + d[i][0], dp[i - 1][2] + d[i][0])
    dp[i][1] = max(dp[i - 1][0] + d[i][1], dp[i - 1][2] + d[i][1])
    dp[i][2] = max(dp[i - 1][0] + d[i][2], dp[i - 1][1] + d[i][2])
print(max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))