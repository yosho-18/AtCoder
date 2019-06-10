import numpy as np
print(np.array([1,2]))

import copy
n,m,l = map(int, input().split())
s = []
for i in range(n):
    s.append(input())



t1 = []
for j in range(m):
    if j == 0 or j == m - 1:
        t1.append("#"*m)
    else:
        t1.append("#" + "."*(m - 2) + "#")
t2 = copy.deepcopy(t1)
for j in range(m):
    t2[j] = list(t2[j])
    if j % 4 == 2 and j != (m - 1)//2:
        t2[j][j] = "D"
    elif j % 4 == 0 and j != (m - 1)//2:
        t2[j][m - j - 1] = "T"
    t2[j] = "".join(t2[j])
t3 = []
for j in range(m):
    if j == 0 or j == m - 1:
        t3.append("#"*m)
    else:
        if j % 8 == 4 and j != (m - 1)//2:
            t3.append("#" + "."*((m - 3)//2) + "R" + "."*((m - 3)//2) + "#")
        elif j % 8 == 0 and j != (m - 1)//2:
            t3.append("#" + "." *((m - 3)//2)+ "L" + "." *((m - 3)//2) + "#")
        else:
            t3.append("#" + "." * (m - 2) + "#")
t4 = []
for j in range(m):
    if j == 0 or j == m - 1:
        t4.append("#"*m)
    else:
        if j % 8 == 4 and j != (m - 1)//2:
            t4.append("#" + "."*((m - 3)//2) + "D" + "."*((m - 3)//2) + "#")
        elif j % 8 == 0 and j != (m - 1)//2:
            t4.append("#" + "." *((m - 3)//2)+ "T" + "." *((m - 3)//2) + "#")
        else:
            t4.append("#" + "." * (m - 2) + "#")
t5 = []
for j in range(m):
    if j == 0 or j == m - 1:
        t5.append("#"*m)
    else:
        if j % 8 == 2 and j != (m - 1)//2:
            t5.append("#" + "."*((m - 3)//2) + "R" + "."*((m - 3)//2) + "#")
        elif j % 8 == 6 and j != (m - 1)//2:
            t5.append("#" + "." * ((m - 3) // 2) + "L" + "." * ((m - 3) // 2) + "#")
        elif j % 8 == 4 and j != (m - 1)//2:
            t5.append("#" + "."*((m - 3)//2) + "D" + "."*((m - 3)//2) + "#")
        elif j % 8 == 0 and j != (m - 1)//2:
            t5.append("#" + "." *((m - 3)//2)+ "T" + "." *((m - 3)//2) + "#")
        else:
            t5.append("#" + "." * (m - 2) + "#")
t6 = []
for j in range(m):
    if j == 0 or j == m - 1:
        t6.append("#"*m)
    else:
        if j % 8 == 2 and j != (m - 1)//2:
            t6.append("#" + "." * ((m - 5) // 4) + "D" + "." * ((m - 5) // 4) + "R" + "." * ((m - 5) // 4) + "T" + "." * ((m - 5) // 4) + "#")
        elif j % 8 == 6 and j != (m - 1)//2:
            t6.append("#" + "." * ((m - 5) // 4) + "L" + "." * ((m - 5) // 4) + "T" + "." * ((m - 5) // 4) + "D" + "." * ((m - 5) // 4) + "#")
        elif j % 8 == 4 and j != (m - 1)//2:
            t6.append("#" + "." * ((m - 1) // 14) + "T" + "." * ((m - 5) // 4) + "L" + "." * ((m - 5) // 4) + "R" + "." * ((m - 5) // 4) + "D" + "." * ((m - 2) // 9) + "#")
        elif j % 8 == 0 and j != (m - 1)//2:
            t6.append("#" + "." * ((m - 2) // 9) + "R" + "." * ((m - 5) // 4) + "D" + "." * ((m - 5) // 4) + "L" + "." * ((m - 5) // 4) + "T" + "." * ((m - 1) // 14) + "#")
        else:
            t6.append("#" + "." * (m - 2) + "#")
t7 = []
for j in range(m):
    if j == 0 or j == m - 1:
        t7.append("#"*m)
    else:
        if j % 8 == 2 and j != (m - 1)//2:
            t7.append("#" + "." * ((m - 5) // 4) + "R" + "." * ((m - 5) // 4) + "T" + "." * ((m - 5) // 4) + "L" + "." * ((m - 5) // 4) + "#")
        elif j % 8 == 6 and j != (m - 1)//2:
            t7.append("#" + "." * ((m - 5) // 4) + "L" + "." * ((m - 5) // 4) + "D" + "." * ((m - 5) // 4) + "R" + "." * ((m - 5) // 4) + "#")
        elif j % 8 == 4 and j != (m - 1)//2:
            t7.append("#" + "." * ((m - 1) // 14) + "T" + "." * ((m - 5) // 4) + "D" + "." * ((m - 5) // 4) + "T" + "." * ((m - 5) // 4) + "D" + "." * ((m - 2) // 9) + "#")
        elif j % 8 == 0 and j != (m - 1)//2:
            t7.append("#" + "." * ((m - 2) // 9) + "D" + "." * ((m - 5) // 4) + "T" + "." * ((m - 5) // 4) + "D" + "." * ((m - 5) // 4) + "T" + "." * ((m - 1) // 14) + "#")
        else:
            t7.append("#" + "." * (m - 2) + "#")


v = []
x = []
X = []
co = [0]*(m*m)
cou = [0]*(m*m)


def Search(t):
    X = []
    co = [0] * (m * m)
    cou = [0] * (m * m)
    for i in range(n):
        for j in range(l):
            if j == 0:
                x = [(m - 1)//2, (m - 1)//2]
                v = [-1, 0]
            if s[i][j] == "S":
                subx = [p + q for (p, q) in zip(x, v)]
                if t[subx[0]][subx[1]] == "#":
                    x = x
                #elif t[x[0]][x[1]] == "L":

                #elif t[x[0]][x[1]] == "R":
                elif t[x[0]][x[1]] == "D":
                    subx2 = [p + q * 2 for (p, q) in zip(x, v)]
                    if t[subx2[0]][subx2[1]] == "#":
                        x = [p + q for (p, q) in zip(x, v)]
                    else:
                        x = [p + q * 2 for (p, q) in zip(x, v)]
                elif t[x[0]][x[1]] == "T":
                    subx2t = [p + q * 2 for (p, q) in zip(x, v)]
                    if t[subx2t[0]][subx2t[1]] == "#":
                        x = [p + q for (p, q) in zip(x, v)]
                    else:
                        subx3t = [p + q * 3 for (p, q) in zip(x, v)]
                        if t[subx3t[0]][subx3t[1]] == "#":
                            x = [p + q * 2 for (p, q) in zip(x, v)]
                        else:
                            x = [p + q * 3 for (p, q) in zip(x, v)]
                else:
                    x = [p + q for (p, q) in zip(x, v)]
            elif s[i][j] == "L":
                #if t[x[0]][x[1]] == "#":
                #if t[x[0]][x[1]] == "L":
                #if t[x[0]][x[1]] == "R":
                if t[x[0]][x[1]] == "D":
                    if v == [0, -1]:
                        v = [0, 1]
                    elif v == [-1, 0]:
                        v = [1, 0]
                    elif v == [0, 1]:
                        v = [0, -1]
                    elif v == [1, 0]:
                        v = [-1, 0]
                elif t[x[0]][x[1]] == "T":
                    if v == [0, -1]:
                        v = [-1, 0]
                    elif v == [-1, 0]:
                        v = [0, 1]
                    elif v == [0, 1]:
                        v = [1, 0]
                    elif v == [1, 0]:
                        v = [0, -1]
                else:
                    if v == [0, 1]:
                        v = [-1, 0]
                    elif v == [-1, 0]:
                        v = [0, -1]
                    elif v == [0, -1]:
                        v = [1, 0]
                    elif v == [1, 0]:
                        v = [0, 1]
            elif s[i][j] == "R":
                #if t[x[0]][x[1]] == "#":
                #elif t[x[0]][x[1]] == "L":
                #elif t[x[0]][x[1]] == "R":
                if t[x[0]][x[1]] == "D":
                    if v == [0, -1]:
                        v = [0, 1]
                    elif v == [-1, 0]:
                        v = [1, 0]
                    elif v == [0, 1]:
                        v = [0, -1]
                    elif v == [1, 0]:
                        v = [-1, 0]
                elif t[x[0]][x[1]] == "T":
                    if v == [0, 1]:
                        v = [-1, 0]
                    elif v == [-1, 0]:
                        v = [0, -1]
                    elif v == [0, -1]:
                        v = [1, 0]
                    elif v == [1, 0]:
                        v = [0, 1]
                else:
                    if v == [0, -1]:
                        v = [-1, 0]
                    elif v == [-1, 0]:
                        v = [0, 1]
                    elif v == [0, 1]:
                        v = [1, 0]
                    elif v == [1, 0]:
                        v = [0, -1]
        if x in X:
            co[x[0] * m + x[1]] += 1
        else:
            co[x[0] * m + x[1]] = 1
        X.append(x)

    for c in range(m*m):
        if co[c] == 1:
            cou[c] = 10
        elif co[c] == 2:
            cou[c] = 3
        elif co[c] == 3:
            cou[c] = 1
        else:
            cou[c] = 0
    result = [t, sum(cou)]
    return result

r = []
t1c = Search(t1)[1]
t2c = Search(t2)[1]
t3c = Search(t3)[1]
t4c = Search(t4)[1]
t5c = Search(t5)[1]
t6c = Search(t6)[1]
t7c = Search(t7)[1]
tmax = max(t1c, t2c, t3c, t4c, t5c, t6c, t7c)

T = [t1c, t2c, t3c, t4c, t5c, t6c, t7c]
Tar = [t1,t2,t3,t4,t5,t6,t7]

for u in T:
    if tmax == u:
        r = Search(Tar[T.index(u)])[0]


for j in range(m):
    print(t2[j])



