def __logging(visited, rest=[]):
    print("visited:%s\n   rest:%s\n" % (visited, rest))


def bfs(graph, start, end):
    queue = [start]
    visited = []
    while queue:
        label = queue.pop(0)
        if label == end:
            visited.append(label)
            __logging(visited, queue)
            return visited
        if label not in visited:
            visited.append(label)
            queue += graph.get(label, [])
            #こっちでもいい
            #queue += [x for x in graph.get(label, []) if x not in visited]
        __logging(visited, queue)
    return visited


if __name__ == '__main__':
    """
    +-------------1
    |             |
    |     +-------+-----+
    |     |       |     |
    |   +-2-+     3   +-4-+
    |   |   |     |   |   |
    |   5   6     7   8   9
    |       |     |   |   |
    +-------10    +---+   11
    """
    graph = {1: [2, 3, 4],
             2: [5, 6],
             3: [7],
             4: [8, 9],
             5: [],
             6: [10],
             7: [],
             8: [7],
             9: [11],
             10: [1],
             11: [],
             }
    print(bfs(graph, 1, 10))






a = hs(10)

def bfs(circlepoint):
    flag = [[0 for _ in range(10)] for _ in range(10)]
    queue = deque()
    queue.append(circlepoint)
    while queue != deque():
        cri_i, cri_j = queue.popleft()
        for dx, dy in dd:
            nx = cri_j + dx
            ny = cri_i + dy
            if 0 <= nx < 10 and 0 <= ny < 10:
                if a[ny][nx] == "o" and flag[ny][nx] == 0:
                    queue.append((ny, nx))
                    flag[ny][nx] = 1
    for i in range(10):
        for j in range(10):
            if a[i][j] == "o" and flag[i][j] == 0:
                return False
    else:
        return True


for i in range(10):
    for j in range(10):
        circlepoint = (i, j)
        if a[i][j] == "x":
            a[i][j] = "o"
            if bfs(circlepoint):
                print("YES")
                exit()
            else:
                a[i][j] = "x"
print("NO")