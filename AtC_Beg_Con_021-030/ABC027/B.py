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

n = i()
a = wip()

A = sum(a)
q = A // n
tmpn = 0
if A % n != 0:
    print(-1)
else:
    for i in range(n):
        if tmpn == 0:
            tmp += a[i]
            tmpn += 1
        else:
            if tmp / tmpn != q:
                tmp += a[i]
                tmpn += 1
                ans += 1
        if tmp / tmpn == q:
            tmp = 0
            tmpn = 0
    print(ans)