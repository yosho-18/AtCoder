import math
h, w = map(int, input().split())
if (h * w) % 3 == 0:
    print(0)
    exit()
if h % 3 == 1:
    k = h + 2
if h % 3 == 2:
    k = h + 1
if w % 3 == 1:
    v = w + 2
if w % 3 == 2:
    v = w + 1

if h % 2 == 0:
    m = h
if h % 2 == 1:
    m = h + 1
if w % 2 == 0:
    u = w
if w % 2 == 1:
    u = w + 1

s11 = k // 3 * w
s12 = (h - k // 3) * (math.floor(w / 2))
s13 = (h - k // 3) * (math.ceil(w/ 2))
s1 = max(s11, s12, s13) - min(s11, s12, s13)

t11 = (k // 3 - 1) * w
t12 = (h - k // 3 + 1) * (math.floor(w / 2))
t13 = (h - k // 3 + 1) * (math.ceil(w/ 2))
t1 = max(t11, t12, t13) - min(t11, t12, t13)

s21 = (k // 3) * w
s22 = (k // 3 - 1) * w
if h % 3 == 1:
    s23 = (k // 3 - 1) * w
else:
    s23 = (k // 3) * w
s2 = max(s21, s22, s23) - min(s21, s22, s23)

s31 = v // 3 * h
s32 = (w - v // 3) * (math.floor(h / 2))
s33 = (w - v // 3) * (math.ceil(h / 2))
s3 = max(s31, s32, s33) - min(s31, s32, s33)

t31 = (v // 3 - 1) * h
t32 = (w - v // 3 + 1) * (math.floor(h / 2))
t33 = (w - v // 3 + 1) * (math.ceil(h / 2))
t3 = max(t31, t32, t33) - min(t31, t32, t33)

s41 = (v // 3) * h
s42 = (v // 3 - 1) * h
if h % 3 == 1:
    s43 = (v // 3 - 1) * h
else:
    s43 = (v // 3) * h
s4 = max(s41, s42, s43) - min(s41, s42, s43)

print(min(s1, s2, s3, s4, t1, t3))