p = []
for i in range(5):
    p.append(input())
u = 10
v = 0
for i in range(5):
    if int(p[i][-1]) < u and int(p[i][-1]) != 0:
        u = int(p[i][-1])
        v = int(p[i])
q = []
r = 0
for i in range(5):
    if v != int(p[i]) or r == 1:
        if int(p[i][-1]) != 0:
            q.append(int(p[i]) + 10 - int(p[i][-1]))
        else:
            q.append(int(p[i]))
    else:
        r = 1
print(sum(q) + v)