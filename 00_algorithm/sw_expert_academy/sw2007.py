for T in range(1, int(input()) + 1):
    string = input()
    for i in range(1, 30):
        temp = string[:i] * (30 // i)
        if temp == string[:len(temp)]:
            result = i
            break
    print(f'#{T} {result}')
