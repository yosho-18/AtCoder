from collections import defaultdict
n, ma, mb = map(int, input().split())
d = []
for i in range(n):#h:高さ
    d.append([int(m) for m in input().split()])

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

#dptable,dp[n][a][b][c](a = dp[n][0])
"""dp = []
for i in range(401):
    for j in range(401):
        dp.append([i,j])"""

cost = []
for i in range(401):
    cost.append([])
for i in range(401):
    for j in range(401):
        cost[i].append([])
for i in range(401):
    for j in range(401):
        cost[i][j] = float("INF")
cost[0][0] = 0
pos = []
pos.append([0,0])
pos2 = set()
pos2.add((0,0))
#cppos = []
#cppos.append([0,0])
cppos2 = set()
cppos2.add((0,0))

cpcost = {}
cpcost = defaultdict(lambda: float("INF"))
for i in range(n):
    for v in range(2):
        for w in range(len(pos)):
            p = pos[w][0] + v * d[i][0]
            q = pos[w][1] + v * d[i][1]
            if (p, q) not in pos2:
                #cppos.append([p, q])
                cppos2.add((p, q))
            if cost[p][q] > cost[pos[w][0]][pos[w][1]] + d[i][2]:
                if cpcost[p, q] > cost[pos[w][0]][pos[w][1]] + d[i][2]:
                    cpcost[p, q] = cost[pos[w][0]][pos[w][1]] + d[i][2]
    #pos += cppos
    for u in cppos2:
        pos2.add(u)
        pos.append(list(u))
    for u in cpcost:
        cost[u[0]][u[1]] = cpcost[u]
    cppos = []
    cppos2 = set()
    cpcost = {}
    cpcost = defaultdict(lambda: float("INF"))

realcost = []
for i in range(401):
    for j in range(401):
        if gcd(i, j) != 0:
            if i // gcd(i, j) == ma and j // gcd(i, j) == mb and cost[i][j] != float("INF"):
                realcost.append(cost[i][j])

if len(realcost) > 0:
    print(min(realcost))
else:
    print(-1)
