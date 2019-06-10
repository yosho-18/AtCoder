n = input()
j = [int(x) for x in list(str(n))]
for i in range(3):
    if j[i] == 1:
        j[i] = 9
    else:
        j[i] = 1

print(str(j[0]) + str(j[1]) + str(j[2]))