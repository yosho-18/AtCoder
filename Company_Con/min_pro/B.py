a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())
if [a1, b1, a2, b2, a3, b3].count(1) == 3 or [a1, b1, a2, b2, a3, b3].count(2) == 3 or [a1, b1, a2, b2, a3, b3].count(3) == 3 or [a1, b1, a2, b2, a3, b3].count(4) == 3:
    print("NO")
else:
    print("YES")