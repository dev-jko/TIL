for T in range(1, 11):
    V, E = map(int, input().split())
    graph = [[False for _ in range(V + 1)] for _ in range(V + 1)]
    inputs = list(map(int, input().split()))
    for i in range(0, len(inputs), 2):
        graph[inputs[i]][inputs[i + 1]] = True
    result = []
    visited = [False for _ in range(V + 1)]
    while len(result) < V:
        for i in range(1, V + 1):
            if not visited[i]:
                for j in range(1, V + 1):
                    if graph[j][i]:
                        break
                else:
                    result.append(i)
                    visited[i] = True
                    for j in range(1, V + 1):
                        graph[i][j] = False
    print(f'#{T} {" ".join(map(str, result))}')
