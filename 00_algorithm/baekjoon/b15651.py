# https://www.acmicpc.net/problem/15651
# N과 M (3)

import itertools

N, M = map(int, input().split())
for i in itertools.product(range(1, N + 1), repeat=M):
    print(*i)
