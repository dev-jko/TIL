# 2819. 격자판의 숫자 이어 붙이기


def dfs(k, x, y):
    if k == 7:
        result.add(tuple(number))
    else:
        number[k] = data[x][y]
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                dfs(k + 1, nx, ny)


dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
number = [0] * 7
for T in range(1, int(input()) + 1):
    data = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            dfs(0, i, j)
    print('#{} {}'.format(T, len(result)))
