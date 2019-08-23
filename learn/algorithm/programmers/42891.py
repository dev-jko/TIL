def solution(food_times, k):
    food = [0] + sorted(food_times)
    foods = len(food)
    for i in range(1, foods):
        length = (foods - i) * (food[i] - food[i - 1])
        if k >= length:
            k -= length
            continue
        length = foods - i
        k %= length
        if k < length:
            index = -1
            for idx, time in enumerate(food_times):
                if time >= food[i]:
                    k -= 1
                    if k < 0:
                        index = idx
                        break
            return index + 1
    return -1
