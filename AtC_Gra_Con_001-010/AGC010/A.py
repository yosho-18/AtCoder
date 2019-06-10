n = int(input())
a = [int(m) for m in input().split()]
oddcnt = 0
for i in range(n):
    if a[i] % 2 == 1:
        oddcnt += 1
if oddcnt % 2 == 1:
    print("NO")
else:
    print("YES")