"""def BellmanFord(edges, num_v, source):
    # グラフの初期化
    inf = float("inf")
    dist = [inf for i in range(num_v)]
    dist[source - 1] = 0

    # 辺の緩和
    for i in range(num_v):
        for edge in edges:
            if edge[0] != inf and dist[edge[1] - 1] > dist[edge[0] - 1] + edge[2]:
                dist[edge[1] - 1] = dist[edge[0] - 1] + edge[2]
                if i == num_v - 1:
                    return -1

    return dist"""
edge = [[0,1,2],[0,2,5],[1,2,4],[1,3,6],[1,4,10],[2,3,2],[3,5,1],[4,5,3],[4,6,5],[5,6,9],
       [1,0,2],[2,0,5],[2,1,4],[3,1,6],[4,1,10],[3,2,2],[5,3,1],[5,4,3],[6,4,5],[6,5,9]]

def shortest_path(edge,num_v,start):
    inf = float("inf")
    d = [inf for f in range(num_v)]
    d[start] = 0;
    while True:
        update = False
        for e in edge:
            if d[e[0]] != inf and d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                update = True
        if not update:
            break
    return d

print(shortest_path(edge,7,0)[6])

def Bell_shortest_path(edge, num_v, start):
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

print(-Bell_shortest_path(edge, n, 0)[n - 1])
#print("inf")
#print(BellmanFord(e, n, m))