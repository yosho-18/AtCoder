n = int(input())
if n % 2 == 0:
    print((n ** 2)// 2 - n)
else:
    print(n ** 2 - (n + 1) * (n + 3) // 2 + 4)