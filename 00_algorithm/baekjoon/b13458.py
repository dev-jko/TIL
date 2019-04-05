# https://www.acmicpc.net/problem/13458
# 시험 감독


N = int(input())
data = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0
for n in data:
    result += 1
    n -= B
    if n > 0:
        result += n // C + (1 if n % C else 0)
print(result)
