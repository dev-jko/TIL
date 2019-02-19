import my_std

for T in range(1, int(input()) + 1):
    result = 0
    boxes = []
    for _ in range(int(input())):
        boxes.append(list(map(int, input().split())))
    grid = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(len(boxes)):
        for j in range(boxes[i][0], boxes[i][2] + 1):
            for k in range(boxes[i][1], boxes[i][3] + 1):
                if grid[j][k] not in (0, -1) and boxes[i][4] != grid[j][k]:
                    grid[j][k] = -1
                elif grid[j][k] == 0:
                    grid[j][k] = boxes[i][4]
                if grid[j][k] == -1:
                    result += 1
    print(f'#{T} {result}')
