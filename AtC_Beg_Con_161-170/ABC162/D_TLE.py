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


r_list= []
g_list = []
b_list = []
def length(t):
    if t == "R":
        return len(r_list)
    elif t == "G":
        return len(g_list)
    else:
        return len(b_list)

def rgb_list(t):
    if t == "R":
        return r_list
    elif t == "G":
        return g_list
    else:
        return b_list
n = i()
s = s()

for i, t in enumerate(s):
    if t == "R":
        r_list.append(i)
    elif t == "G":
        g_list.append(i)
    else:
        b_list.append(i)

rgb = ["R", "G", "B"]
s_start = 0
t_start = 0
for color in itertools.permutations(rgb, 3):
    f_len = length(color[0])
    s_len = length(color[1])
    t_len = length(color[2])
    f_list = rgb_list(color[0])
    s_list = rgb_list(color[1])
    t_list = rgb_list(color[2])

    s_start = 0
    for first in f_list:
        t_start = 0
        flag = 0
        for s_i in range(s_start, len(s_list)):
            second = s_list[s_i]
            if first < second:
                if flag == 0:
                    s_start = s_i
                    flag += 1
                interval = second - first
                if first + 2 * interval in set(t_list):
                    ans -= 1
                for t_i in range(t_start, len(t_list)):
                    third = t_list[t_i]
                    if second < third:
                        ans += t_len - t_i
                        t_start = t_i
                        break
                else:
                    break

print(ans)

