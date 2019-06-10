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
flagli = [0]*(n + 1)
dp = [[0, 0] for i in range(n + 1)]
stack = [1]

dp[1][0] = 1; dp[1][1] = 1 #0白,1黒
flagli[1] = 1
ans = 1
while stack != []:
    tmpstack = []
    cripoint = stack.pop()
    for point in routedi[cripoint]:
        if flagli[point] == 0:
            tmpstack.append(point)
            flagli[point] = 1
    if tmpstack == []:
        ans *= (dp[cripoint][0] + dp[cripoint][1])
        ans %= mod
    for nowpoint in tmpstack:
        dp[nowpoint][0] = dp[cripoint][0] + dp[cripoint][1]
        dp[nowpoint][1] = dp[cripoint][0]
    stack += tmpstack

print(ans)