#横にn個入力
n, k = map(int, input().split())
a = input().split()
a = [int(m) for m in a]
nli = []
b = 0
for i in range(n):
    for j in range(i, n):
        b += a[j]
        nli.append(b)
    b = 0
nli.sort(reverse=True)
m = 41
x = 0

cnt = 0
candili = []
for i in range(m - 1, -1, -1):
    if x == 0:
        for j in range(len(nli)):
            if nli[j] & (x + 2 ** i) == x + 2 ** i:
                candili.append(nli[j])
                cnt += 1
        if cnt >= k:
            x += 2 ** i
            cnt = 0
        else:
            cnt = 0
            candili = []
    else:
        for j in candili:
            if j & (x + 2 ** i) == x + 2 ** i:
                cnt += 1
        if cnt >= k:
            x += 2 ** i
            cnt = 0
        else:
            cnt = 0
print(x)


