n = input()
j = [x for x in list(str(n))]
count = 0
for i in range(4):
    if j[i] == '+':
        count += 1
    else:
        count -= 1

print(count)
