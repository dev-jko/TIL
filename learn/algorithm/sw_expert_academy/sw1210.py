for T in range(1, 11):
    input()
    ladder = []
    for _ in range(100):
        ladder.append(list(input().strip().split(' ')))
    x = ladder[-1].index('2')
    y = len(ladder) - 1
    while y > 0:
        if x > 0 and ladder[y][x - 1] == '1':
            ladder[y][x] = '0'
            x -= 1
        elif x < len(ladder[0]) - 1 and ladder[y][x + 1] == '1':
            ladder[y][x] = '0'
            x += 1
        elif ladder[y - 1][x] == '1':
            ladder[y][x] = '0'
            y -= 1
    print(f'#{T} {x}')
