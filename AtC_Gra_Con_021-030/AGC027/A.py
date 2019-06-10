n, x = map(int, input().split())
a = [int(m) for m in input().split()]

a.sort()
t = 0
ans = 0
for i in range(n):
    t += a[i]
    if t > x:
        print(ans)
        exit()
    else:
        ans += 1
if t == x:
    print(ans)
else:
    print(ans - 1)