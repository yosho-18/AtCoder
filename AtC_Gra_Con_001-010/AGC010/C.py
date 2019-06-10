k = int(input())
print(k)
for i in range(1, k + 1):
    for j in range(1, k + 1):
        j = j + i
        if j <= k:
            print(j, end = " ")
        else:
            j -= k
            print(j, end = " ")
    print()