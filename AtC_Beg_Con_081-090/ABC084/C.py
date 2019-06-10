n = int(input())
a = []
for i in range(n - 1):#h:高さ
    a.append([int(m) for m in input().split()])

cp = 0
for i in range(n):
    if i == n - 1:
        print(0)
    else:
        for j in range(i, n - 1):
            if cp == 0:
                k = a[j][1] + a[j][0]
            else:
                if k < a[j][1]:
                    k = a[j][1]
                    k += a[j][0]
                else:
                    if (k - a[j][1]) % a[j][2] == 0:
                        r = 0
                    else:
                        r = a[j][2] - (k - a[j][1]) % a[j][2]
                    k += a[j][0]
                    k += r
            cp = 1
        print(k)
        cp = 0

""" elif j == n - 2:
k += a[j][0]"""