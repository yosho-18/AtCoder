n = int(input())
l = (n + 1) // 9
if (l % 2 == 0 and n % 2 != 0) or (l % 2 != 0 and n % 2 == 0):
    print("Win")
else:
    print("Lose")