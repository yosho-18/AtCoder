import collections
w = input()
c = collections.Counter(w)
for i in c:
    if c[i] % 2 != 0:
        print("No")
        exit()
print("Yes")