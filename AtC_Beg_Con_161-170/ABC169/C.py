import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
import sys
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter as ig
def main():
    sys.setrecursionlimit(10 ** 7)
    inf = 10 ** 20; INF = float("INF"); ans = 0; tmp = 0; cnt = 0; ansli = []; tmpli = []; candili = []; stillset = set()
    eps = 1.0 / 10 ** 10; mod = 10 ** 9 + 7
    dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]; ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)]; ddn9 = ddn + [(0, 0)]
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

    n = i()
    h = wi()

    for i in range(1, n):
        if h[i - 1] < h[i]:
            ans = max(ans, tmp)
            tmp = 0
        else:
            tmp += 1
    ans = max(ans, tmp)
    print(ans)


if __name__ == '__main__':
    main()