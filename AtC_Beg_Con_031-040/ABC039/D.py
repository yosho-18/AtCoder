import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, copy, functools, random
from collections import deque
from heapq import heappush, heappop
sys.setrecursionlimit(10 ** 7)
ans = 0
tmp = 0
inf = 10 ** 20
INF = float("INF")
eps = 1.0 / 10 ** 10
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
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

h, w = wi()
s = hs(h)
ansli = [["."] * w for i in range(h)]
for i in range(h):
    for j in range(w):
        for dx, dy in ddn + [(0, 0)]:
            nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:
                if s[ny][nx] == ".":
                    break
        else:
            ansli[i][j] = "#"

confirmli = [["."] * w for i in range(h)]
for i in range(h):
    for j in range(w):
        for dx, dy in ddn + [(0, 0)]:
            nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:
                if ansli[ny][nx] == "#":
                    confirmli[i][j] = "#"
                    break

for i in range(h):
    confirmli[i] = ''.join(confirmli[i])

if confirmli == s:
    print("possible")
    for i in range(h):
        for j in range(w):
            print(ansli[i][j] ,end="")
        print()
else:
    print("impossible")