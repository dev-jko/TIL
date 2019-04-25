# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용


from heapq import heappush, heappop

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for T in range(1, int(input()) + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    q = []
    visited = [[-1] * N for _ in range(N)]
    heappush(q, (0, 0, 0))
    while q:
        w, x, y = heappop(q)
        if visited[x][y] == -1 or visited[x][y] > w:
            visited[x][y] = w
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    heappush(q, (w + 1 + ((data[nx][ny] - data[x][y]) if data[x][y] < data[nx][ny] else 0), nx, ny))
    print('#{} {}'.format(T, visited[-1][-1]))
