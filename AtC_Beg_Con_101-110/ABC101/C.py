n, k = map(int, input().split())
a = input().split()

a = [int(m) for m in a]
t = a.index(min(a))#1

leftar = []
rightar = []
leftco = 0
rightco = 0
startco = 1
#左側
for i in range(1, k + 1):
    if (t - k + i) / (k - 1) <= 0:#マイナス、０のときは０とする
        leftar.append(leftco)
    elif (t - k + i) % (k - 1) == 0:
        p = int((t - k + i) / (k - 1))
        for j in range(1, p + 1):
            leftco += 1
        leftar.append(leftco)
        leftco = 0
    else:#割り切れないときは繰り上げ
        p = int((t - k + i) / (k - 1)) + 1
        for j in range(1, p + 1):
            leftco += 1
        leftar.append(leftco)
        leftco = 0
#右側
for i in range(1, k + 1):
    if (n - t - i) / (k - 1) <= 0:
        rightar.append(rightco)
    if (n - t - i) % (k - 1) == 0:
        q = int((n - t - i) / (k - 1))
        for j in range(1, q + 1):
            rightco += 1
        rightar.append(rightco)
        rightco = 0
    else:
        q = int((n - t - i) / (k - 1)) + 1
        for j in range(1, q + 1):
            rightco += 1
        rightar.append(rightco)
        rightco = 0

sumar = [x + y + startco for (x, y) in zip(leftar, rightar)]

print(min(sumar))