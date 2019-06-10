n, m = map(int, input().split())
map = [input() for i in range(n)]

from_up = [[0 for j in range(m)] for i in range(n)]
from_left = [[0 for j in range(m)] for i in range(n)]
from_down = [[0 for j in range(m)] for i in range(n)]
from_right = [[0 for j in range(m)] for i in range(n)]


for i in range(n):
    for j in range(m):
        if map[i][j] == ".":
            if i - 1 >= 0:
                if map[i - 1][j] == ".":#"#"のときは0
                    from_up[i][j] = from_up[i - 1][j] + 1
            if j - 1 >= 0:
                if map[i][j - 1] == ".":
                    from_left[i][j] = from_left[i][j - 1] + 1

for i in reversed(range(n)):
    for j in reversed(range(m)):
        if map[i][j] == ".":
            if i + 1 < n:
                if map[i + 1][j] == ".":
                    from_down[i][j] = from_down[i + 1][j] + 1
            if j + 1 < m:
                if map[i][j + 1] == ".":
                    from_right[i][j] = from_right[i][j + 1] + 1

ans = 0
for i in range(n):
    for j in range(m):
        ans += from_up[i][j] * from_right[i][j] + from_right[i][j] * from_down[i][j] + from_down[i][j] * from_left[i][j] + from_left[i][j] * from_up[i][j]
print(ans)