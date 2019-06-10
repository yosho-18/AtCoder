from collections import deque
n, m = map(int, input().split())
#graph = []
pathli = [[] for _ in range(1000 ** 2)]

for x in range(1, 1000):
    for y in range(1, 1000):
        if x < y:
            x2 = int(str(x)[::-1])
            y2 = y
        else:
            x2 = x
            y2 = int(str(y)[::-1])
        if x2 < y2:
            y2 = y2 - x2
        else:
            x2 = x2 - y2
        #graph.append([[x2, y2], [x, y], 1])
        pathli[1000 * x2 + y2].append(1000 * x + y)

al = n * m
conans = 0
stack = deque()
for i in range(1000):
    stack.append(i)
    stack.append(1000 * i)

flagli = [0]*(1000 ** 2)
while stack != deque([]):
    tmp = stack.pop()
    if flagli[tmp] == 0:
        for k in pathli[tmp]:
            stack.append(k)
            if (not (k % 1000 == 0 or 0 <= k <= m)) and (k % 1000 < m + 1 and k // 1000 < n + 1):
                conans += 1
            flagli[tmp] = 1
print(al - conans)