import collections
s = input()
c = collections.Counter(s)
ans = 0
p = 0
for i in c:
    if c[i] % 2 == 0:
        ans += c[i]
        c[i] = 0
    else:
        if p == 0:
            ans += c[i]
            c[i] = 0
            p = 1
        elif p == 1:
            ans += c[i] - 1
            c[i] = 1
ans2 = 0
for i in c:
    ans2 += c[i]

print(ans ** 2 + ans2)