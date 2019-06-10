n, k = map(int, input().split())
s = []
for i in range(n):#h:高さ
    s.append([int(m) for m in input().split()])
s.sort()
t = 0
for i in range(n):
    if i == 0:
        if k <= s[i][1]:
            print(s[i][0])
            break
    elif i == n - 1:
        print(s[i][0])
        break
    else:
        t += s[i - 1][1]
        if t < k <= t + s[i][1]:
            print(s[i][0])
            break