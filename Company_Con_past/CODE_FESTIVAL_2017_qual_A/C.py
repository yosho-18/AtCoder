#Counter
import collections
h, w = map(int, input().split())
a = []
for i in range(h):
    a.append(input())


palinmoji = ""
for i in range(h):
    palinmoji += a[i]

palinli = collections.Counter(palinmoji)

if h % 2 == 0 and w % 2 == 0:
    for i in palinli:
        if palinli[i] % 4 != 0:
            print("No")
            exit()
    print("Yes")
elif h % 2 == 0 and w % 2 != 0:
    cnt = 0
    for i in palinli:
        if palinli[i] % 4 != 0:
            if palinli[i] % 2 != 0:
                print("No")
                exit()
            if palinli[i] % 2 == 0:
                cnt += 1
            if cnt == h // 2 + 1:
                print("No")
                exit()
    print("Yes")
elif h % 2 != 0 and w % 2 == 0:
    cnt = 0
    for i in palinli:
        if palinli[i] % 4 != 0:
            if palinli[i] % 2 != 0:
                print("No")
                exit()
            if palinli[i] % 2 == 0:
                cnt += 1
            if cnt == w // 2 + 1:
                print("No")
                exit()
    print("Yes")
elif h % 2 != 0 and w % 2 != 0:
    cnt = 0
    onecnt = 0
    for i in palinli:
        if palinli[i] % 4 != 0:
            if palinli[i] % 2 != 0:
                onecnt += 1
                if (palinli[i] - 1) % 4 != 0 and onecnt == 1:
                    cnt += 1
                    pass
                elif onecnt == 2:
                    print("No")
                    exit()
            if palinli[i] % 2 == 0:
                cnt += 1
    if cnt >= h // 2 + w // 2 + 1:
        print("No")
        exit()
    print("Yes")
