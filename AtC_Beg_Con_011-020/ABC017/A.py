s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())
s3, e3 = map(int, input().split())
ans = (s1 * e1 + s2 * e2 + s3 * e3) * 1 / 10
print(int(ans))
