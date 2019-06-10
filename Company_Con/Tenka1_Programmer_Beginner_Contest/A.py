n = input()
j = [str(x) for x in list(str(n))]
k = len(j)

if k == 2:
    print(n)
if k == 3:
    j.reverse()
    print(j[0]+j[1]+j[2])

