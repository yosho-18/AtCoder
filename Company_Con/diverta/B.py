R, G, B, N = map(int, input().split())
ans = 0
for r in range(3001):
    for g in range(3001):
        if (N - r * R - g * G) / B == (N - r * R - g * G) // B and (N - r * R - g * G) / B >= 0:
            ans += 1
print(ans)