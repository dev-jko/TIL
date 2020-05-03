# https://www.acmicpc.net/problem/14499
# 주사위 굴리기


class Dice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.top = 0
        self.bot = 0
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0

    def move(self, d):
        nx, ny = self.x + dxy[d][0], self.y + dxy[d][1]
        if 0 > nx or nx >= N or 0 > ny or ny >= M:
            return None
        self.x, self.y = nx, ny
        if d == 3:  # 위
            temp = self.up
            self.up = self.top
            self.top = self.down
            self.down = self.bot
            if data[nx][ny] == 0:
                data[nx][ny] = self.bot = temp
            else:
                self.bot = data[nx][ny]
                data[nx][ny] = 0
        elif d == 4:  # 아래
            temp = self.down
            self.down = self.top
            self.top = self.up
            self.up = self.bot
            if data[nx][ny] == 0:
                data[nx][ny] = self.bot = temp
            else:
                self.bot = data[nx][ny]
                data[nx][ny] = 0
        elif d == 2:  # 왼쪽
            temp = self.left
            self.left = self.top
            self.top = self.right
            self.right = self.bot
            if data[nx][ny] == 0:
                data[nx][ny] = self.bot = temp
            else:
                self.bot = data[nx][ny]
                data[nx][ny] = 0
        else:  # 오른쪽
            temp = self.right
            self.right = self.top
            self.top = self.left
            self.left = self.bot
            if data[nx][ny] == 0:
                data[nx][ny] = self.bot = temp
            else:
                self.bot = data[nx][ny]
                data[nx][ny] = 0
        return self.top


dxy = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]
N, M, x, y, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
cmds = list(map(int, input().split()))
dice = Dice(x, y)
for used in cmds:
    result = dice.move(used)
    if result is not None:
        print(result)
