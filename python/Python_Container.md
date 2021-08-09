# 컨테이너

> 여러 개의 값을 저장할 수 있는 것(객체)

## 시퀀스형(sequence) 

- 순서가 있는(ordered) 데이터 , 인덱스값으로 접근 가능( !=정렬되어있다)

### 리스트(list)

- 순서 있는 스퀀스로 인덱스를 통해 접근(값 접근은 list[i])
- str() 내장함수 사용해서 문자열의 형태로 변환 가능!
- <u>리스트는 수정하거나 삭제할 수 있다!(mutable)</u>

##### 리스트 연산(더해서 연결하기, 곱해서 반복하기, 길이구하기)

##### 리스트 인덱싱

##### 리스트 슬라이싱

##### 내장함수

- 리스트 정렬

  ```python
  a = [1, 3, 2]
  a.sort()
  a
  
  # [1, 2, 3]
  ```

- 리스트 뒤집기

  ```python
  a = [1, 3, 2]
  a.reverse()
  a
  
  # [2, 3, 1]
  ```

  

### 튜플(tuple)

- <u>수정 불가능(immutable)</u> 한 시퀀스로 인덱스로 접근(값 접근은 tuple[i])

- () 혹은 tuple() 을 통해 생성

- 하나의 항목으로 구성된 튜플은 값 뒤에 쉼표 붙여야

  ```python
  b = (1, )
  ```

##### 튜플 연산(더해서 연결하기, 곱해서 반복하기, 길이구하기)

##### 튜플 인덱싱

##### 튜플 슬라이싱



### 레인지(range)

- 숫자의 시퀀스를 나타내기 위해 사용
  - range(n) : 0 부터 n-1까지
  - range(n, m) : n부터 m-1까지
  - range(n, m, s) : n부터 m-1까지 s만큼 증가

### 문자형(string)

### 바이너리(binary)



## 비 시퀀스형(non-sequence)

- 순서가 없는(unordered) 데이터

### 자료형 - 세트(set)

- 순서가 없고, 중복도 허용하지 않는다!!!

```python
s1 = set([1,2,3]) # 리스트 입력 {1, 2, 3}
s2 = set('hello') # 문자열 입력 {'e', 'h', 'l', 'o'}
```

- 순서 없어 인덱싱 지원 x, 인덱싱 접근하려면 리스트나 튜플로 변환

```python
s1 = set([1,2,3])
l1 = list(s1)
t1 = tuple(s1)

s1[0] # error
l1[0] # 1 
t1[0] # 1
```



### 딕셔너리(dictionary)

```python
{key1:value1, key2:value2, key3:value3}
```

- key 에는 변하지 않는 값 사용 : 숫자형, 문자형
- 인덱싱, 슬라이싱 등 적용 불가능! 순서가 없기 떄문에.. 따라서 key값으로만 찾을 수 있다

```python
grade = {'student1':80, 'student2':90}
grade['student1']
```

- 관련함수

  - key, value 쌍 얻기(items) (tuple로 반환)

    ```python
    a = {'name':'euijin','phone':'010-1234-5678'}
    
    a.items()
    dict_items([('name','euijin'),('phone','010-1234-5678')])
    ```

  - key로 value 얻기(get)

    ```python
    a = {'name':'euijin','phone':'010-1234-5678'}
    
    a.get('name')
    a.get('phone')
    ```

    
