n = int(input())
mod = 10 ** 9 + 7
#?AGC,?ACG,A?GC,AG?C,?GAC

A, G, C, T = 0, 1, 2, 3
#[[[],[]],]
#dp[i][A][T][C] += dp[i - 1][][][]
dp = [[] for i in range(n + 1)]
for i in range(n + 1):
    for j in range(4):
        dp[i].append([])
for i in range(n + 1):
    for j in range(4):
        for k in range(4):
            dp[i][j].append([])
for i in range(n + 1):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                dp[i][j][k].append(0)
dp[0][T][T][T] = 1

for leng in range(n):
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                if dp[leng][c1][c2][c3] == 0:
                    continue
                for x in range(4):
                    if x == C and c1 == G and c2 == A:
                        continue
                    if x == G and c1 == C and c2 == A:
                        continue
                    if x == C and c1 == G and c3 == A:
                        continue
                    if x == C and c2 == G and c3 == A:
                        continue
                    if x == C and c1 == A and c2 == G:
                        continue
                    dp[leng + 1][x][c1][c2] += dp[leng][c1][c2][c3]
                    dp[leng + 1][x][c1][c2] %= mod

ans = 0
for j in range(4):
    for k in range(4):
        for l in range(4):
            ans += dp[n][j][k][l]
            ans %= mod
print(ans)