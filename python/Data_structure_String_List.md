# 데이터 구조

## 문자열 string

#### 특징

- immutable : 변경할 수 없다

  ```python
  a = 'hello word'
  a[-1] = 'a'
  
  # type error : 'str' object does not support item assignment
  ```

  

- iterable : 순회 가능하다

  ```python
  a = '123'
  for char in a:
      print(char)
  
  # 1
  # 2
  # 3
  ```

- Built-in Function 적용시 원본데이터 유지



#### 문자열 자르기

-  s[start:stop:step]

  ```python
  a = 'abcdefghi'
  
  print(a[2:5]) # cde
  print(a[-6:-2]) # defg
  
  print(a[2:5:2])	# cd
  print(a[-6:-1:3]) # dg
  print(a[2:5:-1]) #     '' 해당되는 값이 없다면 빈 문자열 제공
  print(a[5:2:-1]) # fed
  
  print(a[::]) # abcdefghi
  print(a[::-1]) # ihgfedcba
  ```

  

#### 메서드

##### .find(x) : x의 첫 번째 위치를 반환, 없으면 오류 발생

```python
'apple'.index('p') # 1 
```

##### .index(x) : x의 첫 번째 위치를 반환, 없으면 -1

```python
'apple'.find('p') # 1 
```

##### .replace(old, new[,count]) : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환

```python
# .replace(old, new[,count]) 베커스-나우르 표기법 [] 선택적인자

'coone'.replace('o', 'a') # caane 바뀔 글자를 새로운글자로 바꿔서 반환
'cooone'.replace('o', 'i', 2) # ciione 카운트 지정시 해당개수만큼 시행

# 원본데이터 바뀌지 않는다. 활용하려면? => 변수에 넣어야!
result = a.replace('y','h')
print(a)
print(result)
```

##### .strip([chars]) : 특정 문자 지정하여 제거, 미지정시 공백 제거

```python
'    와우!\n'.strip() # '와우!'
'안녕하세요???'.rstrip('?') #'안녕하세요'
'    와우!\n'.lstrip() # '와우!'

# 원본데이터는 바뀌지 않는다. 활용하려면? => 변수에 넣어야!
result = a.strip()
print(a)
print(result)
```

##### .split([char]) : 문자열을 특정 단위로 나눠 리스트로 반환 (중요!!)

```python
'a,b,c'.split('_') # [a,b,c]
'a b c'.split()	#['a', 'b', 'c']

# 원본데이터는 바뀌지 않는다. 활용하려면? => 변수에 넣어야!
result = a.split()
print(a)
print(result)

# 1 2 3 4 5 로 입력된 input str 데이터를 int로 바꾸려면?
# sol1 
i = input()
numbers_str = i.split(' ') # char(띄어쓰기) 기준으로 분리

# sol2
result = []
for number_str in numbers_str:
    result += [int(number_str)]
    # result.append(int(number_str))
print(result)
# [1, 2, 3, 4, 5]

# sol3
result = map(int, input().split(' '))
print(list(result))
# [1, 2, 3, 4, 5]
```

##### 'separator'.join([iterable]) : 반복가능한 요소들을 구분자로 합쳐 문자열로 반환

``` python
'!'.join('love') # 'l!o!v!e'
' '.join(['3', '5']) # '3 5'

# 원본데이터는 바뀌지 않고 수정한 결과를 반환. 활용하려면? => 변수에 넣어야!
result = '!'.join(a)
print(a)
print(result)
```



#### 문자열 관련 검증 메소드

##### .isalpha() :알파벳 문자 여부

```python
'abc'.isalpha() # True
'ㄱㄴㄷ'.isalpha() # True
```



## 리스트 list

#### 특징

- mutable : 변경 가능하다
- ordered : 순서가 있다
- iterable : 순회 가능하다
- Built-in Function 적용시 원본데이터 변경



#### 값 추가 및 삭제

##### .append(x) : 리스트에 값을 추가

```python
cafe = ['starbucks', 'holly']
cafe.append('presso')

# ['starbucks', 'holly', 'presso']
```

##### .extend(iterable) : 리스트에 iterable의 항목을 추가

```python
cafe = ['starbucks', 'holly']
cafe.extend(['presso'])
# ['starbucks', 'holly', 'presso']

cafe = ['starbucks', 'holly']
cafe += ['presso']
# ['starbucks', 'holly', 'presso']

cafe = ['starbucks', 'holly']
cafe += ['presso']
# ['starbucks', 'holly', 'p', 'r', 'e', 's', 's', 'o']
```

##### .append(x) vs .extend(iterable) 

```python
# append는 개별 요소가, extend는 리스트 내의 데이터가 들어간다.
cafe = ['starbucks', 'tomntoms', 'hollys']

cafe.append(['coffeenie'])
print(cafe)
# ['starbucks', 'tomntoms', 'hollys', ['coffeenie']]

cafe.extend(['twosome'])
print(cafe)
# ['starbucks', 'tomntoms', 'hollys','twosome']
```

##### .insert(i, x) : 정해진 위치 i에 값을 추가

```python
cafe = ['starbucks', 'holly']
cafe.insert(0, 'start')
# ['start', starbucks', 'holly']
# i가 리스트 길이보다 큰 경우 맨 뒤에 추가된다
```

##### .pop(i) : 정해진 위치 i 값을 삭제하고, 그 항목을 반환, i 미지정시 마지막 값을 삭제하고 반환

```python
numbers = [1, 2, 3, 4, 5, 6]
result = numbers.pop()
print(result)
print(numbers)

# 6
# [1, 2, 3, 4, 5]
```



#### 리스트 탐색 및 정렬

##### .index(x) : x 값을 찾아 해당 index 값을 반환

```python
numbers = [1, 2, 3, 4, 1, 1]
numbers.index(3)
# 2
numbers.index(100)
# error
```

##### .count(x) : 원하는 값의 개수를 반환

```python
numbers = [1, 2, 3, 4, 1, 1]
numbers.count(1)
# 3
numbers.count(100)
# 0 

# 원하는 값을 모두 삭제하려면 다음과 같이 할 수 있습니다.
a = [1, 2, 1, 3, 4]
target_value = 1
for i in range(a.count(target_value)):
    a.remove(target_value)
print(a)
```

##### .sort() : 원본 리스트를 정렬함. 복사본은 없기 때문에 None 을 반환. 내장함수인 sorted 함수와 비교!!

```python
numbers = [3, 2, 5, 1]
result = numbers.sort() # 원본 변경(내 자신을 정렬), 복사본 없음
print(numbers, result)
# [1, 2, 3, 5] None

numbers = [3, 2, 5, 1]
result = sorted(numbers) # 원본 변경 없음
print(numbers, result)
# [3, 2, 5, 1] [1, 2, 3, 5]
```

##### .reverse() : 순서를 반대로 뒤집음(정렬하는 것이 아님)

```python
numbers = [3, 2, 5, 1]
result = numbers.reverse() # 원본 변경, 복사본 없음
print(numbers, result)
# [1, 5, 2, 3] None
```

##### 리스트 복사 : 리스트 복사본 바꿔도 원본 변경, 같은 리스트의 주소 참조

```python
origin_list = [1, 2, 3]
copy_list = origin_list
print(origin_list, copy_list)
# [1, 2, 3] [1, 2, 3]

copy_list[0] = 'hello'
print(origin_list, copy_list)
# ['hello', 2, 3] ['hello', 2, 3]
```

##### 얕은 복사1 : 서로 다른 결과가 나오려면 slice 연산자 활용

```python
a = [1, 2, 3]
b = a[:]
print(a, b)
b[0] = 5
print(a, b)

# [1, 2, 3] [1, 2, 3]
# [1, 2, 3] [5, 2, 3]
```

##### 얕은 복사2 : list() 활용하여 같은 원소를 가진 리스트지만 다른 주소

```python
a = [1, 2, 3]
b = list(a)
print(a, b)
b[0] = 5
print(a, b)

# [1, 2, 3] [1, 2, 3]
# [1, 2, 3] [5, 2, 3]

# 주의사항 : 가장 큰 리스트는 복사가 되지만 , 그 안의 리스트는 같은 값을 바라보고 있어 복사가 안됨
a = [1, 2, ['a', 'b']]
b = a[:]
print(a, b)
b[2][0] = 0
print(a, b)

# [1, 2, ['a', 'b']][1, 2, ['a', 'b']]
# [1, 2, [0, 'b']][1, 2, [0, 'b']]
```

##### 리스트 복사 - 깊은 복사(deep copy) 모듈 내 메서드

```python
import copy
a = [1, 2, ['a', 'b']]
b = copy.deepcopy(a)
print(a, b)
b[2][0] = 0
print(a, b) # 원본 리스트 유지

# [1, 2, ['a', 'b']][1, 2, ['a', 'b']]
# [1, 2, ['a', 'b']][1, 2, [0, 'b']]
```

##### List Comprehension

[<expression> for <변수> in <iterable>]

[<expression> for <변수> in <iterable> if <조건식>]

```python
# 1~3의 세제곱의 결과가 담긴 리스트

cubic_list = []
for number in range(1, 4):
    cubic_list.append(number ** 3)
print(cubic_list)
# [1, 8, 27]

[number ** 3 for number in range(1, 4)]
# [1, 8, 27]
```

```python
# 1~3까지 숫자 중 짝수만 담긴 리스트

even_list = []
for i in range(1, 4):
    if i % 2 == 0 :
        even_list.append(i)
print(even_list)
# 2

[x for x in range(1,4) if x % 2 == 0]
# 2
```

```python
girls = ['jane', 'amy']
boys = ['max', 'jin']

pair = []
for boy in boys:
    for girl in girls:
        pair.append((boy, girl))
print(pair)
# [('max', 'jane'), ('max', 'amy'), ('jin', 'jane'), ('jin', 'amy')]  
 
[(boy, girl) for boy in boys for girl in girls]
    
# [('max', 'jane'), ('max', 'amy'), ('jin', 'jane'), ('jin', 'amy')]        
```

##### 빌트인함수 - map (중요!!)

- map(function, iterable)
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하여 그 결과를 map object로 반환

```python
numbers = [1, 2, 3]
result = map(str, numbers)
print(result, type(result))
# <map object at 0x10e2ca100> <class 'map'>

list(result)
# ['1', '2', '3']
```
