# 데이터 구조

## 문자열 string

##### .split([char]) : 문자열을 특정 단위로 나눠 리스트로 반환 (중요!!)

- Return a list of the words in the string, using 'sep' as the delimiter string.
- If 'sep' is given, consecutive delimiters are not grouped together and delimit empty strings.
- If 'sep' is not specified or is `None` , runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings.

```python
# 1 2 3 4 5 로 입력된 문자열 인풋을 정수로 바꾸는 법

# split method
# 원본데이터는 바뀌지 않는다. 활용하려면? => 변수에 넣어야!
i = input()
numbers_str = i.split(' ')

result = []
for number_str in numbers_str:
    result += [int(number_str)] # result.append(int(number_str))
print(result)

# => # [1, 2, 3, 4, 5]


# map function
result = map(int, input().split(' '))
print(list(result))
# => [1, 2, 3, 4, 5]
```



##### map(function, iterable, ...)

- Built-in Function
- Return an iterator that applies ***function*** to ***every item of iterable***, yielding the results. 
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하여 그 결과를 map object로 반환

```python
# 'str' to 'int'
result = map(int, input().split(' '))
print(list(result))
# => [1, 2, 3, 4, 5]

# 'int' to 'str' 
numbers = [1, 2, 3, 4, 5]
result = map(str, numbers)
print(result, type(result))
# <map object at 0x10e2ca100> <class 'map'>

# need list!! to be shown :) 
list(result)
# => ['1', '2', '3', '4', '5']
```





## 리스트 list

##### .append(x) : 리스트에 단일 값을 추가

```python
cafe = ['starbucks', 'holly']
cafe.append('presso')

# ['starbucks', 'holly', 'presso']
```

##### .pop(i) : 정해진 위치 i 값을 삭제하고, 그 항목을 반환, i 미지정시 마지막 값을 삭제하고 반환

- Remove and return an arbitrary element from the set.
- Raises 'Keyerror' if the set is empty.

```python
numbers = [1, 2, 3, 4, 5, 6]
result = numbers.pop()
print(result)
print(numbers)

# 6
# [1, 2, 3, 4, 5]
```

