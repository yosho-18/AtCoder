from collections import deque
h, w = map(int, input().split())
a = []
for i in range(h):
    a.append(str(input()))
que = deque()
dist = [[-1]*w for i in range(h)]

for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            dist[i][j] = 0
            que.append((i, j))


dd = ((0, -1), (-1, 0), (0, 1), (1, 0))
ans = 0
d = 0
while que:
    y, x = que.popleft() #幅優先探索
    d = dist[y][x]
    for dx, dy in dd:
        nx = x + dx; ny = y + dy
        if 0 <= nx < w and 0 <= ny < h and dist[ny][nx] == -1:
            dist[ny][nx] = 0
            que.append((ny, nx))
            dist[ny][nx] = d + 1
print(d)