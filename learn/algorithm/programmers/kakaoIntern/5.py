def solution(stones, k):
    s, e = 1, 200000000
    answer = 0
    while s <= e:
        mid = (s + e) // 2
        if check(mid, stones[:], k):
            answer = max(answer, mid)
            s = mid + 1
        else:
            e = mid - 1
    return answer


def check(n, stones, k):
    n -= 1
    for i in range(len(stones)):
        stones[i] -= n
    cnt = k
    for i in range(len(stones)):
        if stones[i] <= 0:
            cnt -= 1
            if cnt == 0:
                return False
        else:
            cnt = k
    return True


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
# 3
