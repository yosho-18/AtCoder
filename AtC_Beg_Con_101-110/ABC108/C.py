n, k = map(int, input().split())

a = []

for i in range(1, n + 1):
    if k % 2 != 0:
        if i % k == 0:
            a.append(i)
    if k % 2 == 0:
        if i % int(k/2) == 0:
            a.append(i)

e = []
f = []
if k % 2 == 0:
    for j in range(len(a)):
        if a[j] % 2 != 0:
            e.append(a[j])
        if a[j] % 2 == 0:
            f.append(a[j])

if k % 2 != 0:
    print(len(a)**3)

if k % 2 == 0:
    if len(a) % 2 != 0:
        print(int(((len(a) + 1)/2) ** 3 + ((len(a) - 1)/2) ** 3))
    else:
        print(int((len(a)/2) ** 3))
