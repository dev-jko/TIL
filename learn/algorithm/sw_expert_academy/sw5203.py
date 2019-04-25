# 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임


def is_run_or_triplet(card_cnt):
    for i in range(len(card_cnt)):
        if card_cnt[i] >= 3:
            return True
        elif i < len(card_cnt) - 2 and (card_cnt[i] and card_cnt[i + 1] and card_cnt[i + 2]):
            return True
    return False


for T in range(1, int(input()) + 1):
    inputs = list(map(int, input().split()))
    result = 0
    p1 = [0 for _ in range(10)]
    p2 = [0 for _ in range(10)]
    for i in range(0, len(inputs), 2):
        p1[inputs[i]] += 1
        p2[inputs[i + 1]] += 1
        if is_run_or_triplet(p1):
            result = 1
            break
        elif is_run_or_triplet(p2):
            result = 2
            break
    print(f'#{T} {result}')
