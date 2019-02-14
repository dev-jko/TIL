for T in range(1, 11):
    building_num = int(input())
    buildings = list(map(int, input().split()))
    result = 0
    for i in range(2, building_num - 2):
        temp = buildings[i] - max(buildings[i - 1], buildings[i - 2], buildings[i + 1], buildings[i + 2])
        if temp > 0:
            result += temp
    print(f'#{T} {result}')
