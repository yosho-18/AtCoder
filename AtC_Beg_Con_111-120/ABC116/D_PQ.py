from heapq import heappush, heappop
#import collections
n, k = map(int, input().split())
c = []
for i in range(n):#h:高さ
    c.append([int(m) for m in input().split()])
c.sort(key=lambda x:(x[0], x[1]))
f = sorted(c, key=lambda x:(x[1], x[0]), reverse=True)
donyoku = 0
donset = set()
#pq = PriorityQueue()
notfirst =[]
for i in range(k):
    if f[i][0] not in donset:
        donset.add(f[i][0])
    else:
        heappush(notfirst, f[i][1])
    donyoku += f[i][1]
donyoku += len(donset)**2

candidate = []
candidateset = set()
donyokulength = len(donset)#len(donset)の長さが変わってしまうので予めとっておく
for i in range(k, n):
    if f[i][0] not in donset:#
        candidate.append(-f[i][1])#最小のものから取り出されるのでマイナスをつけることによって最大のものから取り出せるようにしている
        candidateset.add(f[i][0])
        donset.add(f[i][0])#donsetにも入れて二番目以降の侵入を妨げる

satili = [donyoku]
donyoku -= donyokulength**2
for i in range(len(candidateset)):
    if notfirst == []:
        break
    else:
        donyoku -= heappop(notfirst)
        donyoku += -heappop(candidate)#最小のものから取り出されるのでマイナスをつけることによって最大のものから取り出せるようにしている
        donyoku += (donyokulength + i + 1) ** 2
        satili.append(donyoku)
    donyoku -= (donyokulength + i + 1) ** 2




print(max(satili))
