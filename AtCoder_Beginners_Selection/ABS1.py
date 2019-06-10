#a = int(input())
#b = int(input())
a, b = map(int, input().split())

if a * b % 2 == 0:
    print("Even")
else:
    print("Odd")