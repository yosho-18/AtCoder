n = int(input())
a = input().split()
a = [int(m) for m in a]
xyli = []
for i in range(n - 1):
    if i == 0:
        snu = a[i]
        ara = sum(a) - a[i]
        xyli.append(abs(snu - ara))
    else:
        snu += a[i]
        ara -= a[i]
        xyli.append(abs(snu - ara))
print(min(xyli))