h,w,d = map(int, input().split())
a = []

for i in range(h):#h:高さ
    a.append([int(m) for m in input().split()])

q = int(input())
lr = []
for i in range(q):#h:高さ
    lr.append([int(m) for m in input().split()])

rea = []
for i in range(h * w):
    rea.append([])


for i in range(h):
    for j in range(w):
        rea[w*i+j].append(a[i][j])
        rea[w*i+j].append(i)
        rea[w*i+j].append(j)

rea.sort()

pre = []
for i in range(h*w):
    pre.append([])
p = 0
for i in range(h):
    if p == 1:
        break
    for j in range(w):
        if w * i + j + 1 <= d:
            lmn = 0
            pre[w * i + j].append(lmn)

            for k in range(0,h*w,d):
                if w*i+j + d + k < h*w:
                    lmn += abs(rea[w*i+j + k][1] - rea[w*i+j+d + k][1]) + abs(rea[w*i+j + k][2]- rea[w*i+j+d + k][2])
                    pre[w*i+j].append(lmn)
                else:
                    break
        else:
            p = 1
            break

for i in range(q):
    print(pre[(lr[i][0] - 1) % d][(lr[i][1] - 1)//d] - pre[(lr[i][0] - 1) % d][(lr[i][0] - 1)//d])
