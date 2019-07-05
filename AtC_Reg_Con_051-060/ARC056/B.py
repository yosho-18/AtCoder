import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
import sys
from collections import deque, defaultdict, Counter;
from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter as ig

sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20;
INF = float("INF");
ans = 0;
tmp = 0;
ansli = [];
tmpli = [];
candili = []
eps = 1.0 / 10 ** 10;
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)];
ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)];
ddn9 = ddn + [(0, 0)]
"""for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:"""


def wi(): return list(map(int, sys.stdin.readline().split()))


def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]  # WideIntPoint


def ws(): return sys.stdin.readline().split()


def i(): return int(sys.stdin.readline())


def s(): return input()


def hi(n): return [i() for _ in range(n)]


def hs(n): return [s() for _ in range(n)]  # HeightString


def mi(n): return [wi() for _ in range(n)]  # MatrixInt


def mip(n): return [wip() for _ in range(n)]


def ms(n): return [ws() for _ in range(n)]


n, m, s = wi()
vu = mip(m)
s = s - 1

class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納。par[x] == xの時そのノードは根
        self.par = [-1 for i in range(n + 1)]
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
            if self.par[x] < self.par[y]:  # par<0の小さい方に合わせる
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

for i in range(m):
    vu[i].sort()
vu.sort(reverse=True)
start = 0
for i in range(m):
    if vu[i][0] == s:
        u.union(vu[i][0], vu[i][1])
    elif vu[i][0] < s:
        start = i
        break
connect = start
for i in range(s, -1, -1):
    if u.same_check(s, i):
        ansli.append(i)
    if i == 0:
        break
    while True:
        connect = start
        if connect == m:
            break
        elif vu[connect][0] == i - 1:
            u.union(vu[connect][0], vu[connect][1])
            start += 1
        else:
            break
for i in range(len(ansli)):
    print(ansli[-i - 1] + 1)

