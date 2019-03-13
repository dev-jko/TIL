# https://www.acmicpc.net/problem/2606
# 바이러스

def dfs(v):
    for i in range(N + 1):
        if data[v][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(i)


N = int(input())
data = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    data[a][b] = data[b][a] = 1
visited = [False for _ in range(N + 1)]
visited[1] = True
dfs(1)
result = visited.count(True) - 1
print(result)

