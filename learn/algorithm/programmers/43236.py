def solution(distance, rocks, n):
    rocks.sort()
    rocks = [0] + rocks + [distance]
    answer = 0
    s, e = 1, distance
    while s <= e:
        mid = (s + e) // 2
        if check(mid, n, rocks):
            answer = max(answer, mid)
            s = mid + 1
        else:
            e = mid - 1
    return answer


def check(k, n, rocks):
    i, before = 1, 0
    while i < len(rocks):
        gap = rocks[i] - before
        if gap < k:
            n -= 1
            if n < 0:
                return False
        else:
            before = rocks[i]
        i += 1
    return True


print(solution(25, [2, 14, 11, 21, 17], 2))
# 4
