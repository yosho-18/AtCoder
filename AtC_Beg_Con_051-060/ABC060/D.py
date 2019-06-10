#入力
n, W = map(int, input().split())
s = []
for i in range(n):#h:高さ
    s.append([int(m) for m in input().split()])
s.sort(key=lambda x:(x[0], x[1]))
s0 = []
s1 = []
s2 = []
s3 = []
for i in range(n):
    if i == 0:
        w0 = s[i][0]
        s0.append(s[i])
    elif s[i][0] == w0:
        s0.append(s[i])
    elif s[i][0] == w0 + 1:
        s1.append(s[i])
    elif s[i][0] == w0 + 2:
        s2.append(s[i])
    elif s[i][0] == w0 + 3:
        s3.append(s[i])
s0.sort(key=lambda x: x[1], reverse=True)
s1.sort(key=lambda x: x[1], reverse=True)
s2.sort(key=lambda x: x[1], reverse=True)
s3.sort(key=lambda x: x[1], reverse=True)
w = []
v = []
t0 = 0
t1 = 0
t2 = 0
t3 = 0
u0 = 0
u1 = 0
u2 = 0
u3 = 0
u = []
for h in range(-1, len(s0)):
    if h == -1:
        t0 = 0
        u0 = 0
    else:
        t0 += s0[h][0]
        u0 += s0[h][1]
    for i in range(-1, len(s1)):
        if i == -1:
            t1 = 0
            u1 = 0
        else:
            t1 += s1[i][0]
            u1 += s1[i][1]
        for j in range(-1, len(s2)):
            if j == -1:
                t2 = 0
                u2 = 0
            else:
                t2 += s2[j][0]
                u2 += s2[j][1]
            for k in range(-1, len(s3)):
                if k == -1:
                    t3 = 0
                    u3 = 0
                else:
                    t3 += s3[k][0]
                    u3 += s3[k][1]
                if t0 + t1 + t2 + t3 <= W:
                    u.append(u0 + u1 + u2 + u3)
print(max(u))



"""for i in range(n):
    w.append(s[i][0])
    v.append(s[i][1])
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
        res = max(rec(i + 1, j - s[i][1]) + s[i][0], rec(i + 1, j - s[i][1]) + s[i][0], rec(i + 1, j - s[i][1]) + s[i][0],
              rec(i + 1, j - s[i][1]) + s[i][0])#深さ優先探索
        dp[i][j] = res
    return dp[i][j]


print(rec(0, W))"""