n = int(input())
s = input()
c = 0
sl = 0
lli =[]
rli =[]
k = 0
j = 0
for i in range(n):
    if i == 0:
        if s[i] == "(":
            lli.append(1)
            j = 1
        else:
            sl += 1
            k = 1
    elif s[i] == "(":
        k = 0
        if c == 1 or j == 1:
            lli[-1] += 1
            j = 0
        else:
            lli.append(1)
        c = 1
    else:
        if k == 1:
            sl += 1
        elif c == 2:
            if lli[-1] > 0:
                lli[-1] -= 1
            else:
                for v in range(len(lli)):
                    if lli[-1-v] > 0:
                        lli[-1-v] -= 1
                        break
                else:
                    rli[-1] += 1
        else:
            rli.append(0)
            lli[-1] -= 1
        c = 2

if sum(rli) + sl > 0 and sum(lli) > 0:
    print("(" * (sum(rli) + sl) + s + ")" * sum(lli))
elif sum(rli) + sl <= 0 and sum(lli) > 0:
    print(s + ")" * sum(lli))
elif sum(rli) + sl > 0 and sum(lli) <= 0:
    print("(" * (sum(rli) + sl) + s)
else:
    print(s)