# https://www.acmicpc.net/problem/16234
# 인구 이동

# TODO  못 품


from collections import deque


def bfs(cnt):
    check = False
    for i in range(N):
        for j in range(N):
            if visited != cnt:
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
                            union.append((nx, ny))
                            visited[nx][ny] = cnt
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
for cnt in range(2000):
    if bfs(cnt):
        result += 1
    else:
        break
print(result)
