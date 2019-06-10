s = input()
x, y = map(int, input().split())
dpx = set()
dpy = set()
xli = []
yli = []
tmp = 0
d = 0
tcnt = 0
xc = 0
yc = 0

for i in range(len(s)):
    if s[i] == "F":
        if tcnt % 2 == 0:
            xc += 1
        else:
            yc += 1
    else:
        if tcnt % 2 == 0:
            if xc != 0:
                xli.append(xc)
                xc = 0
        else:
            if yc != 0:
                yli.append(yc)
                yc = 0
        tcnt += 1
if tcnt % 2 == 0:
    xli.append(xc)
    xc = 0
else:
    yli.append(yc)
    yc = 0



if s[0] == 'F':
    dpx.add(xli[0])
    xli = xli[1:]
else:
    dpx.add(0)
dpy.add(0)
for a in xli:
    tmp = set()
    for dx in dpx:
        tmp.add(dx + a)
        tmp.add(dx - a)
    dpx = tmp
for a in yli:
    tmp = set()
    for dy in dpy:
        tmp.add(dy + a)
        tmp.add(dy - a)
    dpy = tmp

# print(dpx,dpy)
if x in dpx and y in dpy:
    print("Yes")
else:
    print("No")

"""xcnt = 0
ycnt = 0
tcnt = 0
xsym = 0
ysym = 0
xstep = 0
ystep = 0
start = 0
xli = [0]
yli = [0]
xc = 0
yc = 0
for i in range(len(s)):
    if s[i] == "F":
        if tcnt == 0:
            start += 1
        if tcnt % 2 == 0:
            xcnt += 1
            xc += 1
            if xsym == 0:
                xstep += 1
                xsym = 1
        else:
            ycnt += 1
            yc += 1
            if ysym == 0:
                ystep += 1
                ysym = 1
    else:
        if tcnt % 2 == 0:
            if xc != 0:
                xli.append(xc)
                xc = 0
        else:
            if yc != 0:
                yli.append(yc)
                yc = 0
        tcnt += 1
        xsym = 0
        ysym = 0
if tcnt % 2 == 0:
    xli.append(xc)
    xc = 0
else:
    yli.append(yc)
    yc = 0
#xDPtable
xdp = []
for i in range(xstep + 1):
    xdp.append([])
for i in range(xstep + 1):
    for j in range(2 * xcnt + 1):
        xdp[i].append(False)
#yDPtable
ydp = []
for i in range(ystep + 1):
    ydp.append([])
for i in range(ystep + 1):
    for j in range(2 * ycnt + 1):
        ydp[i].append(False)
#xDp
xdp[0][xcnt] = True
if len(xli) > 1:
    xdp[1][xcnt + start] = True
    for i in range(2, xstep + 1):
        for j in range(2 * xcnt + 1):
            if 0 <= j + xli[i] <= 2 * xcnt and 0 <= j - xli[i] <= 2 * xcnt:
                xdp[i][j] = xdp[i - 1][j + xli[i]] or xdp[i - 1][j - xli[i]]
            elif 0 <= j + xli[i] <= 2 * xcnt:
                xdp[i][j] = xdp[i - 1][j + xli[i]]
            elif 0 <= j - xli[i] <= 2 * xcnt:
                xdp[i][j] = xdp[i - 1][j - xli[i]]
#yDp
ydp[0][ycnt] = True
if len(yli) > 1:
    ydp[1][ycnt + yli[1]] = True
    ydp[1][ycnt - yli[1]] = True
    for i in range(2, ystep + 1):
        for j in range(2 * ycnt + 1):
            if 0 <= j + yli[i] <= 2 * ycnt and 0 <= j - yli[i] <= 2 * ycnt:
                ydp[i][j] = ydp[i - 1][j + yli[i]] or ydp[i - 1][j - yli[i]]
            elif 0 <= j + yli[i] <= 2 * ycnt:
                ydp[i][j] = ydp[i - 1][j + yli[i]]
            elif 0 <= j - yli[i] <= 2 * ycnt:
                ydp[i][j] = ydp[i - 1][j - yli[i]]

if 0 <= xcnt + x <= len(xdp[0]) - 1 and 0 <= ycnt + y <= len(ydp[0]) - 1:
    if xdp[xstep][xcnt + x] == True and ydp[ystep][ycnt + y] == True:
        print("Yes")
    else:
        print("No")
else:
    print("No")"""
