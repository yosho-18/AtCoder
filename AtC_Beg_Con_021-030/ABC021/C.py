from collections import deque
n = int(input())
a, b = map(int, input().split())
m = int(input())
z = []
for i in range(m):#h:高さ
    z.append([int(m) for m in input().split()])

mod = 10**9 + 7
p_to_p = [[] for i in range(n + 1)]
dp = [[0] * 500 for i in range(500)]
flagli = [[0, 0] for i in range(n + 1)]
for i in range(m):
    p_to_p[z[i][0]].append(z[i][1])
    p_to_p[z[i][1]].append(z[i][0])

que = deque()
k = 0
que.append([a, k])
flagli[a][0] = 1
tmp = 0
queset = set()
while True:
    if que == deque():
        break
    nowli = que.popleft()
    k = nowli[1] + 1
    if flagli[b][0] != 0 and k != tmp:#bが終わったら終了
        break
    for p in p_to_p[nowli[0]]:
        if flagli[p][0] == 0 or flagli[p][1] == k:#最短経路以外通さない
            if (p, k) not in queset:#二個以上通さない
                queset.add((p, k))
                que.append([p, k])
                flagli[p][0] = 1
                flagli[p][1] = k
            if k != 1:#一個前のを個数にカウント
                dp[k][p] += dp[k - 1][nowli[0]]
            else:
                dp[k][p] += 1
            dp[k][p] %= mod
            if p == b:
                tmp = k

print(dp[tmp][b] % mod)