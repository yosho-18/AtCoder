n, m = map(int, input().split())
#行列
s = []
for i in range(m):#h:高さ
    s.append([int(w) for w in input().split()])
s.sort(key=lambda x:(x[0], x[1]))
adj = []
for i in range(n):
    adj.append([])
for i in range(n):
    for j in range(n):
        adj[i].append(0)
#鱗屑行列
for i in range(m):
    adj[s[i][0] - 1][s[i][1] - 1] = 1
    adj[s[i][1] - 1][s[i][0] - 1] = 1

#深さ優先探索
labelli = [-1]*n
label = 0
v = 0
labelli[0] = label
p = 0
back = []
backnumber = []
q = 0
count = 0
for h in range(m):
    if h == 0:
        adj[s[h][0] - 1][s[h][1] - 1] = 0
        adj[s[h][1] - 1][s[h][0] - 1] = 0
    else:
        adj[s[h - 1][0] - 1][s[h - 1][1] - 1] = 1
        adj[s[h - 1][1] - 1][s[h - 1][0] - 1] = 1
        adj[s[h][0] - 1][s[h][1] - 1] = 0
        adj[s[h][1] - 1][s[h][0] - 1] = 0
        q = 0
        labelli = [-1] * n
        label = 0
        labelli[0] = label
    while q == 0:
        for j in range(n):
            if adj[v][j] == 1 and labelli[j] == -1:#未探索部分を掘る
                label += 1
                v = j
                labelli[j] = label
                p = 1
                break
        if v == 0:#深さ優先探索は最終的にv==0に戻ってくる
            for l in range(n):
                if adj[v][j] == 1 and labelli[j] == -1:#初期地点で、未探索部分があるかチェック、なければ終了
                    break
                if l == n - 1:
                    q = 1
                    p = 1
                    if min(labelli) == -1:#未探索部分があることの証
                        count += 1
        if p == 0:#未探索がなければ戻る
            for k in range(n):
                if adj[v][k] == 1:
                    if labelli[v] > labelli[k]:
                        back.append(abs(labelli[v] - labelli[k]))
                        backnumber.append(k)
            v = backnumber[back.index(min(back))]
            back = []
            backnumber = []
        p = 0

print(count)