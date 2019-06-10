n, m= map(int, input().split())
c = []
for i in range(n):#h:高さ
    c.append([int(m) for m in input().split()])
c.sort()
ans = 0
buy = 0
for i in range(n):
    if buy + c[i][1] < m:
        buy += c[i][1]
        ans += c[i][0] * c[i][1]
    else:
        ans += (m - buy) * c[i][0]
        break
print(ans)