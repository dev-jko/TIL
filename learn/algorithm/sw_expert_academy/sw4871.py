for T in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    graph = [[False for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(E):
        i, j = map(int, input().split())
        graph[i][j] = True
    S, G = map(int, input().split())
    visited = [False for _ in range(V + 1)]
    stack = [S]
    result = 0
    while len(stack) > 0:
        v = stack.pop()
        if visited[v]:
            continue
        visited[v] = True
        if visited[G]:
            result = 1
            break
        for i in range(1, V + 1):
            if graph[v][i]:
                stack.append(i)
    print(f'#{T} {result}')
