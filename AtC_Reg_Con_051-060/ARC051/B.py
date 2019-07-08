k = int(input())
a = [0] * 41
b = [0] * 41
a[0] = 0
b[0] = 1
a[1] = 2
b[1] = 1
for i in range(2, 41):
    if i % 2 == 0:
        a[i] = a[i - 1]
        b[i] = a[i - 1] + b[i - 1]
    else:
        a[i] = a[i - 1] + b[i - 1]
        b[i] = b[i - 1]

if a[k] >= b[k]:
    print(a[k], b[k])
else:
    print(b[k], a[k])