# https://www.acmicpc.net/problem/14500
# 테트로미노

# pypy3만 통과, python3 시간초과

from itertools import combinations

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
result = 0
use = set()
for i in range(N):
    for j in range(M):
        for combi in combinations([0, 1, 2, 3], 3):
            use.add((i, j))
            for d in combi:
                nx, ny = i + dxy[d][0], j + dxy[d][1]
                if 0 <= nx < N and 0 <= ny < M:
                    use.add((nx, ny))
            if len(use) == 4:
                temp = 0
                for x, y in use:
                    temp += data[x][y]
                result = max(result, temp)
            use.clear()
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    use.add((i, j))
                    nx, ny = i, j
                    for d in a, b, c:
                        nx += dxy[d][0]
                        ny += dxy[d][1]
                        if 0 > nx or nx >= N or 0 > ny or ny >= M:
                            break
                        use.add((nx, ny))
                    if len(use) == 4:
                        temp = 0
                        for x, y in use:
                            temp += data[x][y]
                        result = max(result, temp)
                    use.clear()
print(result)


