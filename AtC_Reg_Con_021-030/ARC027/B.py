import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, copy, functools, random
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right; sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20; INF = float("INF"); ans = 1; tmp = 0; ansli = []; tmpli = []; candili = []
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

n = i()
s1 = s()
s2 = s()

class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納。par[x] == xの時そのノードは根
        self.par = [-1 for i in range(n+1)]
        # 木の高さを格納する（初期状態では0）
        """self.rank = [0] * (n + 1)"""


    # 検索
    # 根ならその番号を返す
    def parent(self, x):
        if self.par[x] < 0:
            return x
        else:
            # 走査していく過程で親を書き換える
            self.par[x] = self.parent(self.par[x])
            return self.par[x]

        # 併合
    def union(self, x, y):
        # 根を探す
        x = self.parent(x)
        y = self.parent(y)
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
        return self.parent(x) == self.parent(y)

    def size(self, x):
        return -self.par[self.parent(x)]

u = UnionFind(25)

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_dict = {}
al_num = {} #alphabetからnumberへ
num_al = {} #numberからalphabetへ
for cnt, i in enumerate(alpha):
    alpha_dict[i] = -1
    al_num[i] = cnt
    num_al[cnt] = i

son_dict = {}
for i in range(26):
    son_dict[i] = set()
numset = set()
for i in range(10):
    numset.add(str(i))

#数字を持っているか
for i in range(n):
    if s1[i] in numset and s2[i] not in numset:
        alpha_dict[s2[i]] = s1[i]
    elif s1[i] not in numset and s2[i] in numset:
        alpha_dict[s1[i]] = s2[i]
    elif s1[i] in numset and s2[i] in numset:
        pass
    else:
        u.union(al_num[s1[i]], al_num[s2[i]])

#ひとつ数字を持っているアルファベットがあれば全員に共有
for i in alpha:
    p = u.parent(al_num[i])
    son_dict[p].add(al_num[i])#number

for i in alpha:
    if alpha_dict[i] != -1:
        for val in son_dict[u.parent(al_num[i])]:
            alpha_dict[num_al[val]] = alpha_dict[i]

still_alpha = set() #既に出てきたアルファベットの集合
for i in range(n):
    if s1[i] not in numset:
        if alpha_dict[s1[i]] == -1 and s1[i] not in still_alpha:
            if i == 0:
                ans *= 9
            else:
                ans *= 10

            for val in son_dict[u.parent(al_num[s1[i]])]:
                still_alpha.add(num_al[val])#alphabet
print(ans)
"""
7
498XY7TZ
4ABC87C2
"""
"""
10
"""