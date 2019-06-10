import math
n = int(input())

tmp = 0#平方数まで計算
for i in range(n, 0, -1):
    if math.sqrt(i) == int(math.sqrt(i)):
        tmp = i
        break

li = []
tmp2 = 0#積の差が最小になるように
for i in range(n, tmp - 1, -1):
    for j in range(1, int(math.sqrt(n)) + 2):
        if i % j == 0:
            tmp2 = j
    li.append(abs(tmp2 - i // tmp2))
ansli = []
for i in range(n, tmp - 1, -1):
    ansli.append(li[n - i] + n - i)
print(min(ansli))