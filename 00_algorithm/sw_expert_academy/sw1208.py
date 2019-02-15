for T in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    cnt = [0 for _ in range(101)]
    for i in boxes:
        cnt[i] += 1

    front = 1
    back = 100
    while front < back and dump >= 0:
        while cnt[front] == 0 and front < back:
            front += 1
        while cnt[back] == 0 and front < back:
            back -= 1
        if dump == 0:
            break
        t = cnt[back] - cnt[front]
        if t >= 0:
            if dump >= cnt[front]:
                cnt[front + 1] += cnt[front]
                cnt[back - 1] += cnt[front]
                cnt[back] -= cnt[front]
                dump -= cnt[front]
                cnt[front] = 0
            else:
                dump = 0
        else:
            if dump >= cnt[back]:
                cnt[front + 1] += cnt[back]
                cnt[front] -= cnt[back]
                cnt[back - 1] += cnt[back]
                dump -= cnt[back]
                cnt[back] = 0
            else:
                dump = 0
    print(f'#{T} {back - front}')
