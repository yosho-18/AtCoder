a = int(input())
s = input()
pc = a
mc = 0
if a == 0:
    print("Yes")
    exit()
for i in range(len(s)):
    if s[i] == "+":
        pc += 1
    else:
        mc += 1
    if pc == mc:
        print("Yes")
        exit()
print("No")