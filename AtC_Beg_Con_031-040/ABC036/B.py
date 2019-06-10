n = int(input())
c = []
for i in range(n):#h:高さ
    c.append([str(m) for m in list(input())])
t = []
for i in range(n):
    t.append([])
for i in range(n):
    for j in range(n):
        t[i].append(c[-j-1][i])
for i in range(n):
    print(''.join(t[i]))