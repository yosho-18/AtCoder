n = int(input())
t = [int(m) for m in input().split()]
T = sum(t)
v = [int(m) for m in input().split()]
v.append(0)
#maxv[i]
maxv=[0]
#maxv = []
i = 0
cnt = 0
#for i in range(2*T):
while i < n:
    cnt += 0.5
    if t[i] == cnt:
        maxv.append(min(v[i],v[i+1]))
        i += 1
        cnt = 0
    else:
        maxv.append(v[i])
maxv[0] = 0
#maxv.append(0)
maxv[2*T] = 0

for i in range(1, 2*T+1):
    maxv[i] = min(maxv[i], maxv[i - 1] + 0.5)

for i in range(2*T-1, -1, -1):
    maxv[i] = min(maxv[i], maxv[i + 1] + 0.5)

ans = 0
for i in range(1, 2*T+1):
    ans += (maxv[i - 1] + maxv[i]) * 0.5 * 0.5

print(ans)