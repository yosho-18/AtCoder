n, k = map(int, input().split())
a = input().split()
d = [int(m) for m in a]
aset = set(a)
i = n
while True:
    k = list(str(i))
    klen = len(k)
    for j in range(klen):
        if k[j] in aset:
            i += 10 ** (klen - j - 1)
            i -= i % (10 ** (klen - j - 1))
            break
    else:
        print(i)
        exit()

"""1000 8
1 2 4 5 6 7 8 9"""