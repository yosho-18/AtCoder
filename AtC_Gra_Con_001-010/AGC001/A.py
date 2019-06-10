n = int(input())
l = [int(m) for m in input().split()]

l.sort()

ans = 0
for i in range(0, 2 * n, 2):
    ans += l[i]

print(ans)