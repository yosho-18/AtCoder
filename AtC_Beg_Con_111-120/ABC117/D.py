#横にn個入力
n, k = map(int, input().split())
a = input().split()
a = [int(m) for m in a]
#rr = max(a)
bina = [str(bin(m)) for m in a]
lenbina = [len(str(bin(m))) for m in a]

m = 61
x = 0
X = 0
y = 0
tmp0 = 0
tmp1 = 0
ff = [0 for _ in range(n)]
for v in range(m - 1, -1, -1):
    for i in range(n):
        if len(bina[i]) - 2 > v:
            if ff[i] == 0:
                ff[i] = 1
                lenbina[i] = v + 2
            t = int(bina[i][lenbina[i] - v])
            if int(bina[i][lenbina[i] - v]) ^ x == x:
                tmp0 += 1
            else:
                tmp1 += 1
        else:
            #if len(str(bin(k))) - 2 > v:
            tmp0 += 1
    if tmp0 > tmp1:
        X += 2 ** v
        y += 2 ** v
        if X > k:
            X -= 2 ** v
    tmp0 = 0
    tmp1 = 0

ans = 0
for i in range(n):
    ans += a[i] ^ X
print(ans)