import numpy as np
n = int(input())
"""a = []
for i in range(n):#h:高さ
    a.append([int(m) for m in input().split()])"""
a = [np.array(input().split(), dtype=np.int64) for _ in [0]*n]
"""d = [[float("inf") for i in range(n + 1)] for i in range(n + 1)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(n):
    for j in range(n):
        d[x][y] = z
        d[y][x] = z"""


def warshall_floyd(n,d):
    e = [[0 for i in range(n)] for i in range(n)]
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    print(-1)
                    exit()
                elif d[i][j] == d[i][k] + d[k][j] and i != j and i != k and j != k:
                    e[i][j] = float("INF")
    return (d, e)

##############################
b = warshall_floyd(n,a)[0]
c = warshall_floyd(n,a)[1]
ans = 0
for i in range(n):
    for j in range(n):
        if c[i][j] != float("INF"):
            ans += b[i][j]
ans = ans // 2
print(ans)