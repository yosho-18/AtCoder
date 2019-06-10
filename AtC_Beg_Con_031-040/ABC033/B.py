n = int(input())
s = []
p = []
for i in range(n):#h:高さ
    pi, qi = map(str, input().split())
    s.append(pi)
    p.append(qi)
for i in range(n):
    p[i] = int(p[i])
sm = sum(p)
ans = "atcoder"
for i in range(n):
    if p[i] > sm / 2:
        ans = s[i]
        break
print(ans)