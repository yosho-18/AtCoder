a, b = map(int, input().split())
s = input()

p = 0
for i in range(len(s)):
    if a == i:
        if s[i] == "-":
            p = 1
    else:
        if s[i] == "-":
            print("No")
            exit()

if p == 0:
    print("No")
else:
    print("Yes")
