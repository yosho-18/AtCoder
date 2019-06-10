k = int(input())
if k == 0:
    print(2)
    print(0, 0)
elif k == 1:
    print(3)
    print(1, 0, 3)
elif k < 10 ** 16:
    n = 2
    print(n)
    a = k // n * (n + 1) + n - k - 1#n - k % n
    b = (k // n + 1) * (n + 1) + n - k - 1#k % n
    if k % n == 0:
        print(a, a)
    elif k % n == 1:
        print(a, b)
else:
    n = 50
    print(n)
    a = k // n * (n + 1) + n - k - 1  # n - k % n
    b = (k // n + 1) * (n + 1) + n - k - 1  # k % n
    for i in range(k % n):
        print(b, "", end = "")
    for i in range(n - k % n):
        print(a, "", end = "")
"""if k == 0:
    print(3)
    print(2,2,2)
if k == 1:
    print(3)
    print(1, 0, 3)
else:
    print(k)
    for i in range(k):
        print(k,"",end = "")"""