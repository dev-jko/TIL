from collections import deque

q = deque()
for T in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1
    S, G = map(int, input().split())
    d = [99999 for _ in range(V + 1)]
    q.clear()
    q.append(S)
    d[S] = 0
    while len(q):
        if d[G] != 99999:
            break
        v = q.popleft()
        for i in range(1, V + 1):
            if graph[v][i] == 1 and d[i] == 99999:
                d[i] = d[v] + 1
                q.append(i)
    if d[G] == 99999:
        d[G] = 0
    print('#{} {}'.format(T, d[G]))
