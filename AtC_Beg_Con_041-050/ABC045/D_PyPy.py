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
        vec.append((i,j))
chuukai = []
for i in range(5):
    for j in range(5):
        chuukai.append([i, j])

sq = [[0 for i in range(5)] for j in range(5)]
ansdi = [0]*10
chuukainum = 0
for i in range(n):
    for k in vec:
        if 0 < c2[i][0] + k[0] <= h and 0 < c2[i][1] + k[1] <= w:
            if (c2[i][0] + k[0], c2[i][1] + k[1]) in c:
                sq[chuukai[chuukainum][0]][chuukai[chuukainum][1]] = 1
        else:
            sq[chuukai[chuukainum][0]][chuukai[chuukainum][1]] = -1
        chuukainum += 1
    k1 = [sq[0][0], sq[0][1], sq[0][2],sq[1][0], sq[1][1], sq[1][2], sq[2][0], sq[2][1]].count(1) + 1
    l1 = [sq[0][0], sq[0][1], sq[0][2],sq[1][0], sq[1][1], sq[1][2], sq[2][0], sq[2][1]].count(-1)
    if l1 == 0:
        ansdi[k1] += 1
    k2 = [sq[0][3], sq[0][1], sq[0][2],sq[1][3], sq[1][1], sq[1][2], sq[2][3], sq[2][1]].count(1) + 1
    l2 = [sq[0][3], sq[0][1], sq[0][2],sq[1][3], sq[1][1], sq[1][2], sq[2][3], sq[2][1]].count(-1)
    if l2 == 0:
        ansdi[k2] += 1
    k3 = [sq[0][3], sq[0][4], sq[0][2],sq[1][3], sq[1][4], sq[1][2], sq[2][3], sq[2][4]].count(1) + 1
    l3 = [sq[0][3], sq[0][4], sq[0][2],sq[1][3], sq[1][4], sq[1][2], sq[2][3], sq[2][4]].count(-1)
    if l3 == 0:
        ansdi[k3] += 1
    k4 = [sq[3][0], sq[3][1], sq[3][2],sq[1][0], sq[1][1], sq[1][2], sq[2][0], sq[2][1]].count(1) + 1
    l4 = [sq[3][0], sq[3][1], sq[3][2],sq[1][0], sq[1][1], sq[1][2], sq[2][0], sq[2][1]].count(-1)
    if l4 == 0:
        ansdi[k4] += 1
    k5 = [sq[3][3], sq[3][1], sq[3][2],sq[1][3], sq[1][1], sq[1][2], sq[2][3], sq[2][1]].count(1) + 1
    l5 = [sq[3][3], sq[3][1], sq[3][2],sq[1][3], sq[1][1], sq[1][2], sq[2][3], sq[2][1]].count(-1)
    if l5 == 0:
        ansdi[k5] += 1
    k6 = [sq[3][3], sq[3][4], sq[3][2],sq[1][3], sq[1][4], sq[1][2], sq[2][3], sq[2][4]].count(1) + 1
    l6 = [sq[3][3], sq[3][4], sq[3][2],sq[1][3], sq[1][4], sq[1][2], sq[2][3], sq[2][4]].count(-1)
    if l6 == 0:
        ansdi[k6] += 1
    k7 = [sq[3][0], sq[3][1], sq[3][2],sq[4][0], sq[4][1], sq[4][2], sq[2][0], sq[2][1]].count(1) + 1
    l7 = [sq[3][0], sq[3][1], sq[3][2],sq[4][0], sq[4][1], sq[4][2], sq[2][0], sq[2][1]].count(-1)
    if l7 == 0:
        ansdi[k7] += 1
    k8 = [sq[3][3], sq[3][1], sq[3][2],sq[4][3], sq[4][1], sq[4][2], sq[2][3], sq[2][1]].count(1) + 1
    l8 = [sq[3][3], sq[3][1], sq[3][2],sq[4][3], sq[4][1], sq[4][2], sq[2][3], sq[2][1]].count(-1)
    if l8 == 0:
        ansdi[k8] += 1
    k9 = [sq[3][3], sq[3][4], sq[3][2],sq[4][3], sq[4][4], sq[4][2], sq[2][3], sq[2][4]].count(1) + 1
    l9 = [sq[3][3], sq[3][4], sq[3][2],sq[4][3], sq[4][4], sq[4][2], sq[2][3], sq[2][4]].count(-1)
    if l9 == 0:
        ansdi[k9] += 1
    sq = [[0 for i in range(5)] for j in range(5)]
    chuukainum = 0
for i in range(len(ansdi)):
    if i != 0:
        ansdi[i] = ansdi[i] // i
ansdi[0] = (h - 2) * (w - 2) - sum(ansdi)
for i in range(len(ansdi)):
    print(ansdi[i])