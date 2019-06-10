import collections
s = input()
sdi = collections.Counter(s)

cri = list(sdi.values())[0]
for i in sdi:
    if cri == sdi[i]:
        pass
    else:
        print("No")
        exit()
print("Yes")
