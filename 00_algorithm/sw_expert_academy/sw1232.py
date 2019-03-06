# swea 1232.
# [S/W 문제해결 기본] 9일차 - 사칙연산


def postorder(index):
    if type(data[index]) == type(int) or data[index] == 0:
        return data[index]
    a, b = postorder(L[index]), postorder(R[index])
    if data[index] == '+':
        data[index] = a + b
    elif data[index] == '-':
        data[index] = a - b
    elif data[index] == '*':
        data[index] = a * b
    else:
        data[index] = a // b
    return data[index]


OPERATOR = ['+', '-', '*', '/']
for T in range(1, 11):
    N = int(input())
    data = [0 for _ in range(N + 1)]
    L = [0 for _ in range(N + 1)]
    R = [0 for _ in range(N + 1)]
    for _ in range(N):
        inputs = list(input().split())
        idx = int(inputs[0])
        if inputs[1] in OPERATOR:
            data[idx] = inputs[1]
            L[idx] = int(inputs[2])
            R[idx] = int(inputs[3])
        else:
            data[idx] = int(inputs[1])
    print('#{} {}'.format(T, postorder(1)))
