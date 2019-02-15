for T in range(1, int(input()) + 1):
    K, N, M = map(int, input().split())
    # k = 한번 충전으로 이동 가능 정거장 수
    # n = 종점 번호
    # m = 충전기 설치된 곳 수
    lines = list(map(int, input().split()))

    result = 0
    now = 0
    check = True
    while check:
        if now + K >= N:
            break
        for line in lines[::-1]:
            if now + K >= line and now != line:
                result += 1
                now = line
                break
            if now >= line:
                check = False
                result = 0
                break
        else:
            check = False
            result = 0
            break
    print(f'#{T} {result}')
