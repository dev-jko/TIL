def inorder(node, result):
    if node == 0:
        return
    inorder(L[node], result)
    result += data[node]
    inorder(R[node], result)


for T in range(1, 11):
    N = int(input())
    data = [0 for _ in range(N + 1)]
    L = [0 for _ in range(N + 1)]
    R = [0 for _ in range(N + 1)]
    for _ in range(N):
        temp = input().split()
        idx = int(temp[0])
        data[idx] = temp[1]
        if len(temp) >= 3:
            L[idx] = int(temp[2])
        if len(temp) >= 4:
            R[idx] = int(temp[3])
    result = []
    inorder(1, result)
    print('#{} {}'.format(T, ''.join(result)))
