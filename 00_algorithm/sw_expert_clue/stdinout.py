def change(file_name):
    import sys
    file_name = file_name[:-3]
    try:
        with open(f'{file_name}.txt', 'r') as f:
            sys.stdin = f
    except FileNotFoundError:
        print('input file이 없습니다.')
        sys.exit()
    finally:
        sys.stdout = open(f'{file_name}output.txt', 'w')
