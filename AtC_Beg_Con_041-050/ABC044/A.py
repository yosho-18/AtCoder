n = int(input())
k = int(input())
x = int(input())
y = int(input())
if n > k:
    print(x * k + (n - k) * y)
else:
    print(x * n)