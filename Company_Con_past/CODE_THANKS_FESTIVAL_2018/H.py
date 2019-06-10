n = int(input())
a = input().split()
a = [int(m) for m in a]
q = sum(a) - a[-1]
li = [sum(a)]
v = 0
w = sum(a)
flag = 0
for i in range(n):
    if a[i] > 0:
        flag = 1
if n >= 2:
    if q >= 0 and a[-1] >= 0:
        print(sum(a))
    elif q >= 0 and a[-1] <= 0:
        print(q)
    elif q <= 0 and a[-1] >= 0:
        print(a[-1])
    elif q <= 0 and a[-1] <= 0:
        if flag == 0:
            for i in range(n - 1):
                v += a[i]
                w -= a[i]
                k = max(v, w)
                li.append(k)
            print(max(li))
        else:
            print(max(q, a[-1]))
else:
    print(a[0])