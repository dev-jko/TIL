from collections import deque

dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
q = deque()
for T in range(1, int(input()) + 1):
    N = int(input())
    q.clear()
    miro = []
    for _ in range(N):
        miro.append(list(map(int, input())))
    start = end = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start = (i, j)
            if miro[i][j] == 3:
                end = (i, j)
    q.append(start)
    D = [[999 for _ in range(N)] for _ in range(N)]
    D[start[0]][start[1]] = 0
    while len(q):
        x, y = q.popleft()
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < N and miro[nx][ny] != 1 and D[nx][ny] > D[x][y] + 1:
                D[nx][ny] = D[x][y] + 1
                q.append((nx, ny))
    print('#{} {}'.format(T, D[end[0]][end[1]] - 1 if D[end[0]][end[1]] != 999 else 0))
