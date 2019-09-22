n, m = map(int, input().strip().split(' '))
dest = tuple(map(int, input().strip().split(' ')))
if 0 <= dest[0] < 25 and 0 <= dest[1] < 25:
    if dest == (0, 0):
        print(0)
        print(1)
    else:
        answer = [[0] * (dest[0] + 1) for _ in range(dest[1] + 1)]
        for i in range(dest[1] + 1):
            answer[i][0] = 1
        for i in range(dest[0] + 1):
            answer[0][i] = 1
        for i in range(1, dest[1] + 1):
            for j in range(1, dest[0] + 1):
                answer[i][j] = answer[i][j - 1] + answer[i - 1][j]

        print(sum(dest))
        print(answer[-1][-1])
else:
    print("fail")
