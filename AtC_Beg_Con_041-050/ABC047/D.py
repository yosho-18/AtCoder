n, t = map(int, input().split())
a = input().split()
a = [int(m) for m in a]
b = sorted(a, reverse=True)
c = set()
k = 1
v = 0
high = 0
ansli = []
for i in range(n - 1):
    c.add(a[i])
    if i == 0 or high == a[i]:
        if i == 0 and b[0] == a[i]:
            v += 1
        while True:
            if b[v] in c:
                v += 1
            else:
                break
        for j in range(k, n):
            if a[j] == b[v] and a[j] not in c:
                high = a[j]
                k = j + 1
                v += 1
                break
            elif a[j] == b[v]:
                v += 1
                while True:
                    if b[v] in c:
                        v += 1
                    else:
                        break
    ansli.append(high - a[i])

ansli.sort(reverse=True)
ans = 1
for i in range(1, n - 1):
    if ansli[i - 1] != ansli[i]:
        break
    else:
        ans += 1
print(ans)