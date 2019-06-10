n = int(input())
#a = [list(map(int, input().split())) + [i] for i in range(n)]
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
a = []
b = []
c = []
for i in range(n):
    a.append([])
    b.append([])
    c.append([])
for i in range(n):
    a[i].append(A[i])
    a[i].append(2)
    b[i].append(B[i])
    b[i].append(1)
    c[i].append(C[i])
    c[i].append(0)
d = a + b + c
d.sort(key=lambda x:(x[0], x[1]))
lenli = []
allli = []
count = 0
for i in range(len(d)):
    if d[i][1] == 2:#a
        if lenli == []:
            lenli.append(1)
        else:
            lenli[-1] += 1
    elif d[i][1] == 1:#b
        if allli == [] and lenli != []:
            allli.append(lenli[-1])
            allli.append(allli[-1])
            lenli.append(lenli[-1])
        elif allli == [] and lenli == []:
            pass
        else:
            allli[-1] += lenli[-1]
            allli.append(allli[-1])
            lenli.append(lenli[-1])
    elif d[i][1] == 0:#c
        if allli == []:
            count += 0
        else:
            count += allli[-2]

print(count)