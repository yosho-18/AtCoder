x, y = map(int, input().split())
k = [1, 3, 5, 7, 8, 10, 12]
g = [4, 6, 9, 11]
g2 = [2]
if x in k and y in k:
    print("Yes")
elif x in g and y in g:
    print("Yes")
elif x in g2 and y in g2:
    print("Yes")
else:
    print("No")