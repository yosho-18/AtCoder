p = []
for i in range(5):
    p.append(int(input()))
k = int(input())
if max(p) - min(p) > k:
    print(":(")
else:
    print("Yay!")