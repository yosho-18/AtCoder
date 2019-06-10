s = input()
t = list(s)
x = 0
y = 0
z = 0
r = []

if t[0] == "A":
    x = 1

r.append(t[1])
r.append(t[len(t) - 1])

for i in range(2, len(t) - 1):
    if t[i] == "C":
        y += 1
    else:
        r.append(t[i])

for j in r:
    if j.isupper():
        z = 1

if x == 1 and y == 1 and z == 0:
    print("AC")
else:
    print("WA")
