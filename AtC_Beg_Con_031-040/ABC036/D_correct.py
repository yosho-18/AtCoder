import sys
sys.setrecursionlimit(10 ** 7)
n = int(input())
c = []
for i in range(n - 1):#h:高さ
    c.append([int(m) for m in input().split()])

mod = 10 ** 9 + 7

routedi = {}
for i in range(n + 1):
    routedi[i] = []
for i in range(n - 1):
    routedi[c[i][0]].append(c[i][1])
    routedi[c[i][1]].append(c[i][0])

memof = [-1] * (n + 1)
memog = [-1] * (n + 1)
parli = [-1] * (n + 1)#親を保持
def f(x):#全
    if memof[x] != -1:
        return memof[x]
    else:
        pig = 1
        for i in routedi[x]:
            if parli[x] != i:#親が来るときは断る
                parli[i] = x
                pig *= g(i)
                pig %= mod
        memof[x] = g(x) + pig
        return memof[x]

def g(x):#白
    if memog[x] != -1:
        return memog[x]
    else:
        pif = 1
        for i in routedi[x]:
            if parli[x] != i:#親が来るときは断る
                parli[i] = x
                pif *= f(i)
                if f(i) == 1:
                    pif *= 2
                pif %= mod
        memog[x] = pif
        return memog[x]

print(f(1) % mod)