from heapq import heappush, heappop
from collections import deque
#import copy as cp
n = int(input())
a = input().split()
a = [int(m) for m in a]
#t1 = []
altt1 = []
t2 = deque()
#mt2 = deque()
#t3 = []
mt3 = []
for i in range(3 * n):
    if i < (3 * n) // 3:
        altt1.append(a[i])
        #t1.append(a[i])
    elif (3 * n) // 3 <= i < (3 * n) // 3 * 2:
        t2.append(a[i])
        #mt2.append(-a[i])
    else:
        #t3.append(a[i])
        mt3.append(-a[i])
altt1.sort()
#t1.sort()
#t2.sort()
#mt2.sort()
#t3.sort()
mt3.sort()
#t3.sort(reverse=True)

for _ in range(n):
    pp = heappop(altt1)
    qq = (-heappop(mt3))
    heappush(altt1, pp)
    heappush(mt3, -qq)
    if (t2[0]) - pp >= qq - t2[-1] and (t2[0]) - pp > 0:
        #heappush(t1, t2[0])
        heappush(altt1, t2[0])
        t2.popleft()
        #mt2.popleft()
        #heappop(t1)
        heappop(altt1)
    elif (t2[0]) - pp <= qq - t2[-1] and qq - t2[-1] > 0:
        #heappush(t3, t2[-1])
        heappush(mt3, -t2[-1])
        t2.pop()
        #mt2.pop()
        #heappop(t3)
        heappop(mt3)
    elif (t2[0]) - pp >= qq - t2[-1] and (t2[0]) - pp <= 0:
        #heappush(t1, t2[0])
        #heappush(altt1, t2[0])
        t2.popleft()
        #mt2.popleft()
        #heappop(t1)
    elif (t2[0]) - pp <= qq - t2[-1] and qq - t2[-1] <= 0:
        #heappush(t3, t2[-1])
        #heappush(mt3, t2[-1])
        t2.pop()
        #mt2.pop()
        #heappop(t1)
print(sum(altt1) - (-sum(mt3)))