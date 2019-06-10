import math
n, h = map(int, input().split())
s = []
for i in range(n):#h:高さ
    s.append([int(m) for m in input().split()])#a,b
t = []
for i in range(n):
    t.append(["a", i + 1, s[i][0]])
    t.append(["b", i + 1, s[i][1]])
t.sort(key=lambda x:(x[2]),reverse=True)

count = 0
p = 0
for i in range(n + 1):
    if t[i][0] == "b":
        h -= t[i][2]
        count += 1
        if h <= 0:
            break
    else:
        count += math.ceil(h / t[i][2])
        break
print(count)
