import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
import sys
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter as ig
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20; INF = float("INF"); ans = 0; tmp = 0; cnt = 0; ansli = []; tmpli = []; candili = []; stillset = set()
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
def num_grid(n): return [[int(i) for i in sys.stdin.readline().split()[0]] for _ in range(n)]#NumberGrid
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]
def grid(n): return [s_list() for _ in range(n)]


if __name__ == '__main__':
    n, q = wi()
    A = wi()
    X = hi(q)

    accu_a = list(accumulate(A))
    # from_zero_sum = [i for idx, i in enumerate(a) if idx % 2 == 0]
    # from_one_sum = [i for idx, i in enumerate(a) if idx % 2 == 1]


    # 単調性のある関数の解を見つける

    def isOK(mid):
        turn = n - 1 - mid
        d = mid + 1
        c = mid
        b = c - turn + 2
        a = b - 1
        if b < 0:
            return "f", "t"

        if abs(A[a] - x) < abs(A[c] - x) and a >= 0:
            a -= 1
            if abs(A[a] - x) < abs(A[c] - x) and a >= 0:
                return "t", "t"
            return "d", "t"
        elif abs(A[b] - x) > abs(A[d] - x):
            return "f", "a"
        else:
            return "d", "t"

    # 汎用的な二分探索のテンプレ
    # 条件を満たす最小値（ng,ok）
    def binary_search():
        ng = -1  # 「index = 0」が条件を満たすこともあるので、初期値は -1
        ok = len(A)  # 「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()

        # ok と ng のどちらが大きいかわからないことを考慮
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2

            B = isOK(mid)

            if B[0] == "t":
                ok, t_or_a = mid, B[1]
            elif B[0] == "f":
                ng, t_or_a = mid, B[1]
            else:
                ok, t_or_a = mid, B[1]
                return ok, t_or_a
        return ok, t_or_a

    for _, x in enumerate(X):
        # r_b = bisect_right(A, x)
        ok, t_or_a = binary_search()
        ans += accu_a[-1] - accu_a[ok]
        turn = n - 1 - ok
        b = ok - turn + 2

        if t_or_a == "t":
            b -= 2
        for i in range(b, -1, -2):
            ans += A[i]
        print(ans)
        ans = 0
