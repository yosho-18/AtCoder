d, g = map(int, input().split())

k = [list(map(int, input().split())) for i in range(d)]
l = []
for i in range(1, d + 1):
    l.append(k[-i])
k = l
#k.sort(key=lambda x:(-x[1]))
#A = [0, 1, 2, 3]の部分集合を全て出力する
#A = [0, 1, 2, 3]
combined1 = []
for i in range(d):
    combined1.append([k[i][0] * (d - i) * 100 + k[i][1]])
ansli = []
for i in range(1 << d):
    output = []
    ot = []
    for j in range(d):
        if ((i >> j) & 1) == 1:
            output.append(k[j] + combined1[j])
            ot.append(j)
    #print(output)
    sum = 0
    anscnt = 0
    for m in output:
        sum += m[2]
        anscnt += m[0]
    if sum >= g:
        ansli.append(anscnt)
    else:
        for v in range(d):
            if v not in ot:
                diffyen = g - sum
                tmp = (diffyen + 100 * (d - v) - 1) // (100 * (d - v))
                if tmp < k[v][0]:
                    ansli.append(anscnt + tmp)
                break
print(min(ansli))
"""x = 0
y = 0
z = 0
xcount = 0

#大きいものから順番に
for v in range(d, 0, -1):
    for i in range(1, k[v - 1][0] + 1):
        x += 100 * v
        if i == k[v - 1][0]:
            x += k[v - 1][1]
        xcount += 1
        if x >= g:
            break
    else:
        continue
    break

#print(xcount)

#ボーナスこみでpiだけで賄えるものも個数が最小のもの
m = []
n = []
for j in range(d):
    m.append(100 * (j + 1) * k[j][0] + k[j][1])
    n.append(k[j][0])

p = []
q = []
r = []
for j in range(len(m)):
    if m[j] >= g:
        p.append(n[j])
    else:
        q.append(m[j])
        r.append(n[j])

if p != []:
    ycount = min(p)
else:
    ycount = 1001
#print(ycount)

#ボーナスこみでpiだけで賄えないものと大きいのを足した個数が最小のもの
zcount = 0
add = 0
zar = []
addar = []
h = d - 1
proh = 0

R = sum(r)
hiku = 0
arc = [0 for i in range(d)]
for j in range(len(q)):
    add = q[j]
    comp = q[j]
    for w in range(1, R + 1):
        for u in range(len(q)):
            #qaz = w - hiku
            if h == j:
                h -= 1
            if w == r[u] and j != u:#満タンにぴったり一致するときボーナス分と今までと最大のやつを比較
                if add + 100 * (h + 1) - comp < q[u]:#100 * w * (h + 1)
                    addar.append(q[u])
                    if h == u:
                        proh = 1
                    #100 * d * (w - 1 - pom[pomcount])
                    #pom.append(w - 1)
                    #pomcount += 1
            if u == len(q) - 1 and addar != []:
                add = add + max(addar) - (add - comp) #+ q[j]
                #comp = add
                arc[q.index(max(addar))] += 1
                arc = [0 for i in range(d)]
                arc[q.index(max(addar))] = w
                for m in range(len(q)):
                    if arc[m] < k[m][0] and m != j:
                        h = m
            if u == len(q) - 1 and addar == []:
                add += 100 * (h + 1)
                arc[h] += 1
        zcount += 1
        if arc[h] == k[h][0]:
            hiku += arc[h]
            if proh == 0:
                add += k[h][1]
            h -= 1
            if h == j:
                h -= 1
        proh = 0
        addar = []
        if add >= g:
            zar.append(zcount + r[j])
            zcount = 0

            h = d - 1
            arc = [0 for i in range(d)]
            comp = 0
            hiku = 0
            break

if zar != []:
    coz = min(zar)
else:
    coz = 1001
#print(coz)


print(min(xcount, ycount, coz))"""
