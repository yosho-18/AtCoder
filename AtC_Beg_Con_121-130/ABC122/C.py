n, q = map(int, input().split())
s = input()
lr = []
for i in range(q):#h:高さ
    lr.append([int(m) for m in input().split()])
accntli = [0] * len(s)
accnt = 0
for i in range(1, len(s)):
    accntli[i] = accnt
    if s[i - 1] == "A" and s[i] == "C":
        accnt += 1
        accntli[i] = accnt
ansli = [0] * q
for i in range(q):
    ansli[i] = accntli[lr[i][1] - 1] - accntli[lr[i][0] - 1]
for i in range(q):
    print(ansli[i])