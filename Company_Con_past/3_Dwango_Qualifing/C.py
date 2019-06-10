import sys
# import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
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

n = i()
a = hi(n)

num = [deque() for _ in range(5)]
for i in range(n):
    num[a[i]].append(i + 1)
stillset = set()
ans = 0
tmp = 0
for i in range(1, n + 1):
    tmp = 0
    if i not in stillset:
        num[a[i - 1]].popleft()
        ans += 1
        if a[i - 1] == 1:
            tmp += 1
            if num[3] != deque():
                p = num[3].pop()
                stillset.add(p)
            else:
                if num[2] != deque():
                    p = num[2].pop()
                    stillset.add(p)
                    tmp += 2
                while tmp < 4:
                    if num[1] != deque():
                        p = num[1].pop()
                        stillset.add(p)
                        tmp += 1
                    else:
                        break
        elif a[i - 1] == 2:
            tmp += 2
            if num[2] != deque():
                p = num[2].pop()
                stillset.add(p)
                tmp += 2
            while tmp < 4:
                if num[1] != deque():
                    p = num[1].pop()
                    stillset.add(p)
                    tmp += 1
                else:
                    break

        elif a[i - 1] == 3:
            tmp += 3
            if num[1] != deque():
                p = num[1].pop()
                stillset.add(p)
            else:
                pass
        elif a[i - 1] == 4:
            tmp += 4
            pass

print(ans)