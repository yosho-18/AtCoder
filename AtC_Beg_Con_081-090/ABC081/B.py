n = int(input())
a = input().split()
a = [int(m) for m in a]

ans = 0
while True:
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] = a[i] // 2
            if i == n - 1:
                ans += 1
        else:
            print(ans)
            exit()