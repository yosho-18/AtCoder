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

s = s()
n = i()
lr = mi(n)

for i in range(n):
    if lr[i][1] == len(s) and lr[i][0] == 1:
        t = s[:: -1]
    elif lr[i][1] == len(s):
        t = s[:lr[i][0] - 1] + s[lr[i][1] - 1: lr[i][0] - 2: -1]
    elif lr[i][0] == 1:
        t = s[lr[i][1] - 1:: -1] + s[lr[i][1]:]
    else:
        t = s[:lr[i][0] - 1] + s[lr[i][1] - 1: lr[i][0] - 2: -1] + s[lr[i][1]:]
    s = t

print(s)