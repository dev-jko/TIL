def count_node(v):
    if v == 0:
        return 0
    return 1 + count_node(L[v]) + count_node(R[v])


for T in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    L = [0 for _ in range(E + 2)]
    R = [0 for _ in range(E + 2)]
    P = [0 for _ in range(E + 2)]
    inputs = list(map(int, input().split()))
    for i in range(0, len(inputs), 2):
        if L[inputs[i]] == 0:
            L[inputs[i]] = inputs[i + 1]
        else:
            R[inputs[i]] = inputs[i + 1]
        P[inputs[i + 1]] = inputs[i]
    root = 0
    for i in range(1, len(P)):
        if i == 0:
            root = i
    result = count_node(N)
    print('#{} {}'.format(T, result))
