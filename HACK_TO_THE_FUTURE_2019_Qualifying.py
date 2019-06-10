import copy
import random as rd
n,m,l = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

t1 = []
for j in range(m):
    if j == 0 or j == m - 1:
        t1.append("#" * m)
    else:
        t1.append("#" + "." * (m - 2) + "#")
t2 = copy.deepcopy(t1)
for j in range(1, m - 1):
    t2[j] = list(t2[j])
    if j % 4 == 2 and j != (m - 1) // 2:
        t2[j][j] = "D"
    elif j % 4 == 0 and j != (m - 1) // 2:
        t2[j][m - j - 1] = "T"
    t2[j] = "".join(t2[j])
t3 = copy.deepcopy(t1)
for j in range(1, m - 1):
    t3[j] = list(t3[j])
    if j % 8 == 4 and j != (m - 1) // 2:
        t3[j][(m - 1) // 2] = "R"
    elif j % 8 == 0 and j != (m - 1) // 2:
        t3[j][(m - 1) // 2] = "L"
    t3[j] = "".join(t3[j])
t4 = copy.deepcopy(t1)
for j in range(1, m - 1):
    t4[j] = list(t4[j])
    if j % 8 == 4 and j != (m - 1) // 2:
        t4[j][rd.randint(1, m - 2)] = "D"
        t4[j][rd.randint(1, m - 2)] = "T"
    elif j % 8 == 0 and j != (m - 1) // 2:
        t4[j][rd.randint(1, m - 2)] = "T"
        t4[j][rd.randint(1, m - 2)] = "D"
    t4[j] = "".join(t4[j])
t45 = copy.deepcopy(t1)
for j in range(1, m - 1):
    t45[j] = list(t45[j])
    if j % 8 == 4 and j != (m - 1) // 2:
        t45[j][(m - 1) // 2] = "D"
    elif j % 8 == 0 and j != (m - 1) // 2:
        t45[j][(m - 1) // 2] = "T"
    t45[j] = "".join(t45[j])

t5 = copy.deepcopy(t1)
for j in range(1, m - 1):
    t5[j] = list(t5[j])
    if j % 8 == 4 and j != (m - 1) // 2:
        t5[j][(m - 1) // 2] = "R"
    elif j % 8 == 0 and j != (m - 1) // 2:
        t5[j][(m - 1) // 2] = "L"
    elif j % 8 == 6 and j != (m - 1) // 2:
        t5[j][(m - 1) // 2] = "D"
    elif j % 8 == 2 and j != (m - 1) // 2:
        t5[j][(m - 1) // 2] = "T"
    t5[j] = "".join(t5[j])
t6 = []
for j in range(m):
    if j == 0 or j == m - 1:
        t6.append("#" * m)
    else:
        if j % 8 == 2 and j != (m - 1) // 2:
            t6.append(
                "#" + "." * ((m - 5) // 4) + "D" + "." * ((m - 5) // 4) + "R" + "." * ((m - 5) // 4) + "T" + "." * (
                            (m - 5) // 4) + "#")
        elif j % 8 == 6 and j != (m - 1) // 2:
            t6.append(
                "#" + "." * ((m - 5) // 4) + "L" + "." * ((m - 5) // 4) + "T" + "." * ((m - 5) // 4) + "D" + "." * (
                            (m - 5) // 4) + "#")
        elif j % 8 == 4 and j != (m - 1) // 2:
            t6.append(
                "#" + "." * ((m - 1) // 14) + "T" + "." * ((m - 5) // 4) + "L" + "." * ((m - 5) // 4) + "R" + "." * (
                            (m - 5) // 4) + "D" + "." * ((m - 2) // 9) + "#")
        elif j % 8 == 0 and j != (m - 1) // 2:
            t6.append(
                "#" + "." * ((m - 2) // 9) + "R" + "." * ((m - 5) // 4) + "D" + "." * ((m - 5) // 4) + "L" + "." * (
                            (m - 5) // 4) + "T" + "." * ((m - 1) // 14) + "#")
        else:
            t6.append("#" + "." * (m - 2) + "#")
t7 = []
for j in range(m):
    if j == 0 or j == m - 1:
        t7.append("#" * m)
    else:
        if j % 8 == 2 and j != (m - 1) // 2:
            t7.append(
                "#" + "." * ((m - 5) // 4) + "R" + "." * ((m - 5) // 4) + "T" + "." * ((m - 5) // 4) + "L" + "." * (
                            (m - 5) // 4) + "#")
        elif j % 8 == 6 and j != (m - 1) // 2:
            t7.append(
                "#" + "." * ((m - 5) // 4) + "L" + "." * ((m - 5) // 4) + "D" + "." * ((m - 5) // 4) + "R" + "." * (
                            (m - 5) // 4) + "#")
        elif j % 8 == 4 and j != (m - 1) // 2:
            t7.append(
                "#" + "." * ((m - 1) // 14) + "T" + "." * ((m - 5) // 4) + "D" + "." * ((m - 5) // 4) + "T" + "." * (
                            (m - 5) // 4) + "D" + "." * ((m - 2) // 9) + "#")
        elif j % 8 == 0 and j != (m - 1) // 2:
            t7.append(
                "#" + "." * ((m - 2) // 9) + "D" + "." * ((m - 5) // 4) + "T" + "." * ((m - 5) // 4) + "D" + "." * (
                            (m - 5) // 4) + "T" + "." * ((m - 1) // 14) + "#")
        else:
            t7.append("#" + "." * (m - 2) + "#")

t71 = copy.deepcopy(t1)
for j in range(1, m - 1):
    t71[j] = list(t71[j])
    if j % 8 == 2 and j != (m - 1) // 2:
        t71[j][rd.randint(1, m - 2)] = "D"
        t71[j][rd.randint(1, m - 2)] = "R"
    elif j % 8 == 6 and j != (m - 1) // 2:
        t71[j][rd.randint(1, m - 2)] = "L"
        t71[j][rd.randint(1, m - 2)] = "T"
    elif j % 8 == 4 and j != (m - 1) // 2:
        t71[j][rd.randint(1, m - 2)] = "L"
        t71[j][rd.randint(1, m - 2)] = "D"
    elif j % 8 == 0 and j != (m - 1) // 2:
        t71[j][rd.randint(1, m - 2)] = "T"
        t71[j][rd.randint(1, m - 2)] = "R"
    elif j == (m - 1) // 2:
        t71[j][(m - 1) // 2 - 1] = "L"
        t71[j][(m - 1) // 2 + 1] = "R"
    t71[j] = "".join(t71[j])


t72 = copy.deepcopy(t1)
for j in range(1, m - 1):
    t72[j] = list(t72[j])
    if j % 8 == 3 and j != (m - 1) // 2:
        t72[j][rd.randint(1, m - 2)] = "D"
        t72[j][rd.randint(1, m - 2)] = "R"
        t72[j][rd.randint(1, m - 2)] = "T"
    elif j % 8 == 7 and j != (m - 1) // 2:
        t72[j][rd.randint(1, m - 2)] = "L"
        t72[j][rd.randint(1, m - 2)] = "T"
        t72[j][rd.randint(1, m - 2)] = "D"
    elif j % 8 == 5 and j != (m - 1) // 2:
        t72[j][rd.randint(1, m - 2)] = "T"
        t72[j][rd.randint(1, m - 2)] = "L"
        t72[j][rd.randint(1, m - 2)] = "R"
        t72[j][rd.randint(1, m - 2)] = "D"
    elif j % 8 == 1 and j != (m - 1) // 2:
        t72[j][rd.randint(1, m - 2)] = "T"
        t72[j][rd.randint(1, m - 2)] = "L"
        t72[j][rd.randint(1, m - 2)] = "R"
        t72[j][rd.randint(1, m - 2)] = "D"
    t72[j] = "".join(t72[j])

t73 = copy.deepcopy(t1)
for j in range(1, m - 1):
    t73[j] = list(t73[j])
    if j % 8 == 3 and j != (m - 1) // 2:
        t73[j][rd.randint(1, m - 2)] = "D"
        t73[j][rd.randint(1, m - 2)] = "#"
        t73[j][rd.randint(1, m - 2)] = "T"
    elif j % 8 == 7 and j != (m - 1) // 2:
        t73[j][rd.randint(1, m - 2)] = "#"
        t73[j][rd.randint(1, m - 2)] = "T"
        t73[j][rd.randint(1, m - 2)] = "D"
    elif j % 8 == 5 and j != (m - 1) // 2:
        t73[j][rd.randint(1, m - 2)] = "L"
        t73[j][rd.randint(1, m - 2)] = "R"
    elif j % 8 == 1 and j != (m - 1) // 2:
        t73[j][rd.randint(1, m - 2)] = "T"
        t73[j][rd.randint(1, m - 2)] = "D"
    elif j % 8 == 2 and j != (m - 1) // 2:
        t73[j][rd.randint(1, m - 2)] = "D"
        t73[j][rd.randint(1, m - 2)] = "R"
    elif j % 8 == 6 and j != (m - 1) // 2:
        t73[j][rd.randint(1, m - 2)] = "L"
        t73[j][rd.randint(1, m - 2)] = "T"
    elif j % 8 == 4 and j != (m - 1) // 2:
        t73[j][rd.randint(1, m - 2)] = "L"
        t73[j][rd.randint(1, m - 2)] = "D"
    elif j % 8 == 0 and j != (m - 1) // 2:
        t73[j][rd.randint(1, m - 2)] = "T"
        t73[j][rd.randint(1, m - 2)] = "R"
    elif j == (m - 1) // 2:
        t73[j][(m - 1) // 2 - 1] = "L"
        t73[j][(m - 1) // 2 + 1] = "R"
    t73[j] = "".join(t73[j])
t74 = copy.deepcopy(t1)
for j in range(1, m - 1):
    t74[j] = list(t74[j])
    if j % 8 == 3 and j != (m - 1) // 2:
        t74[j][rd.randint(1, m - 2)] = "D"
    elif j % 8 == 7 and j != (m - 1) // 2:
        t74[j][rd.randint(1, m - 2)] = "T"
    elif j % 8 == 5 and j != (m - 1) // 2:
        t74[j][rd.randint(1, m - 2)] = "L"
        t74[j][rd.randint(1, m - 2)] = "R"
    elif j % 8 == 1 and j != (m - 1) // 2:
        t74[j][rd.randint(1, m - 2)] = "T"
        t74[j][rd.randint(1, m - 2)] = "D"
    elif j % 8 == 2 and j != (m - 1) // 2:
        t74[j][rd.randint(1, m - 2)] = "D"
        t74[j][rd.randint(1, m - 2)] = "R"
    elif j % 8 == 6 and j != (m - 1) // 2:
        t74[j][rd.randint(1, m - 2)] = "L"
        t74[j][rd.randint(1, m - 2)] = "T"
    elif j % 8 == 4 and j != (m - 1) // 2:
        t74[j][rd.randint(1, m - 2)] = "L"
        t74[j][rd.randint(1, m - 2)] = "D"
    elif j % 8 == 0 and j != (m - 1) // 2:
        t74[j][rd.randint(1, m - 2)] = "T"
        t74[j][rd.randint(1, m - 2)] = "R"
    elif j == (m - 1) // 2:
        t74[j][(m - 1) // 2 - 1] = "L"
        t74[j][(m - 1) // 2 + 1] = "R"
    t74[j] = "".join(t74[j])
t75 = copy.deepcopy(t1)
for j in range(1, m - 1):
    t75[j] = list(t75[j])
    if j % 8 == 3 and j != (m - 1) // 2:
        t75[j][rd.randint(1, m - 2)] = "D"
        t75[j][rd.randint(1, m - 2)] = "T"
    elif j % 8 == 7 and j != (m - 1) // 2:
        t75[j][rd.randint(1, m - 2)] = "T"
        t75[j][rd.randint(1, m - 2)] = "D"
    elif j % 8 == 5 and j != (m - 1) // 2:
        t75[j][rd.randint(1, m - 2)] = "L"
        t75[j][rd.randint(1, m - 2)] = "R"
    elif j % 8 == 1 and j != (m - 1) // 2:
        t75[j][rd.randint(1, m - 2)] = "T"
        t75[j][rd.randint(1, m - 2)] = "D"
    elif j % 8 == 2 and j != (m - 1) // 2:
        t75[j][rd.randint(1, m - 2)] = "D"
        t75[j][rd.randint(1, m - 2)] = "R"
    elif j % 8 == 6 and j != (m - 1) // 2:
        t75[j][rd.randint(1, m - 2)] = "L"
        t75[j][rd.randint(1, m - 2)] = "T"
    elif j % 8 == 4 and j != (m - 1) // 2:
        t75[j][rd.randint(1, m - 2)] = "L"
        t75[j][rd.randint(1, m - 2)] = "D"
    elif j % 8 == 0 and j != (m - 1) // 2:
        t75[j][rd.randint(1, m - 2)] = "T"
        t75[j][rd.randint(1, m - 2)] = "R"
    elif j == (m - 1) // 2:
        t75[j][(m - 1) // 2 - 1] = "L"
        t75[j][(m - 1) // 2 + 1] = "R"
    t75[j] = "".join(t75[j])
t76 = copy.deepcopy(t1)
for j in range(1, m - 1):
    t76[j] = list(t76[j])
    if j % 11 == 3 and j != (m - 1) // 2:
        t76[j][rd.randint(1, m - 2)] = "D"
        t76[j][rd.randint(1, m - 2)] = "T"
    elif j % 11 == 7 and j != (m - 1) // 2:
        t76[j][rd.randint(1, m - 2)] = "T"
        t76[j][rd.randint(1, m - 2)] = "D"
    elif j % 11 == 10 and j != (m - 1) // 2:
        t76[j][rd.randint(1, m - 2)] = "L"
        t76[j][rd.randint(1, m - 2)] = "R"
    elif j % 11 == 1 and j != (m - 1) // 2:
        t76[j][rd.randint(1, m - 2)] = "T"
        t76[j][rd.randint(1, m - 2)] = "D"
    elif j % 11 == 2 and j != (m - 1) // 2:
        t76[j][rd.randint(1, m - 2)] = "D"
    elif j % 11 == 6 and j != (m - 1) // 2:
        t76[j][rd.randint(1, m - 2)] = "T"
    elif j % 11 == 4 and j != (m - 1) // 2:
        t76[j][rd.randint(1, m - 2)] = "D"
    elif j % 11 == 0 and j != (m - 1) // 2:
        t76[j][rd.randint(1, m - 2)] = "R"
    elif j == (m - 1) // 2:
        t76[j][(m - 1) // 2 - 1] = "L"
        t76[j][(m - 1) // 2 + 1] = "R"
    t76[j] = "".join(t76[j])
t77 = copy.deepcopy(t1)
for j in range(1, m - 1):
    t77[j] = list(t76[j])
    if j % 11 == 3 and j != (m - 1) // 2:
        t77[j][rd.randint(1, m - 2)] = "D"
        t77[j][rd.randint(1, m - 2)] = "T"
    elif j % 11 == 7 and j != (m - 1) // 2:
        t77[j][rd.randint(1, m - 2)] = "D"
    elif j % 11 == 10 and j != (m - 1) // 2:
        t77[j][rd.randint(1, m - 2)] = "L"
    elif j % 11 == 1 and j != (m - 1) // 2:
        t77[j][rd.randint(1, m - 2)] = "T"
    elif j % 11 == 2 and j != (m - 1) // 2:
        t77[j][rd.randint(1, m - 2)] = "D"
    elif j % 11 == 6 and j != (m - 1) // 2:
        t77[j][rd.randint(1, m - 2)] = "T"
    elif j % 11 == 4 and j != (m - 1) // 2:
        t77[j][rd.randint(1, m - 2)] = "D"
    elif j % 11 == 0 and j != (m - 1) // 2:
        t77[j][rd.randint(1, m - 2)] = "R"
    elif j == (m - 1) // 2:
        t77[j][(m - 1) // 2 - 1] = "L"
        t77[j][(m - 1) // 2 + 1] = "R"
    t77[j] = "".join(t77[j])

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
t71c = Search(t71)[1]
t72c = Search(t72)[1]
t73c = Search(t73)[1]
t74c = Search(t74)[1]
t75c = Search(t75)[1]
t76c = Search(t76)[1]
t77c = Search(t77)[1]
t45c = Search(t45)[1]
tmax = max(t1c, t2c,t3c, t45c, t4c, t5c, t6c, t7c, t71c, t72c, t73c, t74c, t75c, t76c, t77c)

T = [t1c, t2c,t3c, t45c, t4c, t5c, t6c, t7c, t71c, t72c, t73c, t74c, t75c, t76c, t77c]
Tar = [t1,t2,t3,t45,t4,t5,t6,t7,t71,t72, t73, t74, t75, t76, t77]

for u in T:
    if tmax == u:
        r = Search(Tar[T.index(u)])[0]


for j in range(m):
    print(r[j])



