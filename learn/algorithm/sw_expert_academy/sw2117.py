# swea 2117. [모의 SW 역량테스트] 홈 방범 서비스

from collections import deque


def get_cost(k):
    if cost[k] == -1:
        cost[k] = k * k + (k - 1) * (k - 1)
    return cost[k]


dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
cost = [-1 for _ in range(51)]

q = deque()
for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    result = 0
    D = [[0 for _ in range(N)] for _ in range(N)]
    cnt = [0 for _ in range(N * 2)]
    for r in range(N):
        for c in range(N):
            q.clear()
            for i in range(N):
                for j in range(N):
                    D[i][j] = 0
            for i in range(N * 2):
                cnt[i] = 0
            q.append((r, c))
            D[r][c] = 1
            if data[r][c] == 1:
                cnt[1] = 1
            while len(q):
                x, y = q.popleft()
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and D[nx][ny] == 0:
                        q.append((nx, ny))
                        D[nx][ny] = D[x][y] + 1
                        if data[nx][ny] == 1:
                            cnt[D[nx][ny]] += 1
            for i in range(1, len(cnt)):
                cnt[i] += cnt[i - 1]
                if get_cost(i) <= cnt[i] * M and cnt[i] > result:
                    result = cnt[i]
    print('#{} {}'.format(T, result))
