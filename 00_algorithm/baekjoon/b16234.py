# https://www.acmicpc.net/problem/16234
# 인구 이동

from collections import deque


def bfs(cnt):
    check = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] != cnt:
                sum_p = data[i][j]
                q.append((i, j))
                visited[i][j] = cnt
                union = [(i, j)]
                while q:
                    x, y = q.popleft()
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] != cnt and L <= abs(
                                data[x][y] - data[nx][ny]) <= R:
                            sum_p += data[nx][ny]
                            visited[nx][ny] = cnt
                            union.append((nx, ny))
                            q.append((nx, ny))
                if len(union) > 1:
                    r = sum_p // len(union)
                    for x, y in union:
                        data[x][y] = r
                    check = True
    return check


dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque()
N, L, R = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
result = 0
visited = [[-1] * N for _ in range(N)]
while result < 2000:
    if bfs(result):
        result += 1
    else:
        break
print(result)

# 4 10 50
# 10 100 20 90
# 80 100 60 70
# 70 20 30 40
# 50 20 100 10
