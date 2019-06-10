from collections import defaultdict
from heapq import heappop, heappush
import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, copy, functools, random
from collections import deque
from heapq import heappush, heappop
sys.setrecursionlimit(10 ** 7)
ans = 0
tmp = 0
inf = 10 ** 20
INF = float("INF")
eps = 1.0 / 10 ** 10
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def wi(): return list(map(int, sys.stdin.readline().split()))
def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]#WideIntPoint
def ws(): return sys.stdin.readline().split()
def i(): return int(sys.stdin.readline())
def s(): return input()
def vi(n): return [i() for _ in range(n)]
def vs(n): return [s() for _ in range(n)]#VerticalString
def mi(n): return [wi() for _ in range(n)]#MatrixInt
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]

n, m, t = wi()
a = wi()
z = mi(m)

dist = []
for i in range(m):
    dist.append([z[i][0], z[i][1], z[i][2]])

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
# (src, dst, weight)
inputs = dist

g1 = Graph()
g_1 = Graph()
for src, dst, weight in inputs:
    g1.add_edge(src, dst, weight)
    g_1.add_edge(dst, src, weight)

spdi1 = {}
spdi_1 = {}
#d = defaultdict(int)
d1 = Dijkstra(g1, 1)
d_1 = Dijkstra(g_1, 1)
for i in range(1, n + 1):
    sp1 = format(d1.shortest_distance(i))
    spdi1[i] = float(sp1)
    sp_1 = format(d_1.shortest_distance(i))
    spdi_1[i] = float(sp_1)
#print('最短経路: {}'.format(d.shortest_path(1)))
#print('最短距離: {}'.format(d.shortest_distance(1)))


for i in range(n):
    ans = max(ans, (t - (spdi1[i + 1] + spdi_1[i + 1])) * a[i])

print(int(ans))