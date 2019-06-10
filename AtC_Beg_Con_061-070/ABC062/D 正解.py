from heapq import heappush, heappop
n = int(input())
a = input().split()
a = [int(m) for m in a]
t1 = []
t2 = []
mt3 = []
for i in range(3 * n):
    if i < (3 * n) // 3:
        t1.append(a[i])
    elif (3 * n) // 3 <= i < (3 * n) // 3 * 2:
        t2.append(a[i])
    else:
        mt3.append(-a[i])
t1.sort()
mt3.sort()
t1sumli = [sum(t1)]
t3sumli = [-sum(mt3)]
for i in range(n):
    pp = heappop(t1)
    heappush(t1, max(pp, t2[i]))
    t1sumli.append(t1sumli[-1] - pp + max(pp, t2[i]))

for i in range(n - 1, -1, -1):
    qq = -heappop(mt3)
    heappush(mt3, -min(qq, t2[i]))
    t3sumli.append(t3sumli[-1] - qq + min(qq, t2[i]))

sumli = []
for i in range(n + 1):
    sumli.append(t1sumli[i] - t3sumli[-i-1])
print(max(sumli))