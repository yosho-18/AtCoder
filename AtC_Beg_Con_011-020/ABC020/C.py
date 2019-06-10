import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, copy, functools, random
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
from bisect import bisect_left, bisect_right, insort_left, insort_right; sys.setrecursionlimit(10 ** 7)

inf = 10 ** 20; INF = float("INF"); ans = 0; tmp = 0; ansli = []; tmpli = []; candili = []
eps = 1.0 / 10 ** 10; mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]; ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)]; ddn9 = ddn + [(0, 0)]
"""for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:"""
def wi(): return list(map(int, sys.stdin.readline().split()))
def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]#WideIntPoint
def ws(): return sys.stdin.readline().split()
def i(): return int(sys.stdin.readline())
def s(): return input()
def hi(n): return [i() for _ in range(n)]
def hs(n): return [s() for _ in range(n)]#HeightString
def mi(n): return [wi() for _ in range(n)]#MatrixInt
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]


h, w, t = wi()
s = hs(h)
start = 0
goal = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == "S":
            start = i * w + j
        if s[i][j] == "G":
            goal = i * w + j

n = h * w
def isOK(x):
    g2 = [[INF for j in range(n + 1)] for i in range(n + 1)]

    for i in range(h):
        for j in range(w):
            for dx, dy in dd:
                nx = j + dx;
                ny = i + dy
                if 0 <= nx < w and 0 <= ny < h:
                    if s[i][j] == "." or s[i][j] == "S" or s[i][j] == "G":
                        if s[ny][nx] == "." or s[ny][nx] == "S" or s[ny][nx] == "G":
                            g2[i * w + j][ny * w + nx] = 1
                            g2[ny * w + nx][i * w + j] = 1
                        else:
                            g2[i * w + j][ny * w + nx] = x
                            g2[ny * w + nx][i * w + j] = 1
                    else:
                        if s[ny][nx] == "." or s[ny][nx] == "S" or s[ny][nx] == "G":
                            g2[i * w + j][ny * w + nx] = 1
                            g2[ny * w + nx][i * w + j] = x
                        else:
                            g2[i * w + j][ny * w + nx] = x
                            g2[ny * w + nx][i * w + j] = x


    cost = floyd_warshall(csr_matrix(g2))

    if cost[start][goal] < t:
        return 0
    elif cost[start][goal] > t:
        return 1
    else:
        return 2


def isOK2(x):
    class Graph(object):
        """
        隣接リストによる有向グラフ
        """

        def __init__(self):
            self.graph = defaultdict(list)

        def __len__(self):
            return len(self.graph)

        def add_edge(self, src, dst, weight=1):
            self.graph[src].append((dst, weight))

        def get_nodes(self):
            return self.graph.keys()

    class Dijkstra(object):
        """
        ダイクストラ法（二分ヒープ）による最短経路探索
        計算量: O((E+V)logV)
        """

        def __init__(self, graph, start):
            self.g = graph.graph

            # startノードからの最短距離
            # startノードは0, それ以外は無限大で初期化
            self.dist = defaultdict(lambda: float('inf'))
            self.dist[start] = 0

            # 最短経路での1つ前のノード
            self.prev = defaultdict(lambda: None)

            # startノードをキューに入れる
            self.Q = []
            heappush(self.Q, (self.dist[start], start))

            while self.Q:
                # 優先度（距離）が最小であるキューを取り出す
                dist_u, u = heappop(self.Q)
                if self.dist[u] < dist_u:
                    continue
                for v, weight in self.g[u]:
                    alt = dist_u + weight
                    if self.dist[v] > alt:
                        self.dist[v] = alt
                        self.prev[v] = u
                        heappush(self.Q, (alt, v))

        def shortest_distance(self, goal):
            """
            startノードからgoalノードまでの最短距離
            """
            return self.dist[goal]

        def shortest_path(self, goal):
            """
            startノードからgoalノードまでの最短経路
            """
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = self.prev[node]
            return path[::-1]

    dist = []
    for i in range(h):
        for j in range(w):
            for dx, dy in dd:
                nx = j + dx;
                ny = i + dy
                if 0 <= nx < w and 0 <= ny < h:
                    if s[i][j] == "." or s[i][j] == "S" or s[i][j] == "G":
                        if s[ny][nx] == "." or s[ny][nx] == "S" or s[ny][nx] == "G":
                            dist.append((i * w + j, ny * w + nx, 1))
                            dist.append((ny * w + nx, i * w + j, 1))
                        else:
                            dist.append((i * w + j, ny * w + nx, x))
                            dist.append((ny * w + nx, i * w + j, 1))
                    else:
                        if s[ny][nx] == "." or s[ny][nx] == "S" or s[ny][nx] == "G":
                            dist.append((i * w + j, ny * w + nx, 1))
                            dist.append((ny * w + nx, i * w + j, x))
                        else:
                            dist.append((i * w + j, ny * w + nx, x))
                            dist.append((ny * w + nx, i * w + j, x))

    inputs = list(set(dist))

    g = Graph()
    for src, dst, weight in inputs:
        g.add_edge(src, dst, weight)
        # g.add_edge(dst, src, weight)

    d = Dijkstra(g, start)
    shortest_s_g = d.shortest_distance(goal)
    if shortest_s_g < t:
        return 0
    elif shortest_s_g > t:
        return 1
    else:
        return 2


#汎用的な二分探索のテンプレ
def binary_search():
    ng = -1 #「index = 0」が条件を満たすこともあるので、初期値は -1
    ok = 10 ** 9 #「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()

    #ok と ng のどちらが大きいかわからないことを考慮
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        wd = isOK2(mid)
        if wd == 0:
            ng = mid
        elif wd == 1:
            ok = mid
        else:
            return mid
    return ng






print(binary_search())