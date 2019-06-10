n, a, b = map(int, input().split())
if abs(a - b) % 2 == 0:
    print("Alice")
else:
    print("Borys")