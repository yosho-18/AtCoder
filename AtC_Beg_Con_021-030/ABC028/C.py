import itertools
a, b, c, d, e = map(int, input().split())
numli = [a, b, c, d, e]
ansset = set()
for i in itertools.combinations(numli, 3):
    tmp = i[0] + i[1] + i[2]
    ansset.add(tmp)

ansli = list(ansset)
ansli.sort(reverse=True)

print(ansli[2])