n, z, w = map(int, input().split())
a = input().split()
a = [int(m) for m in a]
if n == 1:
    print(abs(a[n - 1] - w))
else:
    print(max(abs(a[n - 1] - w), abs(a[n - 1] - a[n - 2])))
"""k = 0
while a != []:
    if k % 2 == 0:
        for i in range(len(a)):
            if i == 0:
                zc = a[i]
                zcn = i
            elif abs(zc - w) <= abs(a[i] - w):
                zc = a[i]
                zcn = i
        z = zc
        a = a[zcn + 1:]
        k += 1
    else:
        for i in range(len(a)):
            if i == 0:
                wc = a[i]
                wcn = i
            elif abs(wc - z) >= abs(a[i] - z):
                wc = a[i]
                wcn = i
        w = wc
        a = a[wcn + 1:]
        k += 1

print(abs(z - w))"""