n = int(input())
s = input()
t = list(s)

s1 = []
s2 = []

for i in range(n):
    s1.append([])
    s2.append([])

for i in range(n):
    for j in range(n):
        if j < i:
            s1[i].append(t[j])
        else:
            s2[i].append(t[j])

count = 0
com = []
slv = []

for i in range(n):
    for j in range(i):
        if s1[i][j] in s2[i] and s1[i][j] not in com:
            count += 1
            com.append(s1[i][j])
    slv.append(count)
    count = 0
    com = []

print(max(slv))


