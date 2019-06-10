import itertools
from functools import reduce

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcd_list(numbers):
    return reduce(gcd, numbers)

a, b = map(int, input().split())
#x.2の倍数の組(not 3k)
#y.3の倍数の組(not 2k)
#z.6の倍数の組
#w.それ以外の互いに素の組

allli = []
for i in range(a, b + 1):
    allli.append(i)

li6 = []
li2 = [1]
li3 = [1]
otherli = []
for i in allli:
    if i % 6 == 0:
        li6.append(i)
    elif i % 2 == 0:
        li2.append(i)
    elif i % 3 == 0:
        li3.append(i)
    else:
        otherli.append(i)


othergroup = []
for i in range(1, len(otherli) + 1):
    for balls in itertools.combinations(otherli, i):
        if len(balls) != 1:
            for ba in itertools.combinations(balls, 2):
                if gcd(ba[0], ba[1]) != 1:
                    break
            else:
                othergroup.append(balls)
        elif len(balls) == 1:
            othergroup.append(balls)

ans = 0
othergroup.append([1])
#x1つ+y1つ+w
for i in li2:
    for j in li3:
        for k in othergroup:
            if gcd(i, j) != 1:  # 2*7,3*7とか
                break
            for v in k:
                if gcd(i, v) != 1:
                    break
                if gcd(j, v) != 1:
                    break
            else:
                ans += 1

#z1つ+w
for i in li6:
    for k in othergroup:
        for v in k:
            if gcd(i, v) != 1:
                break
        else:
            ans += 1

print(ans)