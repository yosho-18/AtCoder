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

n, m, k = wi()

tmp = 0
for j in range(m):
    if j <= (m - 1) // 2:
        tmp += (j * (j + 1) + ((m - 1 - j) * (m - 1 - j + 1)) // 2) * n ** 2
        tmp = tmp % mod
        ans += (j * (j + 1) + ((m - 1 - j) * (m - 1 - j + 1)) // 2) * n ** 2
    elif j == (m - 1) // 2:
        ans += (j * (j + 1)) * n ** 2
    else:
        ans += tmp
        if m % 2 != 0:
            ans -= (((m - 1) // 2) * (((m - 1) // 2) + 1)) * n ** 2
        break
    ans = ans % mod
ans = ans % mod

tmp = 0
for i in range(n):
    if i <= (n - 1) // 2:
        tmp += (i * (i + 1) + ((n - 1 - i) * (n - 1 - i + 1)) // 2) * m ** 2
        tmp = tmp % mod
        ans += (i * (i + 1) + ((n - 1 - i) * (n - 1 - i + 1)) // 2) * m ** 2
    elif i == (n - 1) // 2:
        ans += (i * (i + 1)) * m ** 2
    else:
        ans += tmp
        if n % 2 != 0:
            ans -= (((n - 1) // 2) * (((n - 1) // 2) + 1)) * m ** 2
        break
        break
    ans = ans % mod
ans = ans % mod
ans = ans // 2

MAX_N = 3 * 10 ** 5 + 100
factorial = [1] * MAX_N
#事前に階上テーブルを用意
def calc_factorial():
    for i in range(1, MAX_N):
        factorial[i] = i * factorial[i - 1] % mod

def comb(n, k):
    a = factorial[n] % mod
    b = (factorial[k] * factorial[n - k]) % mod
    b_ = pow(b, mod - 2, mod)
    return (a * b_) % mod


# 階乗を用意
calc_factorial()

ans *= comb(n * m, k - 2)
print(ans % mod)

