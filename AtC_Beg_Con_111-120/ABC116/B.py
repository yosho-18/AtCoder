s = int(input())
k = set()
k.add(s)
a = [s]
a1 = s
i = 2
while True:
    if a[-1] % 2 == 0:
        #k.add(a[-1] // 2)
        a.append(a[-1]//2)

    else:
        #k.add(3 * a[-1] + 1)
        a.append(3*a[-1] + 1)

    if a[-1] in k:
        print(i)
        exit()
    else:
        k.add(a[-1])
        i += 1