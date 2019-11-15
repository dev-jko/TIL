# 완전탐색 자바로 제출하면 그냥 됨
# 파이썬으로 제출하려면 코드 최적화 필요

N = int(input())
cnt = 0
for k in range(1, N + 1):
    for c in str(k):
        if c in ('3', '6', '9'):
            cnt += 1
print(cnt)
