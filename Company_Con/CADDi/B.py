n, h, w = map(int, input().split())
c = []
for i in range(n):#h:高さ
    c.append([int(m) for m in input().split()])

ans = 0
for i in range(n):
    if c[i][0] >= h and c[i][1] >= w:
        ans += 1
print(ans)