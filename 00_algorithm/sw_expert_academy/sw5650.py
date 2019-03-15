# 5650. [모의 SW 역량테스트] 핀볼 게임

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

next_d = [
    0,
    [1, 3, 0, 2],
    [3, 0, 1, 2],
    [2, 0, 3, 1],
    [1, 2, 3, 0],
    [1, 0, 3, 2]
]


def simul(x, y):
    result = 0
    start_x = x
    start_y = y
    for d in range(4):
        x = start_x
        y = start_y
        score = 0
        while True:
            x += dxy[d][0]
            y += dxy[d][1]
            cell = data[x][y]
            # 블럭
            if 1 <= cell <= 5:
                score += 1
                d = next_d[cell][d]
            elif cell == 99:
                score += 1
                d = next_d[5][d]
            # 웜홀
            elif 6 <= cell <= 10:
                t = wormhole[cell]
                if t[0][0] == x and t[0][1] == y:
                    x = t[1][0]
                    y = t[1][1]
                else:
                    x = t[0][0]
                    y = t[0][1]
            if cell == -1:
                break
            if x == start_x and y == start_y:
                break
        result = max(result, score)
    return result

ans = []
for T in range(1, int(input()) + 1):
    N = int(input())
    data = [[99 for _ in range(N + 2)]]
    for _ in range(N):
        data.append([99] + list(map(int, input().split())) + [99])
    data.append([99 for _ in range(N + 2)])
    result = 0
    wormhole = [None, None, None, None, None, None, [], [], [], [], []]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if data[i][j] >= 6:
                wormhole[data[i][j]].append((i, j))

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if data[i][j] == 0:
                result = max(result, simul(i, j))
    ans.append('#{} {}'.format(T, result))
for a in ans:
    print(a)

