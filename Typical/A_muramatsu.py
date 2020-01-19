from collections import deque
import sys
sys.setrecursionlimit(1000000)

#INF = 1001001001
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]
H, W = map(int, input().split())
S = [input() for _ in range(H)]

#ans = 0
q = deque([])
dist = [['False'] * W for _ in range(H)]
for si in range(H):
    for sj in range(W):
        if S[si][sj] == 's':
            q.append([si,sj])
            #dist[si][sj] = 0

flag = 'False'
ans = 'No'
while q:
    if flag=='True':
        break
    i, j = q.popleft()
    for d in range(4):
        ni = i + di[d]      # 右　左　上　下　入力
        nj = j + dj[d]
        if (ni < 0 or ni >= H or nj < 0 or nj >= W):
            continue
        if S[ni][nj] == '#':     #壁があったらスキップ
            continue
        if S[ni][nj] == 'g':
            ans = 'Yes'
            flag = 'True'
            break
        if dist[ni][nj] != 'False':  #探索済みかどうか
            continue
        q.append((ni, nj))
        dist[ni][nj] = 'True'

print(ans)
