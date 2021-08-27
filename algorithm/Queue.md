# Queue

선입선출구조 (FIFO: First In First Out)

- 선형 큐
- 원형 큐



## 선형 큐 => 일단 이것만 알면 됨!

#### 큐의 주요 연산 (정적 배열 != 리스트)

배열의 길이가 고정되어 있다는 전제조건 하 (동적 타이핑언어인 파이썬과 다름)에

맨 앞에 무엇이 들어있는지 확인할 수 없다. 인덱스를 활용해야한다.

---

![image-20210825171246412](/Users/euijinpang/TIL/Queue.assets/image-20210825171246412.png)

---

![image-20210825171224658](/Users/euijinpang/TIL/Queue.assets/image-20210825171224658.png)



![image-20210825171323169](/Users/euijinpang/TIL/Queue.assets/image-20210825171323169.png)



![image-20210825171339344](/Users/euijinpang/TIL/Queue.assets/image-20210825171339344.png)

![image-20210825171351902](/Users/euijinpang/TIL/Queue.assets/image-20210825171351902.png)



## 큐 구현

![image-20210825171432259](/Users/euijinpang/TIL/Queue.assets/image-20210825171432259.png)

![image-20210825171443320](/Users/euijinpang/TIL/Queue.assets/image-20210825171443320.png)



![image-20210825171457106](/Users/euijinpang/TIL/Queue.assets/image-20210825171457106.png)

![image-20210825171507461](/Users/euijinpang/TIL/Queue.assets/image-20210825171507461.png)

![image-20210825171515377](/Users/euijinpang/TIL/Queue.assets/image-20210825171515377.png)

## 구현(리스트)

- 크기가 정해진 1차원 리스트로 구현

![image-20210825171530003](/Users/euijinpang/TIL/Queue.assets/image-20210825171530003.png)

```python  
Q = [0] * 10 #10칸짜리 큐

front = -1
rear = -1

# enQueue(1)
rear += 1
Q[rear] = 1
# enQueue(2)
rear += 1
Q[rear] = 2
# enQueue(3)
rear += 1
Q[rear] = 3

# print(deQueue())
while front != rear:
  front += 1
  print(Q[front], end = '') 
print()

#########################################################
listQ = []
listQ.append(1)
listQ.append(2)
listQ.append(3)

while listQ:
  print(listQ.pop(0), end=' ')
print()

##########################################################

# from collections import deque
# enqueue -> append 오른쪽에 붙이기
q = deque()
q.append(1)
q.append(2)
q.append(3)
# dequeue -> popleft 왼쪽에서 꺼내기
while q:
  print(q.popleft())

```



## 원형 큐

#### 초기 공백 상태

- front = rear = 0



![image-20210825095151000](/Users/euijinpang/TIL/Que.assets/image-20210825095151000.png)

```python
Q = [0] * 10 #10칸짜리 큐

front = 0
rear = 0

...
```





## 연결 큐

- linked list 로 구현

![image-20210825101609108](/Users/euijinpang/TIL/Que.assets/image-20210825101609108.png)

## 우선순위 큐

- 나갈 때, 들어온 순서가 아닌 우선 순위가 높은 순서대로 먼저 나간다.

##### 배열을 이용하여 구현

- 원소 삽입시 우선순위를 비교 (정렬하며) , 가장 앞에 최고 우선순위 위치

##### 링크드리스트 이용하여 구현



## 큐의 활용 : 버퍼

#### 버퍼

- 데이터를 한 곳에서 다른 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리 영역
- 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작
- 입출력, 네트워크 관련 기능
