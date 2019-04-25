days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
for T in range(1, int(input()) + 1):
    inputs = list(map(int, input().split()))
    result = inputs[3] - inputs[1] + 1
    for i in range(inputs[0], inputs[2]):
        result += days[i]
    print(f'#{T} {result}')
