s = input()
t = input()
u = list(s)
v = list(t)
com1 = []
com1.append(u[0])

p = 0

for i in range(len(u)):
    for j in range(len(u)):
        if j == len(u) - 1:
            u[0] = com1[j]
        else:
            com1.append(u[j + 1])
            u[j + 1] = com1[j]

    if u == v:
        print("Yes")
        p = 1
        break
    com1 = []
    com1.append(u[0])

if p == 0:
    print("No")
