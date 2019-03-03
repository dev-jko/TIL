# https://www.acmicpc.net/problem/15654
# N과 M (5)
import itertools

N, M = map(int, input().split())
for i in itertools.permutations(sorted(map(int, input().split())), M):
    print(*i)
