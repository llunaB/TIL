# 데이터 타입

## 숫자(Number)

##### int (정수, integer)

- 파이썬에서는 오버플로(overflow) 가 나타나지 않는다. 알아서 메모리를 늘려주기 때문이다.

##### float (부동소수점, 실수, floating point number)

- floating point rounding error 부동소수점 실수연산과정에서 문제발생 가능

- 3.14 - 3.92 != 0.12

- 해결방법

  - 임의의 작은수보다 작은가?

    ```python
    abs(a-b) <= 1e-10
    
    # True
    ```

  - sysyem 상의 machine epsilon 보다 작은가?

    ```python
    import sys
    print(abs(a-b) <= sys.float_info.epsilon)
    print(sys.float_info.epsilon)
    
    # True
    # 2.22044...3e-16
    ```

  - python 3.5이상 math 모듈 활용

    ```python
    import math
    math.isclose(a,b)
    
    # True
    ```

    

##### complex (복소수, complex number)

- 허수부를 j 로 표현

  

## 문자열(String)

- 소스 내 하나의 문장부호를 선택하여 유지해야 한다
- <u>문자열은 값 수정불가!!!! (immutable)</u>

### 문자열 연산(더해서 연결하기, 곱해서 반복하기, 길이구하기)

### 문자열 인덱싱(indexing)

### 문자열 슬라이싱(slicing)

### 문자열 포매팅(formatting)

- str.format()

  ```python
  name = 'euijin'
  score = 4.5
  
  print('Hello, {}! 당신의 성적은 {}'.format(name, score))
  
  # Hello, euijin! 당신의 성적은 4.5
  ```

- f-strings 

  ```python
  name = 'euijin'
  score = 4.5
  
  print(f'Hello, {name}! 당신의 성적은 {score}')
  
  # Hello, euijin! 당신의 성적은 4.5
  ```

### 이스케이프 시퀀스(escape sequence)

```python
'\n' # 줄바꿈
'\t' # 탭
'\\' # \
```





## 참/거짓(Boolean)

- 다음은 모두 False 

  ```python
  0, 0.0, (), [], {}, '', None
  ```

- bool 내장함수로 확인가능

  ```python
  bool('') # False
  ```

  

## None

- Nonetype이 존재



# 타입 변환

## 암시적 타입 변환

- bool : True 는 1로 변환
- Numbers (int, float complex) : 실수 + 복소수 = 복소수



## 명시적 타입 변환

- int : 문자열(str*)과 실수(float) 은 int 로 바꿀 수 있다.

  ```python
  # 문자열은 암시적 타입 변환이 되지 않음
  '3' + 4
  
  int('3') + 4
  # 7 
  
  int('3.5') + 4
  # error
  ```

  

- float : 문자열(str*)과 int 는 float 로 바꿀 수 있다.

  ```python
  '3.5' + 3.5
  # error
  
  float('3')
  # 3.0
  ```

  

