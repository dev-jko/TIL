print('good morning')

# 1. 평균
my_score = [79, 84, 66, 93]
my_average = sum(my_score)/len(my_score)
print(my_average)
print(type(my_average))

# 2.
your_score = {
    '수학': 87,
    '국어': 83,
    '영어': 76,
    '도덕': 100
}
your_average = sum(your_score.values())/len(your_score)
print(your_average)
print(type(your_average))
print(type(your_score.values()))

# 3.
cities_temp = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -5, 10],
    '구미': [2, -2, 9]
}

# 도시별 온도 평균
# 서울: ?
# 대전: ?
for key, value in cities_temp.items():
    print(key+':', round(sum(value)/len(value), 1))


# 4. 도시중 최근 3일간 가장 추웠던 곳, 가장 더웠던 곳
# Hottest: ?, Coldest: ?
hottest = {'name': '', 'temp': -999}
coldest = {'name': '', 'temp': 999}

hottest_result = []
coldest_result = []

for key, value in cities_temp.items():
    for temp in value:
        if hottest['temp'] < temp:
            hottest['name'] = key
            hottest['temp'] = temp
            hottest_result.append(key)
        if coldest['temp'] > temp:
            coldest['name'] = key
            coldest['temp'] = temp
            coldest_result.append(key)

print('Hottest:', hottest['name'])
print('Coldest:', coldest['name'])
print('Hottest:', hottest_result)
print('Coldest:', coldest_result)
