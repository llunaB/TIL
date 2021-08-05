# Exception Handling

> 예외처리



## Error

- SyntaxError
- ZeroDivisionError
- NameError
- TypeError
- ValueError
- IndexError
- KeyError
- ModuleNotFoundError
- ImportError
- KeyboardInterrupt



## try & except

```python
try:
  	print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
  	print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
  	print(err)
except:
  	print("알 수 없는 에러가 발생하였습니다.")
    
# 나누기 전용 계산기입니다.    
# 첫 번째 숫자를 입력하세요 : 6
# 두 번째 숫자를 입력하세요 : dd
# 에러! 잘못된 값을 입력하였습니다.

# 나누기 전용 계산기입니다.    
# 첫 번째 숫자를 입력하세요 : 6
# 두 번째 숫자를 입력하세요 : 0 
# division by zero
```



## raise - 에러 발생시키기

- 조건문을 활용하여 의도적으로 에러를 발생시킨다.

```python
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >=10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
    
# 한 자리 숫자 나누기 전용 계산기입니다.
# 첫 번째 숫자를 입력하세요 : 10 5
# 잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.
```



## 사용자 정의 예외처리

- 사용자가 정의하는 에러에 대해 특정 메세지를 찍어낼 지 정의할 수 있다.

```python
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >=10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
    
# 한 자리 숫자 나누기 전용 계산기입니다.
# 첫 번째 숫자를 입력하세요 : 10
# 두 번째 숫자를 입력하세요 : 5
# 에러가 발생하였습니다. 한 자리 숫자만 입력하세요.
# 입력값 : 10, 5
```



## finally

- try 문 내부 명령의 에러와 관계없이 무조건 실행되는 구문

```python
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >=10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")
```

