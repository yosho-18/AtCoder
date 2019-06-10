n, m = map(int, input().split())
d = []
for i in range(m):#h:高さ
    d.append([int(m) for m in input().split()])
e = []
for i in range(m):
    e.append([])
for i in range(m):
    e[i].append(d[i][0] - 1)
    e[i].append(d[i][1] - 1)
    e[i].append(-d[i][2])
#edges = d
#num_v = n
#source = m


#ベルマンフォード
#高々|V|-1回で最安定経路にたどり着くっていうのがなかなか理解できなくて、紙に書きながら理解した。

"""edge = [[0,1,2],[0,2,5],[1,2,4],[1,3,6],[1,4,10],[2,3,2],[3,5,1],[4,5,3],[4,6,5],[5,6,9],
       [1,0,2],[2,0,5],[2,1,4],[3,1,6],[4,1,10],[3,2,2],[5,3,1],[5,4,3],[6,4,5],[6,5,9]]"""
edge = e

def shortest_path(edge,num_v,start):
    inf = float("inf")
    d = [inf for f in range(num_v)]
    d[start] = 0;
    for i in range(num_v):
        update = False
        for e in edge:
            if d[e[0]] != inf and d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                update = True
        if not update:
            break
        if i == num_v - 2:
            k = d[-1]
        if i == num_v - 1 and k != d[-1]:
            d[n - 1] = -inf
            break
    return d

print(-shortest_path(edge,n,0)[n - 1])
#print("inf")
#print(BellmanFord(e, n, m))
"""5 5
1 2 2
2 5 4
4 3 1
3 4 2
2 4 1"""

