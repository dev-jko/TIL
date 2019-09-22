from itertools import permutations

numbers = sorted(list(map(int, input().strip().split(' '))))
k = int(input())
print("".join(map(str, list(permutations(numbers))[k - 1])))
