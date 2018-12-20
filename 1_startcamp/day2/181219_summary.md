# 181219 수업정리

## 1.  convention

### python

* class
  * 대문자로 시작

## 2. list, dict 문제풀이

* list 평균 구하기

  ```python
  my_score = [79, 84, 66, 93]
  my_average = sum(my_score)/len(my_score)
  print(my_average)
  print(type(my_average))
  ```



* dict 평균 구하기

  ```python
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
  ```

  `your_score.values()`의 타입은 `dict_values`이다.

* 도시별 평균 온도 구하기

  ```python
  cities_temp = {
      '서울': [-6, -10, 5],
      '대전': [-3, -5, 2],
      '광주': [0, -5, 10],
      '구미': [2, -2, 9]
  }
  
  for key, value in cities_temp.items():
      print(key+':', round(sum(value)/len(value), 1))
  ```

  print문은 `'{0} : {1}'.format(key, round(sum(value)/len(value), 1)) `식으로 표현 가능

* 도시 중 최근 3일간 가장 추웠던 곳, 가장 더웠던 곳 구하기

  ```python
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
  ```

  `list.append()`방식으로 결과물을 저장하면 최대 최소인 값이 여러개일 때도 표현 가능



## 3. 사용한 것들

* C9
* github
* codecademy
* bootstrap





