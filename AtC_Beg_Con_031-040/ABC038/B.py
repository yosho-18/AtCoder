a, b = map(int, input().split())
c, d = map(int, input().split())

if a == c or a == d:
    print("YES")
elif b == c or b == d:
    print("YES")
elif c == a or c == b:
    print("YES")
elif d == a or d == b:
    print("YES")
else:
    print("NO")