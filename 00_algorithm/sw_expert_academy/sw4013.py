LEFT = -2
RIGHT = 2


class magnet:
    def __init__(self, mag_id, gear):
        self.mag_id = mag_id
        self.gear = gear
        self.top = 0

    def turn(self, direction, num):
        self.top = self.top - (direction * (num % 8)


for T in range(1, int(input())):
    K = int(input())
    gear = []
    for _ in range(4):
        gear.append(list(input().split()))
    turns = []
    # 12시 방향부터 시작, 날은 8개
    # turns[자석 번호][회전 방향] 시계방향=1, 반시계= -1
    for _ in range(K):
        turns.append(list(map(int, input().split())))
        turns[-1][0] -= 1
    idx = [0, 0, 0, 0]
    result = 0
    print('#{} {}'.format(T, result))
