s = input()
k = int(input())

t = len(s)
u = []
u2 = []
"""for i in range(t):
    u.append([])"""
for i in range(5):
    u.append([])

for j in range(5):
    for i in range(t):
        u[j].append([])

for i in range(t):
    u2.append([])


for j in range(5):
    for i in range(t):
        if j == 0:
            if s[i] not in u2[j]:
                u[j][i].append(s[i])
                u2[j].append(s[i])
                u[j][i].append(i)
        elif j == 1:
            if i + 1 < t:
                if s[i] + s[i + 1] not in u2[j] and s[i] + s[i + 1] not in u2[j - 1]:
                    for r in range(j + 1):
                        if u[r][i] == []:
                            u[r][i].append(s[i] + s[i + 1])
                            u2[j].append(s[i] + s[i + 1])
                            u[r][i].append(i)
                            break
        elif j == 2:
            if i + 2 < t:
                if s[i] + s[i + 1] + s[i + 2] not in u2[j] and s[i] + s[i + 1] + s[i + 2] not in u2[j - 1] and s[i] + s[i + 1] + s[i + 2] not in u2[j - 2]:
                    for r in range(j + 1):
                        if u[r][i] == []:
                            u[r][i].append(s[i] + s[i + 1] + s[i + 2])
                            u2[j].append(s[i] + s[i + 1] + s[i + 2])
                            u[r][i].append(i)
                            break
        elif j == 3:
            if i + 3 < t:
                if s[i] + s[i + 1] + s[i + 2] + s[i + 3] not in u2[j] and s[i] + s[i + 1] + s[i + 2] + s[i + 3] not in u2[j - 1] \
                        and s[i] + s[i + 1] + s[i + 2] + s[i + 3] not in u2[j - 2] and s[i] + s[i + 1] + s[i + 2] + s[i + 3] not in u2[j - 3]:
                    for r in range(j + 1):
                        if u[r][i] == []:
                            u[r][i].append(s[i] + s[i + 1] + s[i + 2] + s[i + 3])
                            u2[j].append(s[i] + s[i + 1] + s[i + 2] + s[i + 3])
                            u[r][i].append(i)
                            break
        elif j == 4:
            if i + 4 < t:
                if s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4] not in u2[j] and s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4] not in u2[j - 1]\
                        and s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4] not in u2[j - 2]and s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4] not in u2[j - 3]\
                        and s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4] not in u2[j - 4]:
                    for r in range(j + 1):
                        if u[r][i] == []:
                            u[r][i].append(s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4])
                            u2[j].append(s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4])
                            u[r][i].append(i)
                            break
    """for i in range(t):
    for j in range(k):
        if j == 0:
            u[i].append(s[i])
        elif j == 1:
            u[i].append(s[i] + s[i + 1])
        elif j == 2:
            u[i].append(s[i] + s[i + 1] + s[i + 2])
        elif j == 3:
            u[i].append(s[i] + s[i + 1] + s[i + 2] + s[i + 3])
        elif j == 4:
            u[i].append(s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4])"""
p = [0] * t
n = "z" * 10000
m = -1
l = -1
for i in range(5):
    for j in range(t + 5):
        if j < len(u[0]):
            if u[0][j] != []:
                if u[0][j][0] <= n:
                    n = u[0][j][0]
                    m = u[0][j][1]
                    l = j
    #sorted(u[0])
    if i + 1 == k:
        print(n)
        #print(u[0][0].pop(0))
        exit()
    else:
        u[0].append(u[1 + p[m]][m])
        p[m] += 1
        u[0][l].pop(0)
        u[0][l].pop(0)
        n = "z" * 10000
        m = -1
        l = -1