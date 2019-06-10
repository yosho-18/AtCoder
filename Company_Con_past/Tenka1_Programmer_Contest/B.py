n, k = map(int, input().split())
c = []
for i in range(n):#h:高さ
    c.append([int(m) for m in input().split()])

x = 0
candi = [k]
for i in range(31, -1, -1):
    if k & (x + 2 ** i) == x + 2 ** i:
        candi.append(x + 2 ** i - 1)
        x += 2 ** i

ans = 0
tmpans = 0
for can in candi:
    for i in range(n):
        if can & c[i][0] == c[i][0]:
            tmpans += c[i][1]
    ans = max(ans, tmpans)
    tmpans = 0
print(ans)
"""n, k = map(int, input().split())
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
print(x)"""
