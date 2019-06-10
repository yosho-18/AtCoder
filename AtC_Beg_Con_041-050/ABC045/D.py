"""import time

if __name__ == '__main__':
    start = time.time()
    p = 0
    li = []
    y = []
    for i in range(0,3*10**6):
        li.append(i)
        y.append(i + 1)
        p += 1
    print(p)
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")"""
h, w, n = map(int, input().split())
c = set()
c2 = []
for i in range(n):#h:高さ
    c2.append([int(m) for m in input().split()])
for i in range(n):
    c2[i] = tuple(c2[i])
for i in range(n):
    c.add(c2[i])

vec = []
for i in range(-2, 3):
    for j in range(-2, 3):
        if i != 0 or j != 0:
            vec.append((i,j))
sq = {}
ansdi = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0 , 6:0, 7:0, 8:0, 9:0}
for i in range(n):
    for k in vec:
        if 0 < c2[i][0] + k[0] <= h and 0 < c2[i][1] + k[1] <= w:
            if (c2[i][0] + k[0], c2[i][1] + k[1]) in c:
                sq[str(k[0]) + str(k[1])] = 1
            else:
                sq[str(k[0]) + str(k[1])] = 0
        else:
            sq[str(k[0]) + str(k[1])] = -1
    k1 = [sq["-2-2"], sq["-1-2"], sq["0-2"],sq["-2-1"], sq["-1-1"], sq["0-1"], sq["-20"], sq["-10"]].count(1) + 1
    l1 = [sq["-2-2"], sq["-1-2"], sq["0-2"],sq["-2-1"], sq["-1-1"], sq["0-1"], sq["-20"], sq["-10"]].count(-1)
    if l1 == 0:
        ansdi[k1] += 1
    k2 = [sq["-21"], sq["-11"], sq["01"], sq["-20"], sq["-10"], sq["-2-1"], sq["-1-1"], sq["0-1"]].count(1) + 1
    l2 = [sq["-21"], sq["-11"], sq["01"], sq["-20"], sq["-10"], sq["-2-1"], sq["-1-1"], sq["0-1"]].count(-1)
    if l2 == 0:
        ansdi[k2] += 1
    k3 = [sq["-22"], sq["-12"], sq["02"], sq["-21"], sq["-11"], sq["01"], sq["-20"], sq["-10"]].count(1) + 1
    l3 = [sq["-22"], sq["-12"], sq["02"], sq["-21"], sq["-11"], sq["01"], sq["-20"], sq["-10"]].count(-1)
    if l3 == 0:
        ansdi[k3] += 1
    k4 = [sq["-1-2"], sq["0-2"], sq["1-2"], sq["-1-1"], sq["0-1"], sq["1-1"], sq["-10"], sq["10"]].count(1) + 1
    l4 = [sq["-1-2"], sq["0-2"], sq["1-2"], sq["-1-1"], sq["0-1"], sq["1-1"], sq["-10"], sq["10"]].count(-1)
    if l4 == 0:
        ansdi[k4] += 1
    k5 = [sq["-1-1"], sq["0-1"], sq["1-1"], sq["-10"], sq["10"], sq["-11"], sq["01"], sq["11"]].count(1) + 1
    l5 = [sq["-1-1"], sq["0-1"], sq["1-1"], sq["-10"], sq["10"], sq["-11"], sq["01"], sq["11"]].count(-1)
    if l5 == 0:
        ansdi[k5] += 1
    k6 = [sq["-10"], sq["10"], sq["-11"], sq["01"], sq["11"], sq["-12"], sq["02"], sq["12"]].count(1) + 1
    l6 = [sq["-10"], sq["10"], sq["-11"], sq["01"], sq["11"], sq["-12"], sq["02"], sq["12"]].count(-1)
    if l6 == 0:
        ansdi[k6] += 1
    k7 = [sq["0-2"], sq["1-2"], sq["2-2"], sq["0-1"], sq["1-1"], sq["2-1"], sq["10"], sq["20"]].count(1) + 1
    l7 = [sq["0-2"], sq["1-2"], sq["2-2"], sq["0-1"], sq["1-1"], sq["2-1"], sq["10"], sq["20"]].count(-1)
    if l7 == 0:
        ansdi[k7] += 1
    k8 = [sq["0-1"], sq["1-1"], sq["2-1"], sq["10"], sq["20"], sq["01"], sq["11"], sq["21"]].count(1) + 1
    l8 = [sq["0-1"], sq["1-1"], sq["2-1"], sq["10"], sq["20"], sq["01"], sq["11"], sq["21"]].count(-1)
    if l8 == 0:
        ansdi[k8] += 1
    k9 = [sq["10"], sq["20"], sq["01"], sq["11"], sq["21"], sq["02"], sq["12"], sq["22"]].count(1) + 1
    l9 = [sq["10"], sq["20"], sq["01"], sq["11"], sq["21"], sq["02"], sq["12"], sq["22"]].count(-1)
    if l9 == 0:
        ansdi[k9] += 1
    sq = {}
for i in ansdi:
    if i != 0:
        ansdi[i] = ansdi[i] // i
ansdi[0] = (h - 2) * (w - 2) - sum(ansdi.values())
for i in ansdi:
    print(ansdi[i])