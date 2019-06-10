#横にn個入力
n, m, q = map(int, input().split())
#行列
s = []
for i in range(m):#h:高さ
    s.append([int(m) for m in input().split()] + [i])
# 行列
t = []
for i in range(q):  # h:高さ
    t.append([int(m) for m in input().split()])

LR = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for v in range(m):
     LR[s[v][0]][s[v][1]] += 1

for j in range(1, n + 1):
    for i in range(1, n + 1):#Lについての累積和
        LR[i][j] += LR[i - 1][j]
for i in range(1, n + 1):
    for j in range(1, n + 1):#Rについての累積和，2次元累積和にする
        LR[i][j] += LR[i][j - 1]

for k in range(q):
    tmp = 0
    #for j in range(t[k][0], t[k][1] + 1):#Rについてみていく
        #tmp += LR[t[k][1]][j] - LR[t[k][0] - 1][j]
    tmp += (LR[t[k][1]][t[k][1]] - LR[t[k][1]][t[k][0] - 1]) - (LR[t[k][0] - 1][t[k][1]] - LR[t[k][0] - 1][t[k][0] - 1])

    print(tmp)
"""lin = []
li0 = []
for i in range(n):
    lin.append(set())
    li0.append(set())
for i in range(m):
    lin[s[i][0] - 1].add(s[i][2])
    li0[s[i][1] - 1].add(s[i][2])
for i in range(n - 1):
    li0[i + 1] = li0[i + 1] | li0[i]
for i in range(n - 1, 0, -1):
    lin[i - 1] = lin[i] | lin[i - 1]
for i in range(q):
    ans = len(lin[t[i][0] - 1] & li0[t[i][1] - 1])
    print(ans)"""

"""nnli = []
for i in range(n):
    nnli.append([])
for i in range(n):
    for j in range(n):
        nnli[i].append(0)
for h in range(m):
    for i in range(s[h][0]):
        for j in range(s[h][1] - 1, n):
            nnli[i][j] += 1

for g in range(q):
    print(nnli[t[g][0] - 1][t[g][1] - 1])"""