# -*- coding: utf-8 -*-
from itertools import product
def inpl(): return list(map(int, input().split()))

N, A, B, C = inpl()
L = [int(input()) for _ in range(N)]

ans = float("INF")

for X in product(range(4), repeat=N):#4**n,無ABC,[0,1,3,1,2,3,0]
    P = [[] for _ in range(4)]
    for i, x in enumerate(X):
        P[x].append(L[i])

    if min(map(len, P[1:])) == 0:
        continue

    tmp = 0
    for Q, D in zip(P[1:], [A, B, C]):
        tmp += 10*(len(Q)-1) + abs(D-sum(Q))#2つを1つにするのに10かかる
    if tmp < ans:
        ans = min(tmp, ans)

print(ans)
