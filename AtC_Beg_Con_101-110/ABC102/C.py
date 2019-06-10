import statistics

n = int(input())
a = input().split()
a = [int(m) for m in a]
x = []

for i in range(1, n + 1):
    x.append(a[i - 1] - i)

x.sort()

y1 = []
y2 = []
c = 0

if n % 2 == 0:
    #statistics.median()
    for i in range(n):
        if i <= int(n / 2) - 1:
            y1.append(x[i])
        else:
            y2.append(x[i])

    sumy1 = sum(y1)
    sumy2 = sum(y2)
    sumar = sumy2 - sumy1
    print(sumar)

w = []
z1 = []
z2 = []
d = 0

if n % 2 != 0:
    #med = x[int((n + 1) / 2)]
    #statistics.median()
    for h in range(1, n + 1):#中央値を排除
        if h != (n + 1) / 2:
            w.append(x[h - 1])
    for i in range(n - 1):#中央値の分をひく
        if i <= int((n - 1) / 2) - 1:#長さをリストのインデックス番号に変換するために１をひく
            z1.append(w[i])
        else:
            z2.append(w[i])
    sumz1 = sum(z1)
    sumz2 = sum(z2)
    sumar = sumz2 - sumz1
    print(sumar)
