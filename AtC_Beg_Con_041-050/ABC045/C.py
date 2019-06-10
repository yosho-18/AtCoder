import itertools
s = input()
s2 = s

t = []
t2 = []
u = []
ans = int(s)
p = 0
digit = 0
for i in range(len(s)):
    u.append([])
for i in range(len(s)):
    t.append(i)
    if i != len(s) - 1:
        t2.append(i)
    u[i].append(i)
    u[i].append(s[i])
addli = []
for k in range(1, len(s)):
    for balls in itertools.combinations(t2, k):
        for call in balls:
            if p != 0:
                call = call - digit
            r2 = s2
            s3 = r2[:call + 1]
            s2 = r2[call + 1:]
            ss3 = s3
            addli.append(int(ss3))
            p += 1
            digit += len(s3)
            if len(balls) == p:
                addli.append(int(s2))
        ans += sum(addli)

        addli = []
        p = 0
        s2 = s
        digit = 0
print(ans)