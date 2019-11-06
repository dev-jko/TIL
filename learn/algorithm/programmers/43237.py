def solution(budgets, M):
    if sum(budgets) <= M:
        return max(budgets)
    answer = 0
    start, end = 3, max(budgets)
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for b in budgets:
            total += b if b < mid else mid

        if total > M:
            end = mid - 1
        else:
            answer = max(answer, mid)
            start = mid + 1
    return answer


print(solution([120, 110, 140, 150], 485))
