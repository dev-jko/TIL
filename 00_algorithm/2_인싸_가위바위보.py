from itertools import permutations


def game(h1, h2):
    if data[h1][h2] == 2:
        return 1
    return 2


N, K = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
gestures = [[-1 for _ in range(20)]]
gestures.append(list(map(int, input().split())))
gestures.append(list(map(int, input().split())))
result = 0
if N >= K:
    contin = True
    for perms in list(permutations(range(1, N + 1))):
        gestures[0] = perms
        win_cnt = [0, 0, 0]
        for hand in gestures[0]:




print(result)
