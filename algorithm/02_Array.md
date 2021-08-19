# Array 배열

## About Array

### 배열이란?

일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조

### 배열의 필요성?

- 프로그램 내에서 여러 개의 변수가 필요할 때, 일일이 다른 변수명 입력하여 자료에 접근하는 것은 비효율적
- 배열 사용시 하나의 선언을 통해 둘 이상의 변수 선언이 가능하다.
- 다수의 변수로는 하기 힘든 작업을 배열을 활용해 쉽게 할 수 있다. 



## 1차원 배열

### 선언

```python
Arr = list()
Arr = []
```

### 접근

```python
Arr[0] = 10
Arr[idx] = 20   # 배열 Arr의 idx번째 원소에 20을 저장하라
```

### 문제적용

```python
# input : 1 2 3 4 5

A = list(int, input().split())
# ['1', '2', '3', '4', '5']

A = list(map(int, input().split()))
# [1, 2, 3, 4, 5]
```

### 1차원 배열 예제 : Gravity

![image-20210817223000537](/Users/euijinpang/TIL/algorithm/02. Array.assets/image-20210817223000537.png)

![image-20210817223019698](/Users/euijinpang/TIL/algorithm/02. Array.assets/image-20210817223019698.png)

![image-20210817223028320](/Users/euijinpang/TIL/algorithm/02. Array.assets/image-20210817223028320.png)



## 기타 팁

array 는 범위가 지정되어있고, 파이썬의 list는 범위가 변할 수 있다. 

비슷해보이지만 본질적으로 다르다!

각각의 요소요소가 중요! 인덱스 개념이 아님



## 2차원 배열

### 선언

- 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함

```python
arr = [[0,1,2,3][4,5,6,7]] # 2행 4열의 2차원 리스트
```

```python
# N행 M열

# for문으로 구현 [[1, 2, 3], [4, 5, 6]]
arr = []
N, M = map(int, input().split())  # 2 3
for _ in range(N):
  arr.append(list(map(int, input().split())))
  
# 한 줄로 구현 [[1, 2, 3], [4, 5, 6]]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

# [[0, 0, 0], [0, 0, 0]]
arr2 = [[0] * M for _ in range(N)]
print(arr2)
```



### 접근 - 배열순회

- n * m 개의 모든 원소를 빠짐없이 조사

```python
# 상하좌우 (내가 정함)
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
```



![image-20210818214513770](/Users/euijinpang/TIL/algorithm/02_Array.assets/image-20210818214513770.png)



### 접근 - 행우선순회

![image-20210819000923457](/Users/euijinpang/TIL/algorithm/02_Array.assets/image-20210819000923457.png)

### 접근 - 열우선순회

![image-20210819000934869](/Users/euijinpang/TIL/algorithm/02_Array.assets/image-20210819000934869.png)

##### 연습문제

![image-20210819000826428](/Users/euijinpang/TIL/algorithm/02_Array.assets/image-20210819000826428.png)





## 부분집합 생성

#### 부분집합 합(Subset Sum) 문제

![image-20210819001204336](/Users/euijinpang/TIL/algorithm/02_Array.assets/image-20210819001204336.png)



![image-20210819001248669](/Users/euijinpang/TIL/algorithm/02_Array.assets/image-20210819001248669.png)



![image-20210819004300539](/Users/euijinpang/TIL/algorithm/02_Array.assets/image-20210819004300539.png)



## 검색(Search)

- 목적하는 탐색 키를 가진 항목을 찾는 것
  - search key : 자료를 구별하여 인식할 수 있는 키
- 종류
  - 순차 검색 (sequential search)
  - 이진 검색 (binary search)
  - 해쉬 (hash)



### 순차 검색

- 일렬로 되어 있는 자료를 순서대로 검색
- 배열, 연결리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용
- 검색 대상의 수가 많은경우 수행시간이 급격히 증가

##### 정렬된 경우

![image-20210819004534522](/Users/euijinpang/TIL/algorithm/02_Array.assets/image-20210819004534522.png)

##### 정렬되어 있지 않은 경우

![image-20210819004511531](/Users/euijinpang/TIL/algorithm/02_Array.assets/image-20210819004511531.png)



### 바이너리 서치(Binary Search), 이진검색

![image-20210819004443289](/Users/euijinpang/TIL/algorithm/02_Array.assets/image-20210819004443289.png)











## 셀렉션 알고리즘(Selection Algorithm)

## 선택 정렬(Selection Sort)

