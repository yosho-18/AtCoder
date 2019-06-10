from heapq import heappush, heappop

x, y, z, k = map(int, input().split())
a = [int(m) for m in input().split()]
b = [int(m) for m in input().split()]
c = [int(m) for m in input().split()]
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
Q = [[-(a[0] + b[0] + c[0]), 0, 0, 0]]
ansli = []
se = set()
se.add("0,0,0")
for i in range(k):
    tmp = heappop(Q)
    ansli.append(tmp)
    if tmp[1] != x - 1 and str(tmp[1] + 1) + "," + str(tmp[2]) + "," + str(tmp[3]) not in se:
        heappush(Q, [-(a[tmp[1] + 1] + b[tmp[2]] + c[tmp[3]]), tmp[1] + 1, tmp[2], tmp[3]])
        se.add(str(tmp[1] + 1) + "," + str(tmp[2]) + "," + str(tmp[3]))
    if tmp[2] != y - 1 and str(tmp[1]) + "," + str(tmp[2] + 1) + "," + str(tmp[3]) not in se:
        heappush(Q, [-(a[tmp[1]] + b[tmp[2] + 1] + c[tmp[3]]), tmp[1], tmp[2] + 1, tmp[3]])
        se.add(str(tmp[1]) + "," + str(tmp[2] + 1) + "," + str(tmp[3]))
    if tmp[3] != z - 1 and str(tmp[1]) + "," + str(tmp[2]) + "," + str(tmp[3] + 1) not in se:
        heappush(Q, [-(a[tmp[1]] + b[tmp[2]] + c[tmp[3] + 1]), tmp[1], tmp[2], tmp[3] + 1])
        se.add(str(tmp[1]) + "," + str(tmp[2]) + "," + str(tmp[3] + 1))

for i in range(k):
    print(-ansli[i][0])