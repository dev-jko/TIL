print(__name__)

def average(numbers):
    return sum(numbers) / len(numbers)


def cube(number):
    return number*number*number

def main():
    my_score = [79, 84, 66, 93]
    print(average(my_score))
    print(cube(3))

if __name__ == '__main__':
    main()