from collections import deque
h, w = map(int, input().split())
a = []
for i in range(h):
    a.append(str(input()))
que = deque()
allque = deque()

for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            que.append((i, j))
            allque.append((i, j))

dd = ((0, -1), (-1, 0), (0, 1), (1, 0))
ans = 0
d = 0
tmpque = deque()

while que:
    while que:
        y, x = que.popleft() #幅優先探索
        for dx, dy in dd:
            nx = x + dx; ny = y + dy
            if 0 <= nx < w and 0 <= ny < h and (ny, nx) not in allque:
                tmpque.append((ny, nx))
                allque.append((ny, nx))
    que += tmpque
    allque = deque(set(allque))
    que = deque(set(que))
    tmpque = deque()
    if que:
        ans += 1
print(ans)