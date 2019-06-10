n = int(input())
c = []
for i in range(n):#h:高さ
    c.append([int(m) for m in input().split()]+[i])
"""d = []
for i in range(n):#h:高さ
    d.append([c[i][1], c[i][0], i])"""
tans = 0
aans = 0
sumc = []

for i in range(n):
    sumc.append([c[i][0] + c[i][1], i])

sumc.sort(reverse=True)

for i in range(n):
    if i % 2 == 0:
        tans += c[sumc[i][1]][0]
    else:
        aans += c[sumc[i][1]][1]

print(tans -aans)