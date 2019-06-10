n = int(input())
s = input()
ans = 0
an = 0
for i in range(n):
    if s[i] == "R":
        ans += 1
    else:
        an += 1
if ans > an:
    print("Yes")
else:
    print("No")