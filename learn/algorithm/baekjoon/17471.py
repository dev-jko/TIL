from collections import deque


def dfs(k):
    global N, div, answer
    if k == N:
        bfs()
    else:
        div[k] = 1
        dfs(k + 1)
        div[k] = 2
        dfs(k + 1)


def bfs():
    global div, graph, population, answer
    if 1 not in div or 2 not in div:
        return
    check = [None, set(), set()]
    s1 = div.index(1)
    s2 = div.index(2)
    q = deque()
    q.append(s1)
    check[div[s1]].add(s1)
    while q:
        c = q.popleft()
        for i in graph[c]:
            if i in check[div[i]] or div[i] != div[c]:
                continue
            q.append(i)
            check[div[i]].add(i)
    q.append(s2)
    check[div[s2]].add(s2)
    while q:
        c = q.popleft()
        for i in graph[c]:
            if i in check[div[i]] or div[i] != div[c]:
                continue
            q.append(i)
            check[div[i]].add(i)
    if len(check[1]) + len(check[2]) != N:
        return
    sum1 = sum(map(lambda x: population[x], check[1]))
    sum2 = sum(map(lambda x: population[x], check[2]))
    t = abs(sum1 - sum2)
    if answer == -1 or t < answer:
        answer = t


N = int(input())
population = list(map(int, input().split()))
graph = []
for _ in range(N):
    t = list(map(lambda x:int(x) - 1, input().split()))
    graph.append(t[1:])
div = [0] * N
answer = -1
dfs(0)
print(answer)
