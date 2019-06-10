total_score = 0
b = [None] * 2
for i in range(2):
    b[i] = [int(x) for x in input().split()]
    total_score += sum(b[i])
c = [None] * 3
for i in range(3):
    c[i] = [int(x) for x in input().split()]
    total_score += sum(c[i])

board = [-1 for _ in range(9)]
memo = dict()


def get_score():
    score = 0
    for i in range(2):
        for j in range(3):
            if board[i + j * 3] == board[(i + 1) + j * 3]:
                score += b[i][j]
    for i in range(3):
        for j in range(2):
            if board[i + j * 3] == board[i + (j + 1) * 3]:
                score += c[i][j]
    return score


def f(turn):
    if turn == 9:
        return get_score()
    else:
        if tuple(board) in memo.keys():
            return memo[tuple(board)]

        if turn % 2:
            x = 1#1,3,5...(直子)
        else:
            x = 0#0,2,4...(直大)
        res = float('-inf')
        for i in range(9):
            if board[i] == -1:
                board[i] = x
                if turn % 2:
                    res = max(res, -1 * f(turn + 1))#最小値(直子)
                else:
                    res = max(res, f(turn + 1))#最大値(直大)
                board[i] = -1

        if turn % 2:
            res = -1 * res
        memo[tuple(board)] = res
        return res


score = f(0)
print(score)
print(total_score - score)