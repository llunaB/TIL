# 데이터와 제어문

### 논리연산자 - 단축평가

첫 번째 값의 결과가 확실한 경우 두번째 값은 확인하지 않는다.

```python
a = 5 and 4	# 4 - and 연산에서는 모두 True 여야 True
b = 5 or 3	# 5 - or 연산에서는 모두 False여야 False
c = 0 and 5	# 0 
d = 5 or 0	# 0
```





### 실수 비교하기

파이썬은 부동소수점 방식을 이용하여 실수(float)을 표현하는 과정에서, 나타내고자 하는 값과의 오차가 발생하여 원하는 연산이 되지 않을 때가 있다. 두 실수 값을 올바르게 비교하는 방법은?

- 임의의 가장 작은 수보다 절대값의 차가 작거나 같으면 동일하다

```python
num1 = 0.1 * 3
num2 = 0.3

print(num1 == num2) # False, 오차로 인한 연산 오류
print(abs(num1 - num2) <= 1e-10) # True 임의의 가장 작은 수로 비교
```



### 홀수만 출력하기

1부터 50까지 자연수 중 홀수만 출력

```python
numbers = range(1, 51)
numbers_list = list(numbers)	# range 를 슬라이스 위해 리스트로

print(numbers_list[::2])	# 리스트를 2 간격으로 슬라이스
```



### 이스케이프 시퀀스

줄바꿈, 탭, 백슬래시 이스케이프 시퀀스

```python
print("Hi, my name is jessie.")

print("Hi, my name is \n jessie") # 줄바꿈
print("Hi, my name is \t jessie") # 탭
print("Hi, my name is \\ jessie") # 백슬래시
```



### 네모 출력하기

두 개의 정수 n과 m이 주어질 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 별 문자를 이용하여 출력한다.

- 반복문 미사용의 경우 => 이스케이프 시퀀스 활용
- 반복문 사용의 경우 => while 문 사용

```python
n = 5
m = 9
# escape sequence 사용
hor = '*' * n + '\n'  	# "*" 문자열을 n 번 반복하고 줄바꿈 추가
print(hor * m)     		# m 번 반복

# while문 사용
hor = '*' * n + '\n'  	# "*" 문자열을 n 번 반복하고 줄바꿈 추가

ver = 0             	# 변수 초기화
while ver < m:          # 세로가 m 값이 될 때까지 출력
    print(hor, end="")
    ver = ver + 1
    
# for문 사용
for m in range(1, m + 1):	# 프린트문이 m의 값만큼 반복
    print('*' * n)	
    
# for문 사용 2
for i in range(m):	# 가로로 붙인 별을 m번 만큼 출력
    for j in range(n):	# '*'을 n개만큼 출력하고 가로로 붙임
        print('*', end = '')
    print('') 
```



### 근의 공식 구하기

```python
a = 1
b = 2
c = -8

r1 = (-b + (b ** 2 - 4 * a * c ) ** 0.5) / (2 * a) 
r2 = (-b - (b ** 2 - 4 * a * c ) ** 0.5) / (2 * a) 
print('해는 : ', r1, '또는 ', r2)
```



### 세로로 출력하기

자연수 number를 입력받아, 1부터 number까지의 수를 세로로 한 줄씩 출력

```python
user_input = int(input())

for i in range(1, user_input + 1):
    print(i)	# print 함수는 줄바꿈이 내재되어 있다
```



### 거꾸로 세로로 출력하기

자연수 number를 입력받아, number부터 0까지의 수를 세로로 한 줄씩 출력

- 방법 1. range 함수 
- 방법 2. for문과 빈 문자열
- 방법 3. reverse 함수, .join
- 방법 4. reversed 함수
- 방법 5. 문자열 인덱스 거꾸로 호출 [::-1]

```python
# 1. range 함수를 이용
user_input = int(input())	# 5
for i in range(user_input, -1, -1): # range(start, stop[, step]) start에서 시작하고 stop은 미포함, 스텝 -1은 역순
    
    print(i)	# 5 \t 4 \t 3 \t 2 \t 1 \t 0

# 2. for 문과 빈 문자열
user_input = input()
num_reverse = ''    # 빈 문자열 선언
for n in range(0, int(user_input) + 1): # 숫자를 차례대로 가져와 앞뒤 순서를 바꿈
    num_reverse = str(n) + '\n' + num_reverse   # 세로쓰기
    
print(num_reverse)

# 3. reverse 함수와 join
s = 'abcde'
# reverse 함수를 사용하기 위해 문자열을 list로 치환
s_list = list(s)	# ['a', 'b', 'c', 'd', 'e']
# reverse 함수를 사용해 문자열 리스트를 거꾸로 뒤집음
s_list.reverse()	# ['e', 'd', 'c', 'b', 'a']

print(''.join(s_list))	# edcba



# 4. reversed 함수와 join
# reverse는 리스트에만 사용가능하지만 reversed는 문자열에도 적용가능
s = 'abcde'

print(''.join(reversed(s)))	# edcba



# 5. 문자열 인덱스 거꾸로 호출
s = 'abcde'

print(s[::-1])	# edcba
print(s[3:1:-1])# dc
print(s[3::-1])	# dcba

```



### N줄 덧셈

입력으로 자연수 number, 1부터 입력값까지를 모두 더한 값을 출력

- for문 이용

```python
user_input = int(input)

num = 0	# 변수 초기화
for i in range(1, user_input + 1):	# 1부터 입력값까지의 범위
    num = num + i	# 총합 구하기
print(num)
```

