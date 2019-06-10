def warshall_floyd(n,w,d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################
n,w = map(int,input().split()) #n:頂点数　w:辺の数

d = [[float("inf") for i in range(n + 1)] for i in range(n + 1)]
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(w):
    x,y,z = map(int,input().split())
    d[x][y] = z
    d[y][x] = z
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
print(warshall_floyd(n,w,d))



from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

c1 = []
g2 = [[INF for j in range(n + 1)] for i in range(n + 1)]
for i in range(m):
    if c[i][0] != 1 and c[i][1] != 1:
        cnot1.append([c[i][0], c[i][1], c[i][2]])
        g2[c[i][0]][c[i][1]] = c[i][2]
        g2[c[i][1]][c[i][0]] = c[i][2]
    else:
        c1.append([c[i][0], c[i][1], c[i][2]])


cost = floyd_warshall(csr_matrix(g2))#単方向無理