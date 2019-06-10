n = input()
s = [int(i) for i in n]
v = 0
w = ''
for p in range(2):
    if p == 0:
        v = s[0] + s[1]
        w = n[0] + "+" + n[1]
    else:
        v = s[0] - s[1]
        w = n[0] + "-" + n[1]
    for q in range(2):
        if q == 0 and p == 0:
            v += +s[2]
            w += "+" + n[2]
        elif q == 1 and p == 0:
            v = s[0] + s[1] - s[2]
            w = n[0] + "+" + n[1] + "-" + n[2]
        elif q == 0 and p == 1:
            v += +s[2]
            w += "+" + n[2]
        elif q == 1 and p == 1:
            v = s[0] - s[1] - s[2]
            w = n[0] + "-" + n[1] + "-" + n[2]
        for r in range(2):
            if r == 0:
                if v + s[3] == 7:
                    print(w + "+" + n[3] + "=7")
                    exit()
            else:
                if v - s[3] == 7:
                    print(w + "-" + n[3] + "=7")
                    exit()