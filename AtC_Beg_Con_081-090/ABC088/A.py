x = int(input())
a = int(input())
b = int(input())

t = x - a
k = 0
while t - b * k >= 0:
  k += 1

print(t - b * (k - 1))
