n, k = map(int, input().split())
s = []
for i in range(n):#h:高さ
    s.append([int(m) for m in input().split()])
s.sort(key=lambda x:(x[0]))
count = 0
recli = []
if k == 2:
    for i in range(n):
        for j in range(i + 1, n):
            larx = max(s[i][0], s[j][0])
            smax = min(s[i][0], s[j][0])
            lary = max(s[i][1], s[j][1])
            smay = min(s[i][1], s[j][1])
            rec = (larx - smax) * (lary - smay)
            for l in range(n):
                if smax <= s[l][0] <= larx and smay <= s[l][1] <= lary:
                    count += 1
            if count >= k:
                recli.append(rec)
            count = 0

elif k == 3:
    for i in range(n):
        for j in range(i + 1, n):
            for p in range(j + 1, n):
                larx = max(s[i][0], s[j][0], s[p][0])
                smax = min(s[i][0], s[j][0], s[p][0])
                lary = max(s[i][1], s[j][1], s[p][1])
                smay = min(s[i][1], s[j][1], s[p][1])
                rec = (larx - smax) * (lary - smay)
                for l in range(n):
                    if smax <= s[l][0] <= larx and smay <= s[l][1] <= lary:
                        count += 1
                if count >= k:
                    recli.append(rec)
                count = 0
else:
    for i in range(n):
        for j in range(i + 1, n):
            for p in range(j + 1, n):
                for q in range(p + 1, n):
                    larx = max(s[i][0], s[j][0], s[p][0], s[q][0])
                    smax = min(s[i][0], s[j][0], s[p][0], s[q][0])
                    lary = max(s[i][1], s[j][1], s[p][1], s[q][1])
                    smay = min(s[i][1], s[j][1], s[p][1], s[q][1])
                    rec = (larx - smax) * (lary - smay)
                    if q - i + 1 >= k:
                        if (recli == []) or (recli != [] and rec < min(recli)):
                            for l in range(i, q + 1):
                                if smax <= s[l][0] <= larx and smay <= s[l][1] <= lary:
                                    count += 1
                            if count >= k:
                                recli.append(rec)
                            count = 0

print(min(recli))