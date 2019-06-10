w, h, n = map(int, input().split())
c = []
for i in range(n):#h:高さ
    c.append([int(m) for m in input().split()])

sx = [0, w]
sy = [0, h]
for i in range(n):
    if c[i][2] == 1:
        if sx[0] < c[i][0]:
            sx[0] = c[i][0]
    elif c[i][2] == 2:
        if sx[1] > c[i][0]:
            sx[1] = c[i][0]
    elif c[i][2] == 3:
        if sy[0] < c[i][1]:
            sy[0] = c[i][1]
    elif c[i][2] == 4:
        if sy[1] > c[i][1]:
            sy[1] = c[i][1]
if sx[1] <= sx[0] or sy[1] <= sy[0]:
    print(0)
else:
    print((sx[1] - sx[0]) * (sy[1] - sy[0]))