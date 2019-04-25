for T in range(1, int(input()) + 1):
    N = int(input())
    string = ''
    for i in range(N):
        inputs = input().split()
        string += inputs[0] * int(inputs[1])
    i = 0
    result = ''
    while i < len(string):
        result += '\n' + string[i:i+10]
        i += 10
    print(f'#{T}{result}')
