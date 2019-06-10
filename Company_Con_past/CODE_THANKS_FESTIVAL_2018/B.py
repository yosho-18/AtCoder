x, y = map(int, input().split())
"""if x % 4 == 0 and y % 4 == 0:
    print("Yes")
elif (x % 4 == 1 and y % 4 == 3) or (x % 4 == 3 and y % 4 == 1):
    print("Yes")
else:
    print("No")"""
if abs(3 * x - y) % 8 == 0 and abs(3 * y - x) % 8 == 0 and (3 * x - y) >= 0 and (3 * y - x) >= 0:
    print("Yes")
else:
    print("No")