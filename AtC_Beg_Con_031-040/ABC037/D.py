import sys
sys.setrecursionlimit(10**7)#再帰の最大回数を増やす
h, w = map(int, input().split())
a = []
for i in range(h):#h:高さ
    a.append([int(m) for m in input().split()])

mod = 10 ** 9 + 7
memo = [[0] * w for i in range(h)]

def f(i, j):
    if memo[i][j] != 0:
        return memo[i][j]
    else:
        tmp = 0
        dd = ((0, -1), (-1, 0), (0, 1), (1, 0))
        for dx, dy in dd:
            nx = j + dx
            ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:
                if a[ny][nx] < a[i][j]:
                    tmp += f(ny, nx)
                    tmp %= mod
        memo[i][j] = tmp + 1#memo化再帰
        memo[i][j] %= mod
        return memo[i][j]

ans = 0
for i in range(h):
    for j in range(w):
        ans += f(i, j)
        ans %= mod
print(ans)