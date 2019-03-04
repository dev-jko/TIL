# https://www.acmicpc.net/problem/7562
# 나이트의 이동

from collections import deque

dxy = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]
q = deque()
for _ in range(int(input())):
    I = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    visited = [[-1 for _ in range(I)] for _ in range(I)]
    visited[start[0]][start[1]] = 0
    q.clear()
    q.append((start[0], start[1]))
    while len(q):
        x, y = q.popleft()
        if x == end[0] and y == end[1]:
            break
        else:
            for d in dxy:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < I and 0 <= ny < I and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    print(visited[end[0]][end[1]])
