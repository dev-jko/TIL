# 5653. [모의 SW 역량테스트] 줄기세포배양


# 4 30

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]


#     상태 0 빈칸, 1 비활성, 2 활성, 3 죽음
class Cell:
    def __init__(self, x, y, life=0, current_time=0):
        self.x = x
        self.y = y
        self.life = life
        self.timer = life
        self.state = 1
        self.born_time = current_time

    def tick(self, current_time):
        new = set({})
        state12 = set({})
        state23 = set({})
        if self.state == 1 or self.state == 2:
            self.timer -= 1
            if self.timer <= 0:
                if self.state == 1:
                    self.state = 2
                    self.timer = self.life
                    state12.add(self)
                else:
                    self.state = 3
                    state23.add(self)
        if self.state == 2:
            for dx, dy in dxy:
                nx, ny = self.x + dx, self.y + dy
                temp = grid.get_cell_state1(nx, ny)
                if temp is not None:
                    if temp.born_time == current_time and self.life > temp.life:
                        temp.life = temp.timer = self.life
                else:
                    temp = grid.get_cell_state23(nx, ny)
                    if temp is None:  #빈 경우
                        new.add(Cell(nx, ny, self.life, current_time))
        return new, state12, state23


class Grid:
    def __init__(self):
        self.state1 = set({})
        self.state2 = set({})
        self.state3 = set({})
        self.current_time = 0

    def tick(self):
        self.current_time += 1
        temp = None
        for cell in self.state1:
            temp = cell.tick(self.current_time)
        self.state1 |= temp[0]
        self.state1 -= temp[1]
        self.state2 |= temp[1]
        self.state2 -= temp[2]
        self.state3 |= temp[2]
        for cell in self.state2:
            temp = cell.tick(self.current_time)
        self.state1 |= temp[0]
        self.state1 -= temp[1]
        self.state2 |= temp[1]
        self.state2 -= temp[2]
        self.state3 |= temp[2]

    def get_cell_state1(self, x, y):
        for cell in self.state1:
            if cell.x == x and cell.y == y:
                return cell
        return None

    def get_cell_state23(self, x, y):
        for cell in self.state2:
            if cell.x == x and cell.y == y:
                return cell
        for cell in self.state3:
            if cell.x == x and cell.y == y:
                return cell
        return None


for T in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    # n 세로크기, M 가로크기, k 시간
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    grid = Grid()
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0:
                grid.state1.add(Cell(i, j, data[i][j], 0))
    for _ in range(K):
        grid.tick()
    # 배양을 K시간 시킨 후 배양 용기에 있는 살아있는 줄기 세포(비활성 상태 + 활성 상태)의 개수
    result = len(grid.state1) + len(grid.state2)
    print('#{} {}'.format(T, result))
