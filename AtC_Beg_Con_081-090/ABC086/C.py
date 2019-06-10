n = int(input())
s = []
for i in range(n):#h:高さ
    s.append([int(m) for m in input().split()])

for i in range(n):
    if i == 0:
        if not(-s[i][1] - s[i][0] <= s[i][2] <= -s[i][1] + s[i][0] and s[i][1] - s[i][0] <= s[i][2] <= s[i][1] + s[i][0]):
            print("No")
            exit()
        else:
            if (s[i][0] % 2 == 0 and (s[i][1] + s[i][2]) % 2 != 0) or (s[i][0] % 2 != 0 and (s[i][1] + s[i][2]) % 2 == 0):
                print("No")
                exit()
    else:
        if not(-s[i][1] + s[i - 1][1] + s[i - 1][2] - (s[i][0] - s[i - 1][0]) <= s[i][2] <= -s[i][1] + s[i - 1][1] + s[i - 1][2] + (s[i][0] - s[i - 1][0])\
            and s[i][1] - s[i - 1][1] + s[i - 1][2] - (s[i][0] - s[i - 1][0]) <= s[i][2] <= s[i][1] - s[i - 1][1] + s[i - 1][2] + (s[i][0] - s[i - 1][0])):
            print("No")
            exit()
        else:
            if (s[i][0] % 2 == 0 and (s[i][1] + s[i][2]) % 2 != 0) or (s[i][0] % 2 != 0 and (s[i][1] + s[i][2]) % 2 == 0):
                print("No")
                exit()

print("Yes")


"""for i in range(n):
    if i == 0:
        if not(0 - s[i][0] <= s[i][1] <= 0 + s[i][0]) or not(0 - s[i][0] <= s[i][2] <= 0 + s[i][0]):
            print("No")
            exit()
        else:
            if (s[i][0] % 2 == 0 and (s[i][1] + s[i][2]) % 2 != 0) or (s[i][0] % 2 != 0 and (s[i][1] + s[i][2]) % 2 == 0):
                print("No")
                exit()
    else:
        if not(s[i - 1][1] - (s[i][0] - s[i - 1][0]) <= s[i][1] <= s[i - 1][1] + (s[i][0] - s[i - 1][0])) or not(s[i - 1][2] - (s[i][0] - s[i - 1][0]) <= s[i][2] <= s[i - 1][2] + (s[i][0] - s[i - 1][0])):
            print("No")
            exit()
        else:
            if (s[i][0] % 2 == 0 and (s[i][1] + s[i][2]) % 2 != 0) or (s[i][0] % 2 != 0 and (s[i][1] + s[i][2]) % 2 == 0):
                print("No")
                exit()

print("Yes")"""

