# 3752. 가능한 시험 점수

for T in range(1, int(input()) + 1):
    N = int(input())
    data = list(map(int, input().split()))
    sums = {0}
    for i in data:
        for j in list(sums):
            sums.add(j + i)
    print('#{} {}'.format(T, len(sums)))
