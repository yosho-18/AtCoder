import copy
n, m = map(int, input().split())
s = []
for i in range(m):#h:高さ
    s.append([int(i) for i in input().split()])
    #l2 = l[:]
t = s[:]
t.sort()
t.sort(key=lambda x:(x[0], x[1]))
co = 1
for i in range(m):
    if i != 0:
        if t[i][0] != t[i - 1][0]:
            co = 1
    if t[i][0] <10:
        moji1 = "00000" + str(t[i][0])
    elif t[i][0] <100:
        moji1 = "0000" + str(t[i][0])
    elif t[i][0] <1000:
        moji1 = "000" + str(t[i][0])
    elif t[i][0] <10000:
        moji1 = "00" + str(t[i][0])
    elif t[i][0] <100000:
        moji1 = "0" + str(t[i][0])
    else:
        moji1 = str(t[i][0])

    if co <10:
        moji2 = "00000" + str(co)
    elif co <100:
        moji2 = "0000" + str(co)
    elif co <1000:
        moji2 = "000" + str(co)
    elif co <10000:
        moji2 = "00" + str(co)
    elif co <100000:
        moji2 = "0" + str(co)
    else:
        moji2 = str(co)
    t[i].append(moji1 + moji2)
    co += 1

for i in range(m):
    print(s[i][2])