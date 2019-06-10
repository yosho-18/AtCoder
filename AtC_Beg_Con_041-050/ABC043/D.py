import collections
s = input()
n = len(s)
k = list(s)
#c = collections.Counter(k)
if n >= 3:
    for i in range(n - 2):
        tmpli = [s[i], s[i + 1], s[i + 2]]
        if len(set(tmpli)) != 3:
            print(i + 1, i + 3)
            exit()
    print(-1, -1)
else:
    if s[0] == s[1]:
        print(1, 2)
    else:
        print(-1, -1)