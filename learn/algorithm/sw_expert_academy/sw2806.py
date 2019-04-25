d = [[-1, -1], [-1, 1]]


def bt(n, grid, k, result):
    if n == k:
        result[0] += 1
    else:
        for i in range(n):
            check = False
            for j in range(N):
                if grid[j][i] == 1 and j != k:
                    check = True
                    break
            if check:
                continue
            for value in d:
                x, y = k, i
                while True:
                    x += value[0]
                    y += value[1]
                    if not 0 <= x < n or not 0 <= y < n:
                        break
                    if grid[x][y] == 1:
                        check = True
                        break
                if check:
                    break
            if check:
                continue
            grid[k][i] = 1
            bt(n, grid, k + 1, result)
            grid[k][i] = 0


for T in range(1, int(input()) + 1):
    N = int(input())
    grid = [[0 for _ in range(N)] for _ in range(N)]
    result = [0]
    bt(N, grid, 0, result)
    print(f'#{T} {result[0]}')
