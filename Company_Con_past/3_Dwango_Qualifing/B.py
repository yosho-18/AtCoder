import sys
# import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
# from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
# from itertools import permutations, combinations, product, accumulate, groupby
# from bisect import bisect_left, bisect_right, insort_left, insort_right
# from operator import itemgetter as ig
sys.setrecursionlimit(10 ** 7)
# inf = 10 ** 20; INF = float("INF"); ans = 0; tmp = 0; ansli = []; tmpli = []; candili = []; mod = 10 ** 9 + 7
# dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]; ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)]; ddn9 = ddn + [(0, 0)]
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

t = s()
n = len(t)
dp = [[[0, 0], [0, 0]] for i in range(n)]#2,5
for i in range(1, n):
    if t[i] == "?":
        dp[i][0][0] = max(dp[i - 1][0][0], dp[i - 1][1][0])
        tmp = dp[i - 1][0][0]
        tmp2 = dp[i - 1][1][0]
        if t[i - 1] == "?" or t[i - 1] == "2":
            tmp += 1
        dp[i][1][0] = max(tmp, tmp2)
    else:
        if t[i] == "2":
            dp[i][0][0] = max(dp[i - 1][0][0], dp[i - 1][1][0])
            dp[i][1][0] = dp[i - 1][1][0]
        elif t[i] == "5":
            dp[i][0][0] = dp[i - 1][0][0]
            tmp = dp[i - 1][0][0]
            tmp2 = dp[i - 1][1][0]
            if t[i - 1] == "?" or t[i - 1] == "2":
                tmp += 1
            dp[i][1][0] = max(tmp, tmp2)
        else:
            dp[i][0][0] = dp[i - 1][0][0]
            dp[i][1][0] = dp[i - 1][1][0]

print(max(dp[n - 1][0][0], dp[n - 1][1][0]) * 2)