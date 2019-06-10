a, b = map(int, input().split())
a = str(a)
b = str(b)
count = 0
c = int(a)
d = int(b)
for i in range(c, d + 1):
    i = str(i)
    if i[0] == i[4] and i[1] == i[3]:
        count += 1
print(count)