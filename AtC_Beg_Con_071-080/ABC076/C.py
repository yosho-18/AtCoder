import copy as cp
s = input()
t = input()
u = list(s)
v = list(t)
w = cp.deepcopy(u)
p = 0
q = 0
for h in range(len(u) - 1, -1, -1):
    if q == 1:
        break
    if v[-1] == u[h]:
        #w[i] = v[0]
        for j in range(len(v)):
            if (v[-1 - j] == u[h - j]) and h - j >= 0:
                pass
                if j == len(v) - 1:
                    #for k in range(len(v)):
                        #w[h - k] = v[-1 - k]
                    q = 1
                    p = 1
            else:
                break
if q == 0:
    for i in range(len(u) - 1, -1, -1):
        if p == 1:
            break
        if v[-1] == u[i] or "?" == u[i]:
            #w[i] = v[0]
            for j in range(len(v)):
                if (v[-1 - j] == u[i - j] or "?" == u[i - j]) and i - j >= 0:
                    pass
                    if j == len(v) - 1:
                        for k in range(len(v)):
                            w[i - k] = v[-1 - k]
                        p = 1
                else:
                    break

if p == 1:
    for m in range(len(u)):
        if w[m] == "?":
            w[m] = "a"
    print("".join(w))
if p == 0:
    print("UNRESTORABLE")