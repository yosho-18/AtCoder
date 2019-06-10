n = int(input())
f = []
for i in range(n):#h:高さ
    f.append([int(m) for m in input().split()])
p = []
for i in range(n):#h:高さ
    p.append([int(m) for m in input().split()])

fcount = 0
pcount= 0
pli = []
for i0 in range(2):
    for i1 in range(2):
        for i2 in range(2):
            for i3 in range(2):
                for i4 in range(2):
                    for i5 in range(2):
                        for i6 in range(2):
                            for i7 in range(2):
                                for i8 in range(2):
                                    for i9 in range(2):
                                        ili = [i0,i1,i2,i3,i4,i5,i6,i7,i8,i9]
                                        if ili != [0,0,0,0,0,0,0,0,0,0]:
                                            for j in range(n):
                                                for k in range(10):
                                                    if ili[k] == f[j][k] and ili[k] == 1:
                                                        fcount += 1
                                                pcount += p[j][fcount]
                                                fcount = 0
                                            pli.append(pcount)
                                            pcount = 0
print(max(pli))