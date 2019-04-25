def find_winner(cards, start, end):
    if start == end:
        return start
    w1 = find_winner(cards, start, (start + end) // 2)
    w2 = find_winner(cards, (start + end) // 2 + 1, end)
    if cards[w1] == 1:
        if cards[w2] == 2:
            return w2
        return w1
    elif cards[w1] == 2:
        if cards[w2] == 3:
            return w2
        return w1
    else:
        if cards[w2] == 1:
            return w2
        return w1


for T in range(1, int(input()) + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    winner = find_winner(cards, 0, N - 1) + 1
    print(f'#{T} {winner}')
