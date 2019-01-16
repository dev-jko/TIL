for T in range(1, int(input()) + 1):
    result = 1
    string = input().strip()
    for i in range(len(string)//2 + 1):
        if string[i] != string[-i-1]:
            result = 0
            break
    print(f'#{T} {result}')