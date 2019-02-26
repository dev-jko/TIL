for T in range(1, 11):
    input()
    inputs = []
    for _ in range(100):
        inputs.append(list(map(int, input().split())))
    result = 0
    for i in range(100):
        temp = 0
        for j in range(100):
            if inputs[j][i] == 2 and temp == 1:
                result += 1
                temp = 2
            elif inputs[j][i] == 1:
                temp = 1
    print(f'#{T} {result}')
