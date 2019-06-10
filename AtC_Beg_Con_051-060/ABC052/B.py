n = int(input())
s = input()
x = 0
xli = []
xli.append(0)
for i in range(n):
    if s[i] == "I":
        x += 1
    else:
        x -= 1
    xli.append(x)
print(max(xli))