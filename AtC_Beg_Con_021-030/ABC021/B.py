n = int(input())
a, b = map(int, input().split())
k = int(input())
p = [int(m) for m in input().split()]
p.append(a)
p.append(b)
print("YES" if len(p) == len(set(p)) else "NO")