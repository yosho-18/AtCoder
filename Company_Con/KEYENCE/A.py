a = input().split()
a = [int(m) for m in a]
a = set(a)
b = [1, 9, 7, 4]
b = set(b)
if len(a & b) == 4:
    print("YES")
else:
    print("NO")