def solution(brown, red):
    for i in range(1, int(red ** 0.5) + 1):
        if red % i != 0:
            continue
        row = red // i
        b = (row + 2) * (i + 2) - red
        if b == brown:
            return [row + 2, i + 2]
    return 0


def solution(brown, red):
    for i in range(3, 25000):
        for j in range(3, i + 1):
            r = (i - 2) * (j - 2)
            b = i * j - r
            if b == brown and r == red:
                return [i, j]
    return -1


print(solution(10, 2))  # 4,3
print(solution(8, 1))  # 3,3
print(solution(24, 24))  # 8,6
