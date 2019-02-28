ds = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def dfs(x, y):
    global miro, result, N
    if miro[x][y] == 3:
        return 1
    else:
        for d in ds:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < N and miro[nx][ny] not in [1, 4]:
                temp = miro[x][y]
                miro[x][y] = 4
                if dfs(nx, ny):
                    return 1
                miro[x][y] = temp
        return 0


for T in range(1, int(input()) + 1):
    N = int(input())
    miro = []
    result = 0
    for _ in range(N):
        miro.append(list(map(int, input())))
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                result = dfs(i, j)
                break
    print(f'#{T} {result}')
