# 변수, 식별자, 연산자

## 변수

> 변수는 할당 연산자를 통해 값을 할당

##### type() 

- 변수에 할당된 값의 타입 확인

##### id()

- 변수에 할당된 값(객체)의 고유 identity 값

##### 할당 연산자(=)

- 같은 값 동시할당 가능

  ```python
  x = y = 1004
  print(x, y)
  
  # 1004 1004
  ```

- 다른 값 동시할당 가능 (multiple assignment)

  ```python
  x, y = 1, 2
  pritn (x, y)
  
  # 1 2
  ```

- 값 swap

  - x = 10, y = 20 일 때, 각각 값을 바꿔서 저장하는 코드를 작성하시오.

    ```python
    x, y = 10, 20
    
    # 1. 임시변수 활용
    tmp = x
    x = y
    y = tmp
    print(x ,y)
    
    # 2. 파이써닉
    y, x = x, y
    print(x, y)
    
    # 20 10
    ```

    

## 식별자(Identifiers)

- 변수(박스)의 이름짓기

- 예약어(reserved words)로 사용할 수 없는 키워드(keywords)

  ```python
  # 키워드/예약어 찾기
  import keyword
  print(keyword.kwlist)
  
  # [False, None, True, and, as, for, not, or, pass, if, class, continue,...]
  ```

  

## 연산자(Operator)

##### 산술 연산자

- divmond(a, b) : 각각 몫과 나머지를 반환

<img src="Python_Variable,Identifier, Operator.assets/image-20210721082345372.png">

##### 비교 연산자

- True / False 값을 리턴

<img src="Python_Variable,Identifier, Operator.assets/image-20210801235931210-7829972.png">



##### 논리 연산자

<img src="Python_Variable,Identifier, Operator.assets/image-20210721082655223-7827442.png">



- 단축평가!!

  - 결과가 확실한 경우 두번째 값은 확인하지 않고 첫번째 값을 반환한다.

  ```python
  a = 5 and 4
  print(a)
  # 4 : and 연산에서 첫번째 값이 True 이면 다음도 확인해야 하므로 두번째 값으로 넘어간다.
  
  b = 5 or 3
  print(b)
  # 5 : or 연산에서 첫번째 값이 True 이면 무조건 True 이므로 첫번째 값을 반환한다.
  
  c = 0 and 5
  print(c)
  # 0 : and 연산에서 첫번째 값이 False 이면 무조건 False 이므로 첫번째 값을 반환한다.
  
  d = 5 or 0
  print(d)
  # 5 : or 연산에서 첫번째 값이 True 이면 무조건 True 이므로 첫번째 값을 반환한다.
  ```

  

##### 복합 연산자



<img src="Python_Variable,Identifier, Operator.assets/image-20210721083433403.png">



##### 기타 연산자

- concatenation
- containment test
- identity
- indexing
- slicing
