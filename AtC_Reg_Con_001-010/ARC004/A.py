import sys

import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
# from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
# from itertools import permutations, combinations, product, accumulate, groupby
# from bisect import bisect_left, bisect_right, insort_left, insort_right
# from operator import itemgetter as ig
# sys.setrecursionlimit(10 ** 7)

def wi(): return list(map(int, sys.stdin.readline().split()))
def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]  # WideIntPoint
def ws(): return sys.stdin.readline().split()
def si(): return int(sys.stdin.readline())
def ss(): return input()
def hi(n): return [si() for _ in range(n)]
def hs(n): return [ss() for _ in range(n)]  # HeightString
def mi(n): return [wi() for _ in range(n)]  # MatrixInt
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]

def main():
    inf = 10 ** 20;
    INF = float("INF");
    ans = 0;
    ans2 = 0;
    tmp = 0;
    ansli = [];
    tmpli = [];
    candili = [];
    mod = 10 ** 9 + 7
    """dd = [(-1, 0), (0, 1), (1, 0), (0, -1)];
    ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)];
    ddn9 = ddn + [(0, 0)]
    for dx, dy in dd:
            nx = j + dx; ny = i + dy
                if 0 <= nx < w and 0 <= ny < h:"""
    n = si()
    xy = mi(n)

    """for i in range(n):
        for j in range(n):
            ans = max(ans, ((xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2) ** 0.5)

    print(ans)"""

    nums = [i for i in range(n)]
    for balls in itertools.combinations(nums, 2):
        i = balls[0]
        j = balls[1]
        ans2 = max(ans2, ((xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2) ** 0.5)

    print(ans2)

if __name__ == '__main__':
    main()