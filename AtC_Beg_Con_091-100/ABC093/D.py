import math

q = int(input())
s = []
for i in range(q):#h:高さ
    s.append([int(m) for m in input().split()])

def doublecount(dc, i):
    if dc >= s[i][0] and dc >= s[i][1]:
        return -2
    elif dc >= s[i][0] or dc >= s[i][1]:
        return -1
    else:
        return 0


count = 0
for i in range(q):
    t = int(math.sqrt(s[i][0] * s[i][1]))
    if t * (t + 1) < s[i][0] * s[i][1]:
        count = t * 2
        count += doublecount(t, i)
        print(count)
    else:
        if t * t < s[i][0] * s[i][1]:
            count = t * 2 - 1
            count += doublecount(t, i)
            print(count)
        else:
            count = (t - 1) * 2
            count += doublecount(t - 1, i)
            print(count)

