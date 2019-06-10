#横にn個入力
n, k = map(int, input().split())

#n...普通、a...横で入力された複数の要素を配列で取得
a = input().split()

x = [int(m) for m in a]
lx = []
mx = []
rx = []
for i in range(n):
    if x[i] < 0:
        lx.append(x[i])
    elif x[i] == 0:
        mx.append(x[i])
    else:
        rx.append(x[i])

lx.sort(reverse=True)
rx.sort()
lmx = lx + mx
lmx.sort(reverse=True)
ans1 = float("INF")
if len(lmx) >= k:
    ans1 = abs(lmx[k - 1])

mrx = mx + rx
mrx.sort()
ans2 = float("INF")
if len(mrx) >= k:
    ans2 = abs(mrx[k - 1])

p = 1
ans3 = float("INF")
while p <= len(rx):
    if len(rx) >= p and len(lx) >= k - p - len(mx) and k - p - len(mx) > 0:
        if ans3 > abs(2 * rx[p - 1]) + abs(lx[k - p - len(mx) - 1]):
            ans3 = abs(2 * rx[p - 1]) + abs(lx[k - p - len(mx) - 1])
    p += 1

q = 1
ans4 = float("INF")
while q <= len(lx):
    if len(lx) >= q and len(rx) >= k - q - len(mx) and k - q - len(mx) > 0:
        if ans4 > abs(2 * lx[q - 1]) + abs(rx[k - q - len(mx) - 1]):
            ans4 = abs(2 * lx[q - 1]) + abs(rx[k - q - len(mx) - 1])
    q += 1

print(min(ans1,ans2,ans3,ans4))

"""import copy
#横にn個入力
n, k = map(int, input().split())

#n...普通、a...横で入力された複数の要素を配列で取得
a = input().split()

x = [int(m) for m in a]

X = []

X = copy.deepcopy(x)
X.append(0)
X.sort()

co1 = 0
co2 = 0
co3 = 0
co4 = 0
co3ar = []
co4ar = []

if 0 in x:
    if len(x) > x.index(0) + k - 1:
        co1 = x[x.index(0) + k - 1]
    else:
        co1 = 10 ** 9
else:
    if len(X) > X.index(0) + k:
        co1 = X[X.index(0) + k]
    else:
        co1 = 10 ** 9

if 0 in x:
    if 0 <= x.index(0) - (k - 1):
        co2 = - x[x.index(0) - (k - 1)]
    else:
        co2 = 10 ** 9
else:
    if 0 <= X.index(0) - k:
        co2 = - X[X.index(0) - k]
    else:
        co2 = 10 ** 9

if 0 in x:
    for i in range(1, n + 1):
        if i >= k - i:
            break
        else:
            co3ar.append(x[x.index(0) + i] + x[x.index(0) + i] - x[x.index(0) + 1 - (k - i)])
else:
    for i in range(1, n + 1):
        if i >= k - i:
            break
        else:
            co3ar.append(X[X.index(0) + i] + X[X.index(0) + i] - X[X.index(0) - (k - i)])


if 0 in x:
    for i in range(1, n + 1):
        if i >= k - i:
            break
        else:
            co4ar.append(- x[x.index(0) - i] + x[x.index(0) + k - i - 1] - x[x.index(0) - i])
else:
    for i in range(1, n + 1):
        if i >= k - i:
            break
        else:
            co4ar.append(- X[X.index(0) - i] + X[X.index(0) + k - i] - X[X.index(0) - i])

if co3ar == []:
    co3 = 10 ** 9
else:
    co3 = min(co3ar)

if co4ar == []:
    co4 = 10 ** 9
else:
    co4 = min(co4ar)

print(min(co1,co2,co3,co4))
"""
