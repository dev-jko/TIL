# https://www.acmicpc.net/problem/15650
# N과 M (2)

import itertools

N, M = map(int, input().split())
for i in itertools.combinations(range(1, N + 1), M):
    print(*i)
