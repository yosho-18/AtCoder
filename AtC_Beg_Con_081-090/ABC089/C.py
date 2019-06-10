n = int(input())
s = []
for i in range(n):
    s.append(input())
# [d1, d2, d3, ..., dN]
m = []
a = []
r = []
c = []
h = []
for i in s:
    if i[0] == "M":
        m.append(i)
    elif i[0] == "A":
        a.append(i)
    elif i[0] == "R":
        r.append(i)
    elif i[0] == "C":
        c.append(i)
    elif i[0] == "H":
        h.append(i)

ml = len(m)
al = len(a)
rl = len(r)
cl = len(c)
hl = len(h)

count1 = ml*al*rl + ml*al*cl + ml*al*hl + ml*rl*cl + ml*rl*hl + ml*cl*hl + al*rl*cl + al*rl*hl + al*cl*hl + rl*cl*hl
print(count1)