# 1868. 파핑파핑 지뢰찾기


def open_cell(x, y, added):
    temp = set()
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= i < N and 0 <= j < N:
                if data[i][j] == '*':
                    memo[x][y].add((x, y))
                    return
                else:
                    temp.add((i, j))
    memo[x][y].add((x, y))
    for nx, ny in list(temp - memo[x][y]):
        if len(memo[nx][ny]) == 0 and ((nx, ny) not in added):
            open_cell(nx, ny, added | memo[x][y])
        memo[x][y] |= memo[nx][ny]


for T in range(1, int(input()) + 1):
    N = int(input())
    data = [input() for _ in range(N)]
    memo = [[set() for _ in range(N)] for _ in range(N)]
    dots = set()
    result = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == '.':
                open_cell(i, j, set())
                dots.add((i, j))
    sorted_r = sorted(dots, reverse=True, key=lambda a: len(memo[a[0]][a[1]]))
    idx = 0
    while dots:
        if sorted_r[idx] in dots:
            dots -= memo[sorted_r[idx][0]][sorted_r[idx][1]]
            result += 1
        idx += 1
    print('#{} {}'.format(T, result))
