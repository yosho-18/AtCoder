n, x = map(int, input().split())
a = input().split()
a = [int(m) for m in a]
ans = 0
for i in range(1, n):
    t = a[i] + a[i - 1]
    if t <= x:
        pass
    else:
        ans += a[i] - (x - a[i - 1])
        if i == 1:
            if x - a[i - 1] < 0:
                a[i] = 0
                a[i - 1] = x
            else:
                a[i] = x - a[i - 1]
        else:
            a[i] = x - a[i - 1]
print(ans)