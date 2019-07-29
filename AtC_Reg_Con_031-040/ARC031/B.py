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
def s(): return list(input())
def hi(n): return [i() for _ in range(n)]
def hs(n): return [s() for _ in range(n)]#HeightString
def mi(n): return [wi() for _ in range(n)]#MatrixInt
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]

a = hs(10)

def bfs(circlepoint):
    flag = [[0 for _ in range(10)] for _ in range(10)]
    queue = deque()
    queue.append(circlepoint)
    while queue != deque():
        cri_i, cri_j = queue.popleft()
        for dx, dy in dd:
            nx = cri_j + dx
            ny = cri_i + dy
            if 0 <= nx < 10 and 0 <= ny < 10:
                if a[ny][nx] == "o" and flag[ny][nx] == 0:
                    queue.append((ny, nx))
                    flag[ny][nx] = 1
    for i in range(10):
        for j in range(10):
            if a[i][j] == "o" and flag[i][j] == 0:
                return False
    else:
        return True


for i in range(10):
    for j in range(10):
        circlepoint = (i, j)
        if a[i][j] == "x":
            a[i][j] = "o"
            if bfs(circlepoint):
                print("YES")
                exit()
            else:
                a[i][j] = "x"
print("NO")