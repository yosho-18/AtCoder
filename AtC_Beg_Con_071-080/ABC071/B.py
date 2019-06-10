import collections
s = input()
alpha = [chr(i) for i in range(ord('a'), ord('z')+1)]
c = collections.Counter(s)
for al in alpha:
    if al not in c:
        print(al)
        exit()
print("None")
