import math
n, a, b = map(int, input().split())
d = []
for i in range(n):
    d.append(input())
# [d1, d2, d3, ..., dN]
h = [int(m) for m in d]#int型に直す
#print(x)

low = 0
high = math.ceil(max(h)/b)
# t は中央番目の数
t = (low + high) // 2

# 探索の下限のlowが上限のhighになるまで探索
# lowがhighに達すると数は見つからなかっTrueたということ
X = 0
Y = 0
s = 0
while high - low >= 0:
    for j in range(n):
        X += max(0, math.ceil((h[j] - t * b) / (a - b)))
        #Y += max(0, math.ceil((h[j] - (t - 1) * b) / (a - b)))
    if X == t:
        print(t)
        exit()
    elif X < t:
        high = t - 1
        """for j in range(n):
            Y += max(0, math.ceil((h[j] - (t - 1) * b) / (a - b)))"""
    elif X > t:
        low = t + 1
    s = t
    t = (low + high) // 2
    X = 0
    Y = 0
for j in range(n):
  if math.ceil((h[j] - s * b) / (a - b)) > 0:
            Y += math.ceil((h[j] - s * b) / (a - b))
if Y <= s:
  print(s)
else:
  print(s + 1)

#print(math.ceil(sum(h)/(a + b * (n - 1))))
"""h.sort(reverse=True)
h0 = h[0]
h1 = h[1]
h2 = h[2]

t = math.ceil((h0 - h1)/(a - b))
h0 -= t * (a - b) + t * b
h1 -= t * b
h0 = max(h1, h2)
h1 = max(h0, h2)"""

