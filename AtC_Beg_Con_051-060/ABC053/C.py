x = int(input())
k = 0
if 0 < x % 11 <= 6:
    k = 1
else:
    k = 2
if x % 11 == 0:
    k = 0
print(x // 11 * 2 + k)
