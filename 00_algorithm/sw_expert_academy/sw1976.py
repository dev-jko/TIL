for T in range(1, int(input()) + 1):
    inputs = list(map(int, input().split()))
    h = inputs[0] + inputs[2]
    m = inputs[1] + inputs[3]
    if m >= 60:
        h += 1
        m %= 60
    if h == 24:
        h = 12
    elif h > 12:
        h %= 12
    print(f'#{T} {h} {m}')
