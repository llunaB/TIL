# 스택

## About Stack

물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조

- 스택에 저장된 자료는 선형 구조를 갖는다 (자료간의 관계가 1대 1, 1대 다는 트리)
- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.
- 마지막에 삽입한 자료를 가장 먼저 꺼낸다. 후입선출(LIFO, Last-In-First-Out)

## 구현

### 자료구조 : 자료를 선형으로 저장할 저장소

- C언어에서는 배열을 사용
- 저장소 자체를 스택이라 부르기도 한다.
- 스택에서 마지막 삽입환 원소의 위치를 `top`이라 부른다.

### 연산 : push / pop / isEmpty / peek

- 삽입: 저장소에 자료를 저장한다. `push`
- 삭제: 저장소에서 자료를 꺼낸다. 꺼낸 자료는 삽입한 자료를 역순으로 꺼낸다. `pop`
- 스택이 공백인지 아닌지 확인하는 연산. `isEmpty` (비어있으면 true) 
- 스택의 top에 있는 item(원소)를 확인하는 연산. `peek`

### 과정

- `top(stack pointer)`은 `-1` 부터 시작

```python
# [0, 0, 0, 0, 0]
# [0][1][2][3][4]

stack = [0] * 5			# 크기를 정해놓은 스택

push(n)
	top += 1
  stack[top] = n
  
pop(n)
	t = stack[top]
  top -= 1
  return t

pop(n)
	top -= 1
  return stack[top + 1]

# 비어있는 경우, 모두 차있는 경우 pop이나 push 불가
  
```

```python
# push
s = []
def push(item):
  s.append(item)
  
# pop
s = []
def pop() :
  if len(s) == 0 :		# 비어있는 경우, 검사를 먼저 하고 pop을 시작
    #	underflow - 모자라는데 자꾸 꺼내라해서 발생하는 에러
    return
  else:
    return s.pop(-1) 	# or s.pop()
```



## 연습문제

- 스택 구현하고, 3개의 데이터를 스택에 저장하고 3번 꺼내 출력

```python
# 노가다
s = []
s.append(1)
s.append(2)
s.append(3)
print(s.pop(1))
...
# 다꺼내기
while stack:			# stack 이 남아있는 동안
  print(s.pop())	# 맨 뒤부터 하나씩 꺼낸다
  
-------code-------

top = -1					# top 초기화
s = [0] * 10
def push():
  top += 1
  s[top] = 1
 
def pop():
  pass
  
# 다꺼내기
while top >= 0 :		# stack 이 남아있는 동안
  top -= 1
  print(s[top + 1])
  
while top >= 0 :
  print(s[top])
  top -= 1
```



## 구현 고려사항

- 1차원 배열 사용할 경우, 구현 용이하나 스택의 크기를 변경하기가 어렵다. 크기 정할 수 있으면 1차원 배열!
- 더 늘리려면 느리지만 append 사용, 양이 많으면 top 으로 구현 (??)
- 이를 해결하려면 동적 연결리스트를 이용하여 구현 (생략)



## 응용1. 괄호검사

> 괄호의 종류 : 대괄호 [], 중괄호 {}, 소괄호 ()

- 왼쪽 괄호를 만나면 push, 오른쪽 괄호를 만나면 pop(top 괄호 삭제) 한후, 오른쪽 괄호와 짝이 맞는지 검사(같은 괄호)
- 스택이 비어있으면 조건 1,2 위배, 있는데 짝이 안맞으면 조건3 위배
- 마지막 괄호까지 조사한 후에도 스택에 괄호가 남아있으면 조건1 위배

```python
if (( i == 0 )) && ( j == 0 )

( 열리면 push
) 닫히면 pop

# 1. 괄호 수식이 끝났는데 스택에 괄호가 남아있으면 오류
# 2. ')' 남았는데 stack이 비어있는 경우 오류
# 3. 괄호 종류가 다르면 오류
```



## 응용2. Function call

> 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리

- 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조이므로, 스택을 이용하여 수행순서 관리
- 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임(stack frame)에 저장하여 시스템 스택에 삽입
- 함수의 실행이 끝나면 시스템 스택의 top원소(스택 프레임)을 삭제(pop)하면서 프레임에 저장되어 있던 복귀 주소를 확인하고 복귀
- 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백이 된다.

![image-20210818095938426](/Users/euijinpang/TIL/algorithm/05_Stack.assets/image-20210818095938426.png)



# 재귀호출

> 자기 자신(똑같이 생긴 다른 함수)을 호출하여 순환 수행되는 것

- 일반적인 호출방식보다 프로그램 크기를 줄이고 간단하게 작성
- 단, 너무 짤막한것을 여러번 수행하면 실행시간 오래 걸린다. (최대 1000)

## 예시 : 팩토리얼 (갈림길 없는 재귀함수)

- n 에 대한 팩토리얼 : 1부터 n까지의 모든 자연수를 곱하여 구하는 연산

```python
n! = n x (n-1)!
(n-1)! = (n-1) x (n-2)!
(n-2)! = (n-2) x (n-3)!
...
2! = 2 x 1!
1! = 1
0! = 1

# 마지막에 구한 하위값을 이용하여 상위 값을 구하는 작업을 반복
```

![image-20210818102107920](/Users/euijinpang/TIL/algorithm/05_Stack.assets/image-20210818102107920.png)

```python
f(n)
	if n == 1 :					# 호출을 중단하는 조건
    return 1
  else:
    return n * f(n-1)
```



## 예시 : 재귀호출

```python
def f(i, k):
  if i==k: # 배열을 벗어나면(모든 원소에 대한 작업이 끝나면)
    return
  else:
    print(A[i])
    f(i+1, k) # 다음 원소로 이동

N = 3
A = [10, 20, 30]
r = f(0, N) # 배열을 출력하는 함수 r: None
print(r)

'''
10
20
30
None
'''
```



## 예시 : 피보나치(갈림길이 생기는 재귀함수)

> 0과 1로 시작하고 이전의 두 수의 합을 다음 항으로 하는 수열

- 피보나치 수열의 i 번째 값을 계산하는 함수 F
- 피보나치 수열의 i 번째 항을 반환하는 함수를 재귀함수로 구현

```python
F0 = 0, F1 = 1
Fi = Fi-1 + Fi-2 for i>= 2
```

```python
def fibo(n):
	if n < 2:
		return n
	else:
		return fibo(n-1) + fibo(n-2)
```



![image-20210818104805296](/Users/euijinpang/TIL/algorithm/05_Stack.assets/image-20210818104805296.png)



# Algo : Memoization

- 피보나치 수열을 재귀로 구현하면 엄청난 중복호출이 발생
- 시간복잡도 Θ(2 square n) : 기하급수적으로 실행수 증가 ㅠㅠ

![image-20210818114916097](/Users/euijinpang/TIL/algorithm/05_Stack.assets/image-20210818114916097.png)

- 컴퓨터 프로그램을 실행할 때, 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술.
- 동적 계획법의 핵심



## 적용 알고리즘

- 피보나치에서 fibo(n) 계산하자마자 저장시, 실행시간 Θ(n) 으로 단축

```python
# memo를 위한 배열을 할당하고, 모두 0으로 초기화한다.
# memo[0] 을 0으로, memo[1] 은 1로 초기화한다.

# memo = [0] * (n + 1)
# memo[0] = 0
# memo[1] = 1

def fibo1(n):
  global memo
	if memo[n] == 0:
 	 memo[n] = fibo(n-1) + fibo(n-2)
  return memo[n]

def fibo1(n):
  global memo
  if n >= 2 and len(memo) <= n:
    memo.append(fibo1(n-1) + fibo1(n-2))
  return memo[n]

memo = [0, 1]
```

```python
# 각각 구하려는 피보나치 값이 있으면 n의 최댓값만큼 미리 메모를 만들어놓는다.
# memo2 추천

def fibo2(n):
    global cnt
    cnt += 1
    if n>=2 and memo2[n]==0: # 아직 계산되지 않은 값이면
        memo2[n] = fibo2(n-1) + fibo2(n-2) # 계산해서 저장
    return memo2[n]

def fibo1(n):
    if n>=2 and len(memo1)<=n:
        memo1.append(fibo1(n-1) + fibo1(n-2))
    return memo1[n]

n = 10
memo2 = [0] * (n+1)
memo2[0] = 0
memo2[1] = 1
cnt = 0
print(fibo2(n), cnt)

memo1 = [0, 1]
print(fibo1(n))
```





# DP(Dynamic Programming) 동적 계획법

> 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘
>
> 먼저 입력 크기가 작은 부분 문제들을 해결한 후, 그 해를 이용하여 보다 큰 부분 문제를 해결, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

- memorization을 재귀적 구조에 사용하는 것보다, 반복구조로 DP를 구현하는 것이 성능 면에서 보다 효율적이다.



### 피보나치수 DP 적용

- 피보나치 수는 부분 문제의 답으로부터 본 문제의 답을 얻을 수 있으므로 최적 부분 구조로 이루어져 있다.

```python
def fibo(n):
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
        
    return table[n]

n = int(input())
table = [0] * (n+1)
print(fibo(n))
```

![image-20210818142508876](/Users/euijinpang/TIL/algorithm/05_Stack.assets/image-20210818142508876.png)

### facotrial DP 적용

```python
def fact(n):
    table[0] = 1
    for i in range(1, n+1):
        table[i] = i * table[i-1]

    return table[n]


n = int(input())
table = [0] * (n + 1)
print(fact(n))
```



# DFS, 깊이우선탐색

> 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함

- 깊이 우선 탐색(DFS, Depth First Search)
- 너비 우선 탐색(BFS, Breadth First Search)



- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 <u>더 이상 갈 곳이 없게 되면</u>, 가장 마지막에 만났던 갈림길이 간선이 있는 정점으로 되돌아와서(뒷걸음질, 탐색아님) 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가 가시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용 (반드시 스택이어야하는 것은 아님)



### 알고리즘

1) **시작 정점 v를 결정하여 방문한다.**
2) **정점 v에 인접한 정점 중에서**
   1) 방문하지 않은 정점 `w` 가 있으면, 정점 `v`를 스택에 `push`하고 정점 `w`를 방문한다. 그리고 `w`를 `v`로 하여 다시 2 를 반복한다.
   2) 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 `pop`하여 받은 가장 마지막 방문 정점을 `v`로 하여 다시 2 를 반복한다.
3) **스택이 공백이 될 때까지 2를 반복한다.**



- do-while 구조 : 무조건 한 번은 반복

![image-20210818145152062](/Users/euijinpang/TIL/algorithm/05_Stack.assets/image-20210818145152062.png)

![image-20210818145250528](/Users/euijinpang/TIL/algorithm/05_Stack.assets/image-20210818145250528.png)

- stack은 지나온 경로를 저장하는 용도!!
- 다음번 방문지를 정했다면, 그 위치(방문지 말고)는 push !

- 마지막 정점으로 돌아가기 위해 스택을 pop하는데, 스택이 공백이므로 깊이 우선 탐색을 종료
- 깊이 우선 탐색 경로 : A - B - D - F - E - C - G



#### stack의 용도? 지나오는 경로를 저장하는 용도!

#### 어떤게 인접일까? 인접행렬

![image-20210818154029652](/Users/euijinpang/TIL/algorithm/05_Stack.assets/image-20210818154029652.png)

- 1번부터 시작~

