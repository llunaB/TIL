# 제어문(Control Statement)

## 조건문(Conditional Statement)

- if 문은 참/거짓을 판단할 수 있는 조건식과 사용
- 조건(expression) 이 참이면 이후 들여쓰기 된 코드블록 실행
- 그 외의 경우 else 이후 들여쓰기 된 코드블록 실행



```python
if <expression>:
	#
elif <expression>:
  #
elif <expression>:
  #
else:
	#
```



##### 조건문과 조건부 표현식

```python
# 만약 점수가 60점을 이상이면 succeess, 미만이면 failure
score = int(input())

if score >= 60:
  print('success')
else:
  print('failure')
  
print('success') if score >= 60 else print ('failure')
```



##### 대표문항 : 변수 num 값의 홀짝 여부 출력

```python
num = int(input())

if num % 2 == 1:
  print('odd')
else:
  print('even')
  
 print('odd') if num % 2 == 1 else print('even')
```



## 반복문

### while 문

- expression이 True 일때, 문장을 반복해서 수행, False이면 종료

```python
while <expression>:
	#
```



##### 예시문항 : 나무를 10번 찍고 10회째 넘어감

```python
hit = 0
while hit < 10:
  print(f'{hit+1}번째 찍었다')
  hit = hit + 1  # hit += 1
print('넘어갔다')
```

##### break로 빠져나가기

```python
# 자판기 커피는 300원이고, 10잔 있다. 돈을 넣으면 "커피여기" 를 출력하고 커피 수 줄어들고 남은 커피의 양 출력. 커피가 다 떨어지면 '커피가 다 떨어졌음' 출력하고 자판기 정지.

coffee_price = 300
coffee_left = 10

while coffee_price:
  print('커피여기')
  coffee_left -= 1
  print(f'커피 {coffee_left} 잔 남았습니다')
  if coffee_left == 0:
    print('커피가 다 떨어졌음')
    break


# 자판기 커피는 300원이고, 10잔 있다. 돈을 넣어달라는 문구에 돈 입력하고 300원이면 '커피요' 출력하고 커피양 줄어든다. 300원보다 크면 '거스름돈 -원을 줍니다' 출력하고 커피양 줄어든다. 300원보다 적으면 '돈을 돌려주고 커피 안줌' 출력하고 '남은 커피양은 -개입니다.' 출력한다. 커피가 다 떨어지면 '커피가 다 떨어졌음' 출력하고 자판기 정지.
coffee_left = 10
while True:
  money = int(input('돈을 넣어라:'))
  if money == 300:
    print('커피요')
    coffee_left -= 1
  elif money > 300:
    change = money - 300
    print(f'거스름돈 {change}원을 줍니다')
    coffee_left -= 1
  else:
    print('돈을 돌려주고 커피안줌')
  if coffee_left == 0:
    print('커피뚝떨')
    break
```



### for 문

- 리스트나 튜플, 문자열의 첫번째 요소부터 마지막 요소까지 차례로 변수에 대입

```python
for 변수 in 리스트/튜플/문자열:
	#
  

test = ['1','2','3']
for i in test:
  print(i)
# '1' 이 변수에 대입되고 출력, '2'가 변수에 대입되고 출력, ... 
  
# 총 5명의 학생이 시험을 보았는데, 60점 넘으면 합격이고 아니면 불합격이다. 결과출력해보세요.
# 리스트로 표현. 1번 학생은 90점이고 5번 학생은 80점이다.

# 시험점수 리스트
marks = [90, 25, 67, 45, 80]
# 학생들에게 번호를 붙여준다.
num = 0
# 리스트 순서대로 mark에 대입한다.
for mark in marks:
# n을 1씩 증가시킨다.
for mark in marks:
  num += 1
  if mark >= 60:
    print(f'{num}번 학생은 pass')
  else: 
  	print(f'{num}번 학생은 fail')

# 종합
marks = [90, 25, 67, 45, 80]
num = 0
for mark in marks:
  num += 1
  if mark >= 60:
    print(f'{num}번 학생은 pass')
  else: 
  	print(f'{num}번 학생은 fail')
```



##### for문과 continue 문

```python
# for문 수행 중 continue를 만나면 for문의 처음으로 돌아간다

# 60점 이상인 사람에게는 축하메세지 보내기
# 점수 리스트
marks = [90, 25, 67, 45, 80]
# 사람들에게 번호 붙이기
num = 0
# if 문 써서 60점 미만이면 continue 를 통해 다시 처음으로 돌리기, 60점 이상이면 continue를 지나 프린트
for mark in marks:
  if mark < 60:
    num += 1
    continue
  else:
    print(f'{num+1} 번 학생 축하합니다')
    num += 1
    
    
for mark in marks:
  num = num + 1
  if mark < 60: continue
  print(f'{num}번 학생 축하합니다')
```



##### for문과 range 함수

```python
# range(10) 은 0 이상 10 미만의 숫자를 포함하는 range 객체를 생선한다.

# 1부터 10까지의 총합 구하기
n = 0
for i in range(1, 11):
  n = n + i
print(n)

# 60점 이상인 사람에게는 축하메세지 보내기
# 점수 리스트
marks = [90, 25, 67, 45, 80]
num = 0 # 학생 번호

for num in range(0, 5):
  mark = marks[num] # 해당 점수
  if mark >= 60:
    num += 1
    print(f'{num}번 학생 축하합니다')
  else:
    num +=1
    
    
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)): # 0 부터 전체 점수 수-1까지의 범위
  if marks[number] < 60: continue # 점수가 60점 미만이면 맨 처음으로 돌아간다
  print(f'{number+1}번 학생 축하합니다')
  
  
# 1부터 100까지의 합?
num = 0
for i in range(1,101):
  num = num + i
print(num)
  
```

