n = int(input())
s = input()
y = "b"
abcli = [y]
x = ""
z = ""
for i in range(1, 101):
    if i % 3 == 1:
        x += "a"
        z += "c"
        abcli.append(x[::-1] + y + z)
    elif i % 3 == 2:
        x += "c"
        z += "a"
        abcli.append(x[::-1] + y + z)
    elif i % 3 == 0:
        x += "b"
        z += "b"
        abcli.append(x[::-1] + y + z)

for i in range(101):
    if abcli[i] == s:
        print(i)
        exit()
print(-1)