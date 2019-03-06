from collections import deque

q = deque()
for T in range(1, 11):
    N, S = map(int, input().split())
    graph = [[0 for _ in range(101)] for _ in range(101)]
    inputs = list(map(int, input().split()))
    D = [-1 for _ in range(101)]
    for i in range(0, len(inputs), 2):
        graph[inputs[i]][inputs[i + 1]] = 1
    q.clear()
    q.append(S)
    D[S] = 0
    while len(q):
        v = q.popleft()
        for i in range(101):
            if graph[v][i] == 1 and D[i] == -1:
                D[i] = D[v] + 1
                q.append(i)
    result = [0, -1]
    for i in range(100, 0, -1):
        if D[i] > result[1]:
            result[0], result[1] = i, D[i]
    print('#{} {}'.format(T, result[0]))
