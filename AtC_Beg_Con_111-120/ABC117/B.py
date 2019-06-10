n = int(input())
a = [int(m) for m in input().split()]
k = max(a)
q = sum(a) - k
if q > k:
    print("Yes")
else:
    print("No")