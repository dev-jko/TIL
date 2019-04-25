grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for T in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    scores = []
    k = 0
    for i in range(N):
        temp = list(map(int, input().split()))
        scores.append(temp[0] * 0.35 + temp[1] * 0.45 + temp[2] * 0.20)
        if i == K - 1:
            k = scores[i]
    scores.sort(reverse=True)
    rank = scores.index(k)
    d = N//10
    for i in range(N):
        if d * i <= rank < d * (i + 1):
            result = grades[i]
            break
    print(f'#{T} {result}')
