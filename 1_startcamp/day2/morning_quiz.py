print('good morning')

# 1. 평균
my_score = [79, 84, 66, 93]
my_average = sum(my_score)/len(my_score)
print(my_average)
print(type(my_average))

# 2. 
your_score = {
    '수학':87,
    '국어':83,
    '영어':76,
    '도덕':100
}
your_average = sum(your_score.values())/len(your_score)
print(your_average)
print(type(your_average))
print(type(your_score.values()))

