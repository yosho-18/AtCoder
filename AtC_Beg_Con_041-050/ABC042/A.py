a, b, c = map(int, input().split())
if (a == b == 5 and c == 7) or (a == c == 5 and b == 7) or (c == b == 5 and a == 7):
    print("YES")
else:
    print("NO")