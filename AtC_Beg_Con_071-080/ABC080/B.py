n = input()
s = list(n)
f = 0
for i in s:
    f += int(i)
print("Yes" if int(n) % f == 0 else "No")