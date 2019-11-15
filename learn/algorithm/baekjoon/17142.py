from collections import deque

N, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
v = []
for i in range(N):
    for j in range(N):
        if pan[i][j] == 2:
            v.append((i, j))
answer = 0xffffffffff
used = [False] * len(v)
dd = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def bfs(pick):
    global answer
    board = [[-1] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    q = deque()
    for r, c in v:
        board[r][c] = 0
    for i in pick:
        r, c = v[i]
        q.append((0, r, c))
        visited[r][c] = True

    while q:
        t, r, c = q.popleft()
        for dr, dc in dd:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and pan[nr][nc] != 1 and not visited[nr][nc]:
                if board[nr][nc] == -1:
                    board[nr][nc] = t + 1
                visited[nr][nc] = True
                if t + 1 > answer and board[nr][nc] != 0:
                    return
                q.append((t + 1, nr, nc))
    m = 0
    for i in range(N):
        for j in range(N):
            if pan[i][j] == 1:
                continue
            if board[i][j] == -1:
                return
            m = max(board[i][j], m)
    answer = min(m, answer)


def dfs(k, pick):
    if len(pick) == M:
        bfs(pick)
    elif k == len(v):
        return
    else:
        pick.append(k)
        dfs(k + 1, pick)
        pick.pop()
        dfs(k + 1, pick)


dfs(0, [])
print(answer if answer != 0xffffffffff else -1)