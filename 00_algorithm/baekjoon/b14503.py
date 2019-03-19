# https://www.acmicpc.net/problem/14503
# 로봇 청소기

dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, M = map(int, input().split())
data = []
robot = list(map(int, input().split()))
for _ in range(N):
    data.append(list(map(int, input().split())))
data[robot[0]][robot[1]] = 2
cnt = 1
while True:
    nd = robot[2]
    for i in range(4):
        nd = (nd + 3) % 4
        dx, dy = dxy[nd]
        nx, ny = robot[0] + dx, robot[1] + dy
        if data[nx][ny] == 0:
            data[nx][ny] = 2
            cnt += 1
            robot[0], robot[1], robot[2] = nx, ny, nd
            break
    else:
        nd = (robot[2] + 2) % 4
        dx, dy = dxy[nd]
        nx, ny = robot[0] + dx, robot[1] + dy
        if data[nx][ny] == 1:
            break
        robot[0], robot[1] = nx, ny
print(cnt)
