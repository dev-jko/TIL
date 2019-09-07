def dfs(x, y, state, cnt):
    global boardg, visited, N, answer

    if answer <= N + N - 3:
        return

    print(cnt, "  ###################")
    for vv in visited:
        print(vv)

    if x == y == N - 1:
        if cnt < answer:
            answer = cnt
    else:
        if cnt + 1 >= answer:
            return

        if state == 0:  # 가로
            if x + 1 < N and boardg[y][x + 1] == 0 and not visited[y][x + 1]:

                visited[y][x + 1] = True
                dfs(x + 1, y, 0, cnt + 1)
                visited[y][x + 1] = False
            if x - 1 >= 0 and boardg[y][x - 1] == 0 and not visited[y][x - 1]:
                visited[y][x - 1] = True
                dfs(x - 1, y, 0, cnt + 1)
                visited[y][x - 1] = False
            if x - 1 > 0 and y + 1 < N and boardg[y + 1][x] + boardg[y + 1][x - 1] == 0:
                if not visited[y + 1][x]:
                    visited[y + 1][x] = True
                    dfs(x, y + 1, 1, cnt + 1)
                    visited[y + 1][x] = False
                if not visited[y + 1][x - 1]:
                    visited[y + 1][x - 1] = True
                    dfs(x - 1, y + 1, 1, cnt + 1)
                    visited[y + 1][x - 1] = False
            if x >= 1 and y >= 1 and boardg[y - 1][x] + boardg[y - 1][x - 1] == 0:
                if not visited[y - 1][x]:
                    visited[y - 1][x] = True
                    dfs(x, y, 1, cnt + 1)
                    visited[y - 1][x] = False
                if not visited[y - 1][x - 1]:
                    visited[y - 1][x - 1] = True
                    dfs(x - 1, y, 1, cnt + 1)
                    visited[y - 1][x - 1] = False

        else:  # 세로
            if y > 0 and boardg[y - 1][x] == 0 and not visited[y - 1][x]:
                visited[y - 1][x] = True
                dfs(x, y - 1, 1, cnt + 1)
                visited[y - 1][x] = False
            if y + 1 < N and boardg[y + 1][x] == 0 and not visited[y + 1][x]:
                visited[y + 1][x] = True
                dfs(x, y + 1, 1, cnt + 1)
                visited[y + 1][x] = False
            if y >= 0 and x >= 1 and boardg[y][x - 1] + boardg[y - 1][x - 1] == 0:
                if not visited[y - 1][x - 1]:
                    visited[y - 1][x - 1] = True
                    dfs(x, y - 1, 0, cnt + 1)
                    visited[y - 1][x - 1] = False
                if not visited[y][x - 1]:
                    visited[y][x - 1] = True
                    dfs(x, y, 0, cnt + 1)
                    visited[y][x - 1] = False
            if y >= 1 and x + 1 < N and boardg[y][x + 1] + boardg[y - 1][x + 1] == 0:
                if not visited[y - 1][x + 1]:
                    visited[y - 1][x + 1] = True
                    dfs(x + 1, y - 1, 0, cnt + 1)
                    visited[y - 1][x + 1] = False
                if not visited[y][x + 1]:
                    visited[y][x + 1] = True
                    dfs(x + 1, y, 0, cnt + 1)
                    visited[y][x + 1] = False


boardg = None
visited = None
N = 0
answer = 0


def solution(board):
    global boardg, visited, N, answer
    boardg = board
    answer = 999999999999
    N = len(board)
    visited = [[False] * N for _ in range(N)]
    # visited [y][x][상태]  # 0  가로, 1 세로
    visited[0][0] = visited[0][1] = True
    dfs(1, 0, 0, 0)
    return answer


inputs = [
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 0]
]
# inputs = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
# 7
print(solution(inputs))
