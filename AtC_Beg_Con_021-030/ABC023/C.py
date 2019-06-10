import collections
r, c, k = map(int, input().split())
n = int(input())
rc = []
for i in range(n):#h:高さ
    rc.append([int(m) for m in input().split()])
ans = 0
rcan = [0]*(r + 1)
ccan = [0]*(c + 1)
for i in range(n):
    rcan[rc[i][0]] += 1
    ccan[rc[i][1]] += 1

for i in range(n):#先に被っているところを前計算しておく
    if rcan[rc[i][0]] + ccan[rc[i][1]] - 1 == k:
        ans += 1
    if rcan[rc[i][0]] + ccan[rc[i][1]] == k:
        ans -= 1

rcan.sort()
ccan.sort(reverse=True)
rcan.pop(0)
ccan.pop(-1)

rcandi = collections.Counter(rcan)
ccandi = collections.Counter(ccan)
rcandi = sorted(rcandi.items(), key=lambda x:x[0])
ccandi = sorted(ccandi.items(), reverse=True, key=lambda x:x[0])

"""rk = rcandi.keys()
ck = ccandi.keys()
rv = rcandi.values()
cv = ccandi.values()"""
i = 0
j = 0

while j < len(ccandi) and i < len(rcandi):#被っていない底で計算
    if rcandi[i][0] + ccandi[j][0] > k:
        j += 1
    elif rcandi[i][0] + ccandi[j][0] == k:
        ans += rcandi[i][1] * ccandi[j][1]
        i += 1
        j += 1
    else:
        i += 1
print(ans)