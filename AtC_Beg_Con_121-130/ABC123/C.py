n = int(input())
p = []
for i in range(5):
    p.append(int(input()))
mi = min(p)
y = (mi + n - 1) // mi
print(y + 4)