s = input()
n = len(s)
zc = 0
oc = 0
for i in range(n):
    if s[i] == "0":
        zc += 1
    else:
        oc += 1
print(n - abs(zc - oc))