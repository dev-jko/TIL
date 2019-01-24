memo = [0, 1]
def fibonacci(n):
    if n < 2:
        return n
    elif len(memo) < n:
        return memo[n]
    else:
        memo.append(fibonacci(n - 1) + fibonacci(n - 2))
    return memo[n]


print(fibonacci(2))