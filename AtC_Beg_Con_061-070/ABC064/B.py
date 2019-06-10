n = int(input())
a = input().split()
a = [int(m) for m in a]
print(max(a) - min(a))