import math
n = int(input())
m = math.sqrt(n)
p = 0
q = 0
for i in range(int(m), 0, -1):
    if n % i == 0:
        p = str(i)
        q = str(int(n / i))
        break
print(max(len(p), len(q)))