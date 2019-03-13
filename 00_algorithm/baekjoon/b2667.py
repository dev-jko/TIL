# https://www.acmicpc.net/problem/2667
# 단지번호붙이기


from collections import deque

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

q = deque()
N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input())))
group = 2
cnts = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            q.append((i, j))
            data[i][j] = group
            cnt = 1
            while len(q):
                x, y = q.popleft()
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 1:
                        data[nx][ny] = group
                        cnt += 1
                        q.append((nx, ny))
            group += 1
            cnts.append(cnt)
print(group - 2)
cnts.sort()
for c in cnts:
    print(c)
