import sys

import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random

# from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
# from itertools import permutations, combinations, product, accumulate, groupby
# from bisect import bisect_left, bisect_right, insort_left, insort_right
# from operator import itemgetter as ig
sys.setrecursionlimit(10 ** 7)
# inf = 10 ** 20; INF = float("INF"); ans = 0; tmp = 0; ansli = []; tmpli = []; candili = []; mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)];
ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)];
ddn9 = ddn + [(0, 0)]
"""for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:"""


def wi(): return list(map(int, sys.stdin.readline().split()))


def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]  # WideIntPoint


def ws(): return sys.stdin.readline().split()


def i(): return int(sys.stdin.readline())


def s(): return input()


def hi(n): return [i() for _ in range(n)]


def hs(n): return [s() for _ in range(n)]  # HeightString


def mi(n): return [wi() for _ in range(n)]  # MatrixInt


def mip(n): return [wip() for _ in range(n)]


def ms(n): return [[str(m) for m in list(input())] for _ in range(n)]


if __name__ == '__main__':
    b = ms(19)
    blackcnt = 0;
    whitecnt = 0
    for i in range(19):
        for j in range(19):
            if b[i][j] == "o":
                blackcnt += 1
            elif b[i][j] == "x":
                whitecnt += 1
    finishwhite = 0
    finishblack = 0
    if blackcnt == whitecnt + 1:
        finishblack = 1
    elif whitecnt == blackcnt:
        finishwhite = 1
    else:
        print("NO")
        exit()

    notfinish_sign = "x" if finishblack == 1 else "o"
    for i in range(19):
        for j in range(19):
            if b[i][j] == notfinish_sign:
                for dx, dy in ddn:
                    for k in range(1, 5):
                        nx = j + dx * k;
                        ny = i + dy * k
                        if 0 <= nx < 19 and 0 <= ny < 19:
                            if b[ny][nx] != notfinish_sign:
                                break
                        else:
                            break
                    else:
                        print("NO")
                        exit()

    finish_sign = "o" if finishblack == 1 else "x"
    flagli = [[[0, 0, 0, 0] for _ in range(19)] for _ in range(19)]  # →，↓，↘，↙
    arrowli = [[0, 1], [1, 0], [1, 1], [1, -1]]
    overfiveli = []
    overfiveli2 = []
    for arrow in range(4):
        for i in range(19):
            for j in range(19):
                if b[i][j] == finish_sign and flagli[i][j][arrow] == 0:
                    tmpli = [i * 19 + j]
                    flagli[i][j][arrow] = 1
                    for k in range(1, 10):
                        nx = j + arrowli[arrow][1] * k;
                        ny = i + arrowli[arrow][0] * k
                        if 0 <= nx < 19 and 0 <= ny < 19:
                            if b[ny][nx] != finish_sign:
                                if k >= 5:
                                    overfiveli.append(tmpli[k - 5:5])
                                    overfiveli2.append(tmpli)
                                break
                            else:
                                flagli[ny][nx][arrow] = 1
                                tmpli.append(ny * 19 + nx)
                        else:
                            if k >= 5:
                                overfiveli.append(tmpli[k - 5:5])
                                overfiveli2.append(tmpli)
                            break
                    else:
                        print("NO")
                        exit()
    if len(overfiveli) == 1:
        print("YES")
        exit()
    ansli = functools.reduce(lambda a, b: a + b, overfiveli) if overfiveli != [] else []
    ansli2 = functools.reduce(lambda a, b: a + b, overfiveli2) if overfiveli2 != [] else []
    c = collections.Counter(ansli2)
    cnt = 0
    sym = 0
    for i in c:
        if c[i] >= 2:
            cnt += 1
            sym = i
        if cnt == 2:
            print("NO")
            exit()
    for i in overfiveli2:
        if sym not in set(i):
            print("NO")
            exit()
    print("YES" if (len(ansli) == len(set(ansli)) + 1 and len(ansli2) == len(set(ansli2)) + 1) or ansli == [] else "NO")



"""
...................
...................
............o.x....
............o......
....x.......o......
............o......
.......x....o......
.......ooooo.......
..x.....o....o.....
......x.ox.....o...
........o..o.......
.x.....xo......x...
...................
..x................
.........x.........
...x.....x.........
.........x.x.......
...x...............
...................
"""

"""
まず，白黒の個数が妥当かを検討する．次に，最終番手ではない方が5目になっていないかを確かめる．
最後に，最終番手の方を調べていく．五目以上になっていいる場所を探し，ありうる最後の手を考える．違うところで二つ以上出てきたらアウト．
五目が一つのとき，ないときはOK．
候補が一つしかないとすると，それが全ての五目に関わっているかを確かめる．関わっていなかったら矛盾．
"""