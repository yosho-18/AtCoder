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

N, Q = wi()
stx = mi(N)
D = hi(Q)
kukann = [[0, 0, 0] for _ in range(N)]
for i in range(N):
    kukann[i][1] = stx[i][0] - stx[i][2]
    kukann[i][2] = stx[i][1] - stx[i][2]
    kukann[i][0] = stx[i][2]


kukann.sort()

ans = [-1] * Q
skip = [-1] * Q
for pos, start, end in kukann:#kukannから考える，時間計算量が最悪２乗
    left = bisect_left(D, start)
    right = bisect_left(D, end)

    while left < right:
        if skip[left] == -1:
            ans[left] = pos
            skip[left] = right
            left += 1
        else:
            left = skip[left]

print(*ans, sep='\n')

"""
4 6
1 2 1
2 4 2
3 6 3
4 8 4
0
1
2
3
4
5
"""