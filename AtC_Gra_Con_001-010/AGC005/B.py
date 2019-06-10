import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**10
mod = 10**9 + 7

def f():
    n = int(input())
    a = list(map(int, input().split()))
    l = list(range(n+2))
    r = list(range(n+2))
    b = [0]*(n+2)
    for i, x in enumerate(a, 1):
        b[x] = i
    c = 0
    for i in range(n,0,-1):
        bi = b[i]
        c += i * (r[bi] - bi + 1) * (bi - l[bi] + 1)
        r[l[bi]-1] = r[bi]#この部分が分からない
        l[r[bi]+1] = l[bi]#この部分が分からない
    return c

print(f())
