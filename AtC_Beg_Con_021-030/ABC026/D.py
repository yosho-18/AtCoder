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
def hi(n): return [i() for _ in range(n)]
def hs(n): return [s() for _ in range(n)]#HeightString
def mi(n): return [wi() for _ in range(n)]#MatrixInt
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]

a, b, c = wi()

#単調性のある関数の解を見つける

def isOK(mid):
    if ((- a * mid + 100) - (b * math.sin(c * math.pi * mid))) > 0:
        return False
    elif ((- a * mid + 100) - (b * math.sin(c * math.pi * mid))) < 0:
        return True
    """else:
        return True"""


#汎用的な二分探索のテンプレ
def binary_search(ng, ok):
    #ng = -1 #「index = 0」が条件を満たすこともあるので、初期値は -1
    #ok = 10 ** 15 #「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()
    cnt = 0
    #ok と ng のどちらが大きいかわからないことを考慮
    while cnt < 10 ** 5:#abs(ok - ng) > 10 ** (-1):
        mid = (ok + ng) / 2

        if isOK(mid):
            ok = mid
        else:
            ng = mid
        cnt += 1
    return ok

def frange(begin, end, step):
    n = begin
    while n+step < end:
     yield n
     n += step

ng = 0
ok = 0
for x in frange(1/(2 * c), 200/a, 1/(2 * c)):
    if ((- a * (x - 1/(2 * c)) + 100) - (b * math.sin(c * math.pi * (x - 1/(2 * c))))) * \
            ((- a * x + 100) - (b * math.sin(c * math.pi * x))) <= 0:
        ng = x - 1/(2 * c) - 10 ** (-10)
        ok = x + 10 ** (-10)
        break
#正×負か，負×正で考えた方がいいかも
print(binary_search(ng, ok))
