#  https://www.acmicpc.net/problem/15649
#  N과 M (1)

from itertools import permutations

N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
for a in permutations(arr, M):
    print(*a, sep=' ')