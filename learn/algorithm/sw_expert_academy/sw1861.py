# 1861. 정사각형 방


def dfs(x, y):
    cnt[x][y] = 1
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and data[x][y] + 1 == data[nx][ny]:
            if cnt[nx][ny] == -1:
                cnt[nx][ny] = dfs(nx, ny)
            cnt[x][y] = max(cnt[x][y], cnt[nx][ny] + 1)
    return cnt[x][y]


dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for T in range(1, int(input()) + 1):
    N = int(input())
    N2 = N * N
    data = [list(map(int, input().split())) for _ in range(N)]
    cnt = [[-1] * N for _ in range(N)]
    result = [0, 0]
    for i in range(N):
        for j in range(N):
            dfs(i, j)
            if result[1] < cnt[i][j] or (result[1] == cnt[i][j] and result[0] > data[i][j]):
                result[0], result[1] = data[i][j], cnt[i][j]
    print('#{} {} {}'.format(T, result[0], result[1]))
