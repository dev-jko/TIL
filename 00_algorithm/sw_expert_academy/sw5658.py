# swea 5658.
# [모의 SW 역량테스트] 보물상자 비밀번호

for T in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    inputs = input()
    inputs += inputs
    n = N // 4
    num_set = set({})
    for i in range(N):
        num_set.add(inputs[i:i + n])
    result = []
    for num in num_set:
        result.append(int(num, 16))
    result.sort(reverse=True)
    print('#{} {}'.format(T, result.pop(K - 1)))
