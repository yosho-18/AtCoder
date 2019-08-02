import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, copy, functools, random
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
from bisect import bisect_left, bisect_right, insort_left, insort_right; sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20; INF = float("INF"); ans = 0; tmp = INF; ansli = []; tmpli = []; candili = []
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


n, x = wi()
h = wi()
ab = mip(n - 1)
x -= 1

g2 = [[INF for j in range(n)] for i in range(n)]
for i in range(n - 1):
    g2[ab[i][0]][ab[i][1]] = 1
    g2[ab[i][1]][ab[i][0]] = 1

cost = floyd_warshall(csr_matrix(g2))#単方向無理

treasurelist = []
for i in range(n):
    if h[i] > 0:
        treasurelist.append(i)

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

if len(treasurelist) > 1:
    for start, goal in combinations(treasurelist, 2):
        ans += cost[start][goal]

    ans = ans // (len(treasurelist) - 1) * 2

for goal in treasurelist:
    tmp = min(tmp, cost[x][goal])

ans += tmp * 2
print(int(ans))