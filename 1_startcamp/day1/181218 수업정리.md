# 181218 정리

## 1. 개발환경 설정

* chocolatey
  * 윈도우 패키지 매니저
* python v3.6.7
* git
  * version control system
* vscode
  * code editor
* chrome
  * browser

## 2. 단축키

### vscode

* ctrl+`
  * terminal 포커스
* ctrl+1
  * 에디터창 포커스



## 3. list

* #### 리스트 생성과 접근

```python
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
```

리스트 안에는 타입에 상관 없이 넣을 수 있다.

이때 `'spider'`에 접근하려면 `mcu[0][1]`



* #### 리스트 + 연산

```python
nums = [1,2,3,4]
print(nums)
nums += [5]
print(nums)
```

리스트에 리스트를 더하면 하나로 합쳐진다.



* #### 리스트 요소 삭제

```python
del(team[2:4])

del(nums[2])
```

리스트에서 특정 인덱스를 삭제하려면 `del()`함수를 사용한다.





## 4. dict

```python
my_info = {
    'name' : 'neo',
    'job' : 'hacker',
    'mobile' : '01001011010',
    'email' : 'neo@hphk.kr' 
}
print(my_info['email'])


hphk = [
    {
        'name':'john',
        'email':'john@hphk.kr'
    },
    {
        'name' : 'neo',
        'email' : 'neo@hphk.kr' 
    },
    {
        'name' : 'tak',
        'email' : 'tak@hphk.kr' 
    }
]
print(hphk[2]['name'])

```

dict는 key와 value가 한 세트이다.

my_info의 email 값에 접근하려면 `my_info['email']`

hphk의 3번째 name 값에 접근하려면 `hphk[2]['name']`



## 5. function

```python
scores = [45, 60, 78, 88]
high_score = max(scores)
print(high_score)
low_score = min(scores)
print(low_score)

round(1.8)

first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
full = first + second
full_sorted = sorted(full)
reverse_sorted = sorted(full, reverse=True)
print(reverse_sorted)
```





## 6. method

메서드는 함수다! 다만 **[주어].동사()**의 형식으로 이루어지며, [주어] 자리에 오는 object들이 할 수 있는 행동(함수)들이다.

```python
my_list = [4, 7, 9, 1, 3, 6]

print(my_list.index(4))
my_list.reverse()
print(my_list)

lang = 'python'
samsung = ['elec', 'sds', 's1']

lang.capitalize
lang.replace('on', 'off')

samsung.index('sds')
samsung.append('bio')
```



| str        | int   | list             | bool    |
| ---------- | ----- | ---------------- | ------- |
| `'python'` | `100` | `['a', 3, True]` | `False` |

