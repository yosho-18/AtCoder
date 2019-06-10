
#MAX_N = 25; # nの最大値

#入力
n, W = map(int, input().split())
s = []
for i in range(n):#h:高さ
    s.append([int(m) for m in input().split()])
w = []
v = []
for i in range(n):
    w.append(s[i][0])
    v.append(s[i][1])
# DPテーブル
# dp[i][j]はi番目以降の品物から重さの和がj以下なるように選んだときの価値の和の最大値を表す。
dp = []
for i in range(n + 1):
    dp.append([])
for p in range(n + 1):
    for q in range(W + 1):
        dp[p].append(-1)

#iが大きくjが小さい順（使える品物と容量が少ない順）にメモの値が確定
#def solve_dp2():
for j in range(W + 1):
    dp[n][j] = 0
for i in range(n - 1, -1, -1):
    for j in range(W + 1):
      if j < w[i]:
        dp[i][j] = dp[i + 1][j]
      else:
        dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i])

print(dp[0][W])
