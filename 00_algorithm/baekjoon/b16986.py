from itertools import permutations

N, K = map(int, input().split())
data = [0]
for i in range(1, N + 1):
    data.append(list(map(int, input().split())))
    data[i].insert(0, 0)
gestures = [[]]
gestures.append(list(map(int, input().split())))
gestures.append(list(map(int, input().split())))
result = 0
if N >= K:
    for perms in permutations(range(1, N + 1)):
        gestures[0] = perms
        win_cnt = [0, 0, 0]
        idx = [0, 0, 0]
        h1, h2 = 0, 1
        while not win_cnt.count(K) and idx[h1] < len(gestures[h1]) and idx[h2] < len(gestures[h2]):
            if h1 > h2:
                h1, h2 = h2, h1
            if data[gestures[h1][idx[h1]]][gestures[h2][idx[h2]]] == 2:
                win_cnt[h1] += 1
                idx[h1] += 1
                idx[h2] += 1
                h2 = 3 - h1 - h2
            else:
                win_cnt[h2] += 1
                idx[h1] += 1
                idx[h2] += 1
                h1 = 3 - h1 - h2
        if win_cnt[0] == K:
            result = 1
            break
print(result)
