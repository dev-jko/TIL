# 4408. 자기 방으로 돌아가기


for T in range(1, int(input()) + 1):
    N = int(input())
    data = [sorted(list(map((lambda x:(int(x) + (2 if int(x) % 2 else 1))//2), input().split()))) for _ in range(N)]
    cnt = [0] * 201
    for i in range(N):
        for j in range(data[i][0], data[i][1] + 1):
            cnt[j] += 1
    print('#{} {}'.format(T, max(cnt)))
