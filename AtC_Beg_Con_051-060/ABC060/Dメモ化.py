
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

# メモ化テーブル。
# dp[i][j]はi番目以降の品物から重さの和がj以下なるように選んだときの価値の和の最大値を表す。
# -1なら値が未決定であることを表す
dp = []
for i in range(n + 1):
    dp.append([])
for p in range(n + 1):
    for q in range(W + 1):
        dp[p].append(-1)

# i番目以降の品物から重さの和がj以下なるように選んだときの、
# 取りうる価値の総和の最大値を返す関数
def rec(i, j):
    if dp[i][j] != -1:
    # すでに調べたことがあるならその結果を再利用
        return dp[i][j]

    #res = 0
    if i == n:
    # 品物がもう残っていないときは、価値の和の最大値は0で確定
        res = 0
        dp[i][j] = res
    elif j < w[i]:
    # 残りの容量が足りず品物iを入れられないので、入れないパターンだけ処理
    # i+1 以降の品物のみを使ったときの最大値をそのままこの場合の最大値にする
        res = rec(i + 1, j)
        dp[i][j] = res
    else:
    # 品物iを入れるか入れないか選べるので、両方試して価値の和が大きい方を選ぶ
        res = max(rec(i + 1, j), rec(i + 1, j - w[i]) + v[i])#深さ優先探索
        dp[i][j] = res
    return dp[i][j]


print(rec(0, W))