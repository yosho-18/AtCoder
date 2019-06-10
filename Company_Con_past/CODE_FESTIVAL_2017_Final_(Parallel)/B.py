import collections

s = input()

al = collections.Counter(s)
if max(al["a"], al["b"], al["c"]) - min(al["a"], al["b"], al["c"]) <= 1:
    print("YES")
else:
    print("NO")