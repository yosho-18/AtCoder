n, m = map(int, input().split())
x = [int(m) for m in input().split()]
y = [int(m) for m in input().split()]
mod = 10 ** 9 + 7
bx = []
for i in range(1, n):
    bx.append(abs(x[i] - x[i - 1]))

mulx = []
for i in range(1, n):
    mulx.append(i * (n - i))

ansx = 0
for i in range(n - 1):
    ansx += bx[i] * mulx[i]
    #ansx = ansx % mod
ansx = ansx * (m - 1)
#ansx = ansx % mod


by = []
for i in range(1, m):
    by.append(abs(y[i] - y[i - 1]))

muly = []
for i in range(1, m):
    muly.append(i * (m - i))


ans = 0
for i in range(m - 1):
    ans += by[i] * ansx * muly[i] // muly[0]
    ans = ans % mod

ans = ans % mod
print(ans)