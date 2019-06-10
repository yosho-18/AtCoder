n, k = map(int, input().split())
d = []
for i in range(n):
    d.append(input())
# [d1, d2, d3, ..., dN]
s = [int(m) for m in d]#int型に直す

ans = 0
ansstr = 1
tmpans = 0
p = 0
if s.count(0) > 0:
    print(n)
    exit()
for i in range(n):
    if i != 0:
        if p >= i:
            ansstr //= s[i - 1]
            tmpans = tmpans - 1
    if p <= i:
        p = i
        tmpans = 0
    for j in range(p, n):
        ansstr *= s[j]
        if ansstr > k:
            ansstr //= s[j]
            ans = max(ans, tmpans)
            p = j
            break
        else:
            tmpans += 1
            if j == n - 1:
                ans = max(ans, tmpans)
                print(ans)
                exit()
print(ans)