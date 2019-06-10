def dfs(graph, start, visited):
    if visited[start] != -99999:
        return True

    stack = [start]
    visited[start] = 0#初期値を0に設定
    while stack:
        label = stack.pop()
        for nextnode, distance in graph[label]:
            if visited[nextnode] == -99999:#初めて訪れる場所なら座標を設定
                stack.append(nextnode)
                visited[nextnode] = visited[label] + distance
            elif visited[nextnode] != visited[label] + distance:#二回目以降なら一回目と同じかを確認，stackはとらない
                return False
    return True


N, M = (int(i) for i in input().split())

graph = [[] for i in range(N + 1)]#インデックス番号と実際の番号をあわせるためにN+1にする

for i in range(M):
    L, R, D = (int(i) for i in input().split())
    graph[L].append((R, D))
    graph[R].append((L, -1 * D))

visited = [-99999 for i in range(N + 1)]

flag = True
for i in range(1, N + 1):
    ans = dfs(graph, i, visited)
    if not ans:
        flag = False
        break

if flag:
    print('Yes')
else:
    print('No')

"""if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for i in range(m):  # h:高さ
        a.append([int(m) for m in input().split()])
    b = []
    for i in range(m):
        b.append([a[i][1], a[i][0], a[i][2]])
        b.append([a[i][0], a[i][1], -a[i][2]])
dfs()
"""
"""
    +-------------1
    |             |
    |     +-------+-----+
    |     |       |     |
    |   +-2-+     6   +-8-+
    |   |   |     |   |   |
    |   3   4     7   9   10
    |       |     |   |   |
    +-------5     +---+   11
    
    graph = {1: [2, 6, 8],
             2: [3, 4],
             3: [],
             4: [5],
             5: [1],
             6: [7],
             7: [],
             8: [9, 10],
             9: [7],
             10: [11],
             11: [],
             }
    print(dfs(graph, 1, 10))
    """