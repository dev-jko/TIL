# swea 5644
# 무선충전

# move[A, B][이동 인덱스] 0 제자리, 1 위, 2 우, 3 하, 4 좌
# BC[BC번호][x, y, 충전범위c, 처리량p]
# A, B [T초] -> T초일때 좌표
# BC_sets[BC번호] -> 충전범위 셋


def get_charge_set(BC):
    x, y, c, p = BC
    result = set({})
    start, end = x, x + 1
    for i in range(y - c, y + c + 1):
        for j in range(start, end):
            result.add((j, i))
        if i < y:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    return result


dxy = [[0, 0], [0, -1], [1, 0], [0, 1], [-1, 0]]
for T in range(1, int(input()) + 1):
    M, A = map(int, input().split())
    move = {
        'A': list(map(int, input().split())),
        'B': list(map(int, input().split()))
    }
    BCs = [[0, 0, 0, 0]]
    for _ in range(A):
        BCs.append(list(map(int, input().split())))
    a = [(1, 1)]
    b = [(10, 10)]
    for i in range(M):
        a.append((a[i][0] + dxy[move['A'][i]][0], a[i][1] + dxy[move['A'][i]][1]))
        b.append((b[i][0] + dxy[move['B'][i]][0], b[i][1] + dxy[move['B'][i]][1]))
    BC_sets = []
    for BC in BCs:
        BC_sets.append(get_charge_set(BC))
    result = 0
    for i in range(M + 1):
        a_bc = [0, 0]
        b_bc = [0, 0]
        for j in range(1, A + 1):
            if a[i] in BC_sets[j]:
                if BCs[a_bc[0]][3] < BCs[j][3]:
                    a_bc[0], a_bc[1] = j, a_bc[0]
                elif BCs[a_bc[1]][3] < BCs[j][3]:
                    a_bc[1] = j
            if b[i] in BC_sets[j]:
                if BCs[b_bc[0]][3] < BCs[j][3]:
                    b_bc[0], b_bc[1] = j, b_bc[0]
                elif BCs[b_bc[1]][3] < BCs[j][3]:
                    b_bc[1] = j
        if a_bc[0] == b_bc[0]:
            result += (BCs[a_bc[0]][3] + BCs[b_bc[1]][3]) if BCs[a_bc[1]][3] < BCs[b_bc[1]][3] else (BCs[b_bc[0]][3] + BCs[a_bc[1]][3])
        else:
            result += BCs[a_bc[0]][3] + BCs[b_bc[0]][3]
    print('#{} {}'.format(T, result))
