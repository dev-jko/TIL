# https://www.acmicpc.net/problem/5427
# 불

from collections import deque

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = deque()
for _ in range(int(input())):
    q.clear()
    w, h = map(int, input().split())
    data = []
    for _ in range(h):
        data.append(list(input()))
    start = 0
    fire = [[-1 for _ in range(w)] for _ in range(h)]
    move = [[-1 for _ in range(w)] for _ in range(h)]
    exits = []
    for i in range(h):
        for j in range(w):
            if data[i][j] == '*':
                fire[i][j] = 0
                q.append((i, j))
            if data[i][j] == '@':
                move[i][j] = 0
                start = (i, j)
            if (i in [0, h - 1] or j in [0, w - 1]) and data[i][j] == '.':
                exits.append((i, j))
    if start[0] in [0, h - 1] or start[1] in [0, w - 1]:
        print('1')
        continue
    if len(exits) == 0:
        print('IMPOSSIBLE')
        continue
    while len(q):
        x, y = q.popleft()
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < h and 0 <= ny < w and fire[nx][ny] == -1 and data[nx][ny] != '#':
                fire[nx][ny] = fire[x][y] + 1
                q.append((nx, ny))
    q.append(start)
    check = False
    while len(q):
        x, y = q.popleft()
        for e in exits:
            if x == e[0] and y == e[1]:
                check = True
                break
        if check:
            break
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < h and 0 <= ny < w and move[nx][ny] == -1 and data[nx][ny] != '#' and (fire[nx][ny] == -1 or move[x][y] + 1 < fire[nx][ny]):
                move[nx][ny] = move[x][y] + 1
                q.append((nx, ny))
    result = 'IMPOSSIBLE'
    for x, y in exits:
        if move[x][y] != -1 and (result == 'IMPOSSIBLE' or result > move[x][y]):
            result = move[x][y]
    if result != 'IMPOSSIBLE':
        result += 1
    print(result)
