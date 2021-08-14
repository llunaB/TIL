### join

> '구분자'. join(리스트) 를 이용하면 매개변수로 들어온 '문자열(str)' 리스트를 문자열로 합쳐 반환합니다.
>

```python
dummy = ['a', 'b', 'c']

# join 함수 사용
"".join(dummy)

# join 함수 미사용
result = ''
for i in dummy:
  result += i

# => abc
```

- dictionary: When using a dictionary as an iterable, the returned values are the keys, not the values.

```python
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

# => nameTESTcountry
```



### upper & lower

> 문자열 내부의 알파벳을 대문자 & 소문자로 변경합니다.

```python
s1 = 'happy'
s2 = s1.upper()

print(s2)
# => 'HAPPY'

s3 = 'HAPPY'
s4 = s3.lower()

print(s4)
# => "happy"
```



### isupper & islower

> string 객체 내부의 모든 문자가 대문자 & 소문자인지 검사 후 Bool type 반환

```python
s1 = 'happy'
s2 = s1.upper()

print(s1.isupper(), s2.isupper())
# => False, True

s3 = 'HAPPY'
s4 = s3.lower()

print(s3.islower(), s4.islower())
# => False, True
```



### 리스트 관련함수 pop()

> 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다.
>
> pop(x) 는 리스트의 x 번째 요소를 돌려주고 그 요소를 삭제한다.

```python
a = [1,2,3]
a.pop()  # 3
a # [1,2]

a = [1,2,3]
a.pop(1) # 2
a # [1,3]
```

