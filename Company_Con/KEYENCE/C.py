n = int(input())
a = [int(m) for m in input().split()]
b = [int(m) for m in input().split()]
difp = []
difm = []
difmmm = []
difr = []
for i in range(n):
    if a[i] - b[i] >= 0:
        difp.append([a[i] - b[i], i])
    else:
        difm.append([a[i] - b[i], i])
        difmmm.append(1)
        difr.append(abs(a[i] - b[i]))

difp.sort(reverse=True)

if sum(a) < sum(b):
    print(-1)
    exit()
Q = sum(difmmm)
R = sum(difr)
tmp = 0
sign = Q
if difm == []:
    print(0)
    exit()
for i in range(len(difp)):
    tmp += difp[i][0]
    if tmp >= R:
        sign += i + 1
        break

print(sign)