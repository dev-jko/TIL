# https://www.acmicpc.net/problem/1987
# 알파벳


def dfs(x, y, cnt):
    if cnt == 27:
        return cnt
    temp = cnt
    for d in dxy:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < R and 0 <= ny < C and not used[data[nx][ny]]:
            used[data[nx][ny]] = True
            temp = max(temp, dfs(nx, ny, cnt + 1))
            used[data[nx][ny]] = False
    return temp


dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
R, C = map(int, input().split())
data = []
for _ in range(R):
    data.append(list(map(ord, input())))
used = [False for _ in range(91)]
used[data[0][0]] = True
result = dfs(0, 0, 1)
print(result)
