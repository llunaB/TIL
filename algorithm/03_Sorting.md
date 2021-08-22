# Sorting 정렬

## About Sorting

#### 정렬이란?

2개 이상의 자료를 특정 기준에 의해 작은 값부터 큰값(오름차순, ascending), 혹은 그 반대의 순서대로(내림차순, descending) 재배열하는 것

#### 키 란?

자료를 정렬하는 기준이 되는 특정 값!



###### Sorting - Bubble, Counting, Selection, Quick, Insertion, Merge



## 버블정렬 (Bubble Sort)

- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

- ##### 시간 복잡도 : O(n**²**)

##### 정렬 과정

- 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하며 맨 마지막 자리까지 이동한다.
- 한 단계가 끝나면 큰 원소가 마지막 자리로 정렬된다.
- 구간의 끝: i
- 인접 원소의 왼쪽 : j, 그 오른쪽 요소 : j + 1

```python
# N개짜리 리스트일때
#  0  1  2  3  4
# [6, 4, 2, 3, 5]

for i in range(n-1, 1, -1): # for i : n-1->1 
  for j in range(0, i-1):	# 구간의 끝이 i 라면 j는 i-1까지만, 그래야 j+1이 마지막
    											# for j : 0 -> i-1
    if A[j] > A[j+1]: 
      A[j], A[j+1] = A[j+1], A[j]
```

```python
def BubbleSort(a) :
  for i in range(len(a)-1, 0, -1) :
    for j in range(0, i):
      if a[j] > a[j+1] :
        a[j], a[j+1] = a[j+1], a[j]
```

##### 최댓값찾기

```python
# N개짜리 리스트일때
#  0  1  2  3  4
# [6, 4, 2, 3, 5]

# 최댓값: 찾는범위 i 0->4 (n-1)
maxV
maxIdx

N = 5
for i : 0 -> N-1
  if A[i] > maxV:
```



## 카운팅 정렬 (Counting Sort)

- 항목들의 순서를 결정하기 위해 집합에 각 항복이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
- 제한사항: 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능. 각 항목의 발생 회수를 기록하기 위해 정수 항목으로 인덱스되는 카운트들의 배열을 사용하기 때문이다.
- 카운트를 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.
- 시간 복잡도 : **O(n + k)**



##### 정렬 과정

1. 데이터 각 항목의 발생회수를 세고, 정수 항목들로 직접 인덱스되는 카운트배열에 저장한다. (counts 배열)

   ```python
   count[0]=0의 발생 회수 ... count[i]=i 의 발생 회수
   ```

   ```python
   COUNTS = [0] * n #이때 n 은 data의 개수가 아닌 data 원소의 범위
   ```

```python
def Counting_Sort(A, B, k):
# Data [] -- 입력 배열(0 to k)
# Temp [] -- 정렬된 배열
# Counts [] -- 카운트 배열

	Counts = [0] * (k + 1) # [0,0,0,0,..]
  
  for i in range(0, len(Temp)): # 0 -> N-1  
    Counts[Data[i]] += 1 # 값을 인덱스로 받는 배열 (N개만큼)
    
  for i in range(1, len(Counts)):
    Counts[i] += Counts[i-1] # k 번 누적합으로 만든 배열
    
  for i in range(len(Temp)-1, -1, -1) : # N개만큼
    Counts[Data[i]] -= 1
    Temp[Counts[Data[i]]] = Data[i]
```



## 선택정렬 (Selection Sort) 

![image-20210821234010901](/Users/euijinpang/TIL/algorithm/03_Sorting.assets/image-20210821234010901.png)

```python
def selection_sort(arr):
  """
  선택 정렬을 통해 배열 arr을 오름차순 정렬한다.
  
  arr: 정렬하고자 하는 배열
  N: 배열의 길이
  min_idx: 매 정렬시 최소값의 인덱스
  """
  N = len(arr)
  for i in range(N-1):
    min_idx = i
    for j in range(i+1, N):
      if arr[j] < arr[min_idx]:
        min_idx = j
    
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

