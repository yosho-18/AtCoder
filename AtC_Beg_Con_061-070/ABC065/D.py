import array
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
    n = int(input())
    z = []
    for i in range(n):  # h:高さ
        z.append([int(m) for m in input().split()] + [i])

    zx = sorted(z, key=lambda x: (x[0]))
    zy = sorted(z, key=lambda x: (x[1]))

    # 最小木問題をプリム法で解く

    # 点群を発生
    p = [[zx[i][2], zx[i + 1][2], min(abs(zx[i][0] - zx[i + 1][0]), abs(zx[i][1] - zx[i + 1][1]))] for i in range(n - 1)]
    p += [[zy[i][2], zy[i + 1][2], min(abs(zy[i][0] - zy[i + 1][0]), abs(zy[i][1] - zy[i + 1][1]))] for i in range(n - 1)]

    max_v, max_e = n, len(p)
    adjacency_list = collections.defaultdict(set)
    for i in range(max_e):
        s, t, w = p[i][0], p[i][1], p[i][2]
        adjacency_list[s].add(AdjacentVertex(t, w))
        adjacency_list[t].add(AdjacentVertex(s, w))
    (_, key) = compute_mst_prim(max_v, adjacency_list)
    print(sum(key.values()))


if __name__ == '__main__':
    main()