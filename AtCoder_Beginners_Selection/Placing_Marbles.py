n = input()
j = [int(x) for x in list(str(n))]
count = 0
for i in range(3):
    if j[i] == 1:
        count = count + 1
print(count)