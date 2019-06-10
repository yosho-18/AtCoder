n = int(input())
a = input().split()
count = 0
finish = 0
#print("sept")
while finish == 0:
    for i in range(n):
        if int(a[i]) % 2 == 0:
            a[i] = int(a[i]) / 2
        else:
            finish = 1
            break
    if finish == 0:
        count += 1

print(count)