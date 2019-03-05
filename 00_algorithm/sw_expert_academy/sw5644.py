def get_d(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_charge_set(BC):
    x, y, c, p = BC
    result = set({})
    start, end = x, x + 1
    for i in range(y - c, y + c + 1):
        if i < y:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
        for j in range(start, end):
            result.add((j, i))
    return result


dxy = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]

for T in range(1, int(input()) + 1):
    M, A = map(int, input().split())
    move = {
        'A': list(map(int, input().split())),
        'B': list(map(int, input().split()))
    }
    BCs = []
    for _ in range(A):
        BCs.append(list(map(int, input().split())))
    # move[A, B][이동 인덱스] 0 제자리, 1 위, 2 우, 3 하, 4 좌
    # BC[BC번호][x, y, 충전범위c, 처리량p]

    result = 0
    A = [(1, 1)]
    B = [(10, 10)]
    for i in range(M):
        A.append((A[i][0] + dxy[move['A'][i]][0], A[i][1] + dxy[move['A'][i]][1]))
        B.append((B[i][0] + dxy[move['B'][i]][0], B[i][1] + dxy[move['B'][i]][1]))
    # A, B [T초] -> T초일때 좌표

    print(get_charge_set(BCs[0]))

    print('#{} {}'.format(T, result))
