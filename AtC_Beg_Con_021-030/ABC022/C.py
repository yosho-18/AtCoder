import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, copy, functools, random
from collections import deque
from heapq import heappush, heappop
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
INF = float("INF")
ans = INF
tmp = 0
eps = 1.0 / 10 ** 10
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def wi(): return list(map(int, sys.stdin.readline().split()))
def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def wf(): return [float(x) for x in sys.stdin.readline().split()]
def ws(): return sys.stdin.readline().split()
def i(): return int(sys.stdin.readline())
def f(): return float(sys.stdin.readline())
def s(): return input()
def vi(n): return [i() for _ in range(n)]
def vs(n): return [s() for _ in range(n)]
def mi(n): return [wi() for _ in range(n)]
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]
def pf(s): return print(s, flush=True)

n, m = wi()
c = mi(m)
cnot1 = []
c1 = []
g2 = [[INF for j in range(n + 1)] for i in range(n + 1)]
for i in range(m):
    if c[i][0] != 1 and c[i][1] != 1:
        cnot1.append([c[i][0], c[i][1], c[i][2]])
        g2[c[i][0]][c[i][1]] = c[i][2]
        g2[c[i][1]][c[i][0]] = c[i][2]
    else:
        c1.append([c[i][0], c[i][1], c[i][2]])


cost = floyd_warshall(csr_matrix(g2))

for balls in itertools.combinations(c1, 2):
    tmp = balls[0][2] + balls[1][2]
    tmp += cost[balls[0][1]][balls[1][1]]
    ans = min(ans, tmp)

if ans == INF:
    ans = -1

print(int(ans))