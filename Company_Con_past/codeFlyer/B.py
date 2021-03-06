import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
import sys
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter as ig
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20; INF = float("INF"); ans = INF; tmp = 0; cnt = 0; ansli = []; tmpli = []; candili = []; stillset = set()
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
def s_list(): return list(input())
def hi(n): return [i() for _ in range(n)]
def hs(n): return [s() for _ in range(n)]#HeightString
def mi(n): return [wi() for _ in range(n)]#MatrixInt
def num__grid(n): return [[int(i) for i in sys.stdin.readline().split()[0]] for _ in range(n)]#NumberGrid
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]
def grid(n): return [s_list() for _ in range(n)]

n, q = wi()
x = wi()
cd = mi(q)

minus_x = [- i for i in x]

accu_x = list(itertools.accumulate(x))
accu_minus_x = list(itertools.accumulate(minus_x))

# c - d < x < c + d abs(x - c)
# bisectはPyPyより，Pythonのほうが速い
for i, (c, d) in enumerate(cd):
    minus = bisect.bisect_right(x, c - d) - 1
    plus = bisect.bisect_left(x, c + d) - 1
    zero = bisect.bisect_right(x, c) - 1
    if plus == -1:
        ans = d * n
    else:
        if minus == -1 and zero == -1:
            ans = accu_x[plus] - c * (plus + 1) \
                  + d * (n - (plus + 1))
        elif minus == -1:
            ans = accu_minus_x[zero] + c * (zero + 1) \
                  + accu_x[plus] - accu_x[zero] - c * (plus - zero) \
                  + d * (n - (plus + 1))
        else:
            ans = accu_minus_x[zero] - accu_minus_x[minus] + c * (zero - minus) \
                  + accu_x[plus] - accu_x[zero] - c * (plus - zero) \
                  + d * (n - (plus - minus))
    print(ans)