import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
import sys
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter as ig
sys.setrecursionlimit(10 ** 7)
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

n, m = wi()
uv = mi(m)
uv_set = set()
for point in uv:
    uv_set.add((point[0], point[1]))
    uv_set.add((point[1], point[0]))
class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納。par[x] == xの時そのノードは根
        self.par = [-1 for i in range(n+1)]
        # 木の高さを格納する（初期状態では0）
        """self.rank = [0] * (n + 1)"""


    # 検索
    # 根ならその番号を返す
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            # 走査していく過程で親を書き換える
            self.par[x] = self.find(self.par[x])
            return self.par[x]

        # 併合
    def union(self, x, y):
        # 根を探す
        x = self.find(x)
        y = self.find(y)
        # 木の高さを比較し、低いほうから高いほうに辺を張る
        if x != y:
            if self.par[x] < self.par[y]:#par<0の小さい方に合わせる
                self.par[y] += self.par[x]
                self.par[x] = y
            else:
                self.par[x] += self.par[y]
                self.par[y] = x
            # 木の高さが同じなら片方を1増やす
                """if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1"""

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]

u = UnionFind(n)
for point in uv:
    u.union(point[0], point[1])

still_set = set()
group_list = []
for p in range(1, n + 1):
    if p not in still_set:
        still_set.add(p)
        group_list.append([])
        group_list[-1].append(p)
        for p2 in range(p + 1, n + 1):
            if u.same_check(p, p2):
                still_set.add(p2)
                group_list[-1].append(p2)

for part in group_list:
    edge = 0
    for p_p2 in combinations(part, 2):
        if p_p2 in uv_set:
            edge += 1
    if edge == len(part) - 1:
        ans += 1
print(ans)