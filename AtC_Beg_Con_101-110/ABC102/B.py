n = int(input())
a = input().split()
a = [int(m) for m in a]

x = max(a)
y = min(a)

print(x - y)