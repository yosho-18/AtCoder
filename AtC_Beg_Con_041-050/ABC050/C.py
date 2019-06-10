n = int(input())
a = input().split()
a = [int(m) for m in a]
pn = [0]*n
for i in range(n):
    pn[(-a[i] + n - 1)//2] += 1
    if (-a[i] + n - 1)//2 != (a[i] + n - 1)//2:
        pn[(a[i] + n - 1)//2] += 1
for i in range(n):
    if pn[i] > 2:
        print(0)
        exit()
    if n % 2 != 0:
        if pn[(n - 1) // 2] > 1:
            print(0)
            exit()

ans = 1
mod = 10**9 + 7
for i in range(n):
    if i <= (n - 1) // 2:
        ans = (ans * pn[i]) % mod
    else:
        break
print(ans)