# https://www.acmicpc.net/problem/2635
# 수 이어가기


N = int(input())
result = []
for i in range(N, -1, -1):
    temp = [N, i]
    pp, p = N, i
    while pp >= p:
        temp.append(pp - p)
        pp, p = p, pp - p
    if len(result) < len(temp):
        result = temp
print('{}\n{}'.format(len(result), ' '.join(map(str, result))))
