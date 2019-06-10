N = int(input())

towns = []
for i in range(N):
    x, y = map(int, input().split())
    towns.append((i, x, y))

# x, y座標の値でソートして、隣接する街の間の道を、隣接リストadjに追加する
adj = [[] for i in range(N)]
for xy in [1, 2]:
    towns.sort(key=lambda t: t[xy])
    for i in range(N - 1):
        t1 = towns[i][0]
        t2 = towns[i + 1][0]
        cost = min(abs(towns[i + 1][1] - towns[i][1]), abs(towns[i + 1][2] - towns[i][2]))#towns[i + 1][xy] - towns[i][xy]
        adj[t1].append((t2, cost))
        adj[t2].append((t1, cost))

# 最小全域木を求める（プリム法）
import heapq
pq = []
heapq.heappush(pq, (0, 0))

done = set()
ans = 0
while pq:
    cost, v_now = heapq.heappop(pq)

    if v_now in done:
        continue

    ans += cost
    done.add(v_now)

    if len(done) == N:
        break

    for v, c in adj[v_now]:
        if v not in done:
            heapq.heappush(pq, (c, v))

print(ans)

"""import array
import collections
import heapq

AdjacentVertex = collections.namedtuple("AdjacentVertex", "vertex cost")
INF = 2 ** 31 - 1
NO_VERTEX = -1


# Prim法で頂点0からの最小全域木を求める
def compute_mst_prim(max_v, adj_list):
    # pred[u]は頂点uの「ひとつ前」の頂点を表す
    pred = collections.defaultdict(lambda: NO_VERTEX)
    # uとpred[u]を結ぶ辺の重みがkey[u]に入る
    key = collections.defaultdict(lambda: INF)
    key[0] = 0
    # 二分ヒープを優先度付きキューとして用いる
    pq = [(key[v], v) for v in range(max_v)]
    heapq.heapify(pq)
    # 優先度付きキューに頂点が入っているかを示す配列
    in_pq = array.array("B", (True for _ in range(max_v)))
    while pq:
        _, u = heapq.heappop(pq)
        in_pq[u] = False
        for v, v_cost in adj_list[u]:
            if in_pq[v]:
                weight = v_cost
                if weight < key[v]:
                    pred[v] = u
                    key[v] = weight
                    heapq.heappush(pq, (weight, v))
                    in_pq[v] = True
    return (pred, key)


def main():
    max_v, max_e = map(int, input().split())
    adjacency_list = collections.defaultdict(set)
    for _ in range(max_e):
        s, t, w = map(int, input().split())
        adjacency_list[s].add(AdjacentVertex(t, w))
        adjacency_list[t].add(AdjacentVertex(s, w))
    (_, key) = compute_mst_prim(max_v, adjacency_list)
    print(sum(key.values()))


if __name__ == '__main__':
    main()
    """