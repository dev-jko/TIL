numbers = [1,2,3] # 변수 이름은 뜻을 담아서 짓자

family = ['mom', 1.64, 'dad', 1.75, 'sister', 1.78]

mcu = [
    ['iron','capt'],
    ['spider'],
    ['xmen']
]
disney = mcu[0]
print(disney)
print(disney[1])
print(mcu[0][1])

numbers = list(range(100))
numbers1 = numbers[1:10]
numbers2 = numbers[2:5] # [start:end] => start는 포함, end는 안 포함
print(numbers1)
print(numbers2)

x = ['x', 'y', 'z', True, 123, ['a', 'b', 'c']]
my_bool1 = x[3]
my_bool2 = x[-3]
print(my_bool1, my_bool2)


