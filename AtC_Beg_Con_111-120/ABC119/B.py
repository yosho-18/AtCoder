n = int(input())
c = []
for i in range(n):#h:高さ
    c.append([str(m) for m in input().split()])
for i in range(n):
    c[i][0] = float(c[i][0])
ans = 0
for i in range(n):
    if c[i][1] == "JPY":
        ans += c[i][0]
    else:
        ans += c[i][0] * 3.8 * (10 ** 5)
print(ans)