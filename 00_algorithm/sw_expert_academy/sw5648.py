# 5648. [모의 SW 역량테스트] 원자 소멸 시뮬레이션

dxy = [[0, 1], [0, -1], [-1, 0], [1, 0]]


# 이동 방향은 상(0), 하(1), 좌(2), 우(3)

class Atom:
    def __init__(self, x, y, d, k):
        self.x = x
        self.y = y
        self.d = d
        self.k = k
        self.alive = True


def my_key(case):
    return case[0], case[1], case[2]


for T in range(1, int(input()) + 1):
    N = int(input())
    result = 0
    atoms = []
    for _ in range(N):
        x, y, d, k = map(int, input().split())
        atoms.append(Atom(x, y, d, k))

    case = []
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if atoms[i].d == 0:
                if atoms[j].d == 1 and atoms[i].x == atoms[j].x:
                    case.append((abs(atoms[i].y - atoms[j].y) // 2, i, j))
                elif atoms[j].d == 2 or atoms[j].d == 3:
                    if abs(atoms[i].x - atoms[j].x) == abs(atoms[i].y - atoms[j].y):
                        case.append((abs(atoms[i].x - atoms[j].x), i, j))

            elif atoms[i].d == 1:
                if atoms[j].d == 0 and atoms[i].x == atoms[j].x:
                    case.append((abs(atoms[i].y - atoms[j].y) // 2, i, j))
                elif atoms[j].d == 2 or atoms[j].d == 3:
                    if abs(atoms[i].x - atoms[j].x) == abs(atoms[i].y - atoms[j].y):
                        case.append((abs(atoms[i].x - atoms[j].x), i, j))

            elif atoms[i].d == 2:
                if atoms[j].d == 3 and atoms[i].y == atoms[j].y:
                    case.append((abs(atoms[i].x - atoms[j].x) // 2, i, j))
                elif atoms[j].d == 0 or atoms[j].d == 1:
                    if abs(atoms[i].x - atoms[j].x) == abs(atoms[i].y - atoms[j].y):
                        case.append((abs(atoms[i].x - atoms[j].x), i, j))

            elif atoms[i].d == 3:
                if atoms[j].d == 2 and atoms[i].y == atoms[j].y:
                    case.append((abs(atoms[i].x - atoms[j].x) // 2, i, j))
                elif atoms[j].d == 0 or atoms[j].d == 1:
                    if abs(atoms[i].x - atoms[j].x) == abs(atoms[i].y - atoms[j].y):
                        case.append((abs(atoms[i].x - atoms[j].x), i, j))
    case.sort(key=my_key)
    temp = set()
    time = 0
    for i in range(len(case)):
        if case[i][0] > time or i == len(case) - 1:
            for j in temp:
                atoms[j].alive = False
                result += atoms[j].k
            time = case[i][0]
            temp.clear()
            if atoms[case[i][1]].alive and atoms[case[i][2]].alive:
                temp.add(case[i][1])
                temp.add(case[i][2])
        else:
            if atoms[case[i][1]].alive and atoms[case[i][2]].alive:
                temp.add(case[i][1])
                temp.add(case[i][2])

    print('#{} {}'.format(T, result))

# 0.20904s 시간초과
# 0.13195s 틀림
