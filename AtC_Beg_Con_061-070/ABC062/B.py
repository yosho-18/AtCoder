h, w = map(int, input().split())
#行列
s = []
str_changed = []
for i in range(h):#h:高さ
    s.append([str(m) for m in input().split()])

for i in range(h):
    str_changed.append("".join(s[i]))
for i in range(h + 2):
    if i == 0:
        print("#" * (w + 2))
    elif i == h + 1:
        print("#" * (w + 2))
    else:
        print("#" + str_changed[i - 1] + "#")