import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
import sys
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter as ig
import matplotlib.pyplot as plt
import random
import numpy as np
import math
import sys
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
    w, h = wi()
    p = hi(w - 1)
    q = hi(h - 1)

    towns = []
    for i in range(n):
        x, y = map(int, input().split())
        towns.append((i, x, y))

    # x, y座標の値でソートして、隣接する街の間の道を、隣接リストadjに追加する
    adj = [[] for i in range(N)]
    for xy in [1, 2]:
        towns.sort(key=lambda t: t[xy])
        for i in range(N - 1):
            t1 = towns[i][0]
            t2 = towns[i + 1][0]
            cost = min(abs(towns[i + 1][1] - towns[i][1]),
                       abs(towns[i + 1][2] - towns[i][2]))  # towns[i + 1][xy] - towns[i][xy]
            adj[t1].append((t2, cost))
            adj[t2].append((t1, cost))

    # 最小全域木を求める（プリム法）
    import heapq

    pq = []
    heapq.heappush(pq, (0, 0))

    done = set()
    ans = 0
    while pq:
        cost, v_now = heapq.heappop(pq)

        if v_now in done:
            continue

        ans += cost
        done.add(v_now)

        if len(done) == N:
            break

        for v, c in adj[v_now]:
            if v not in done:
                heapq.heappush(pq, (c, v))

    print(ans)
