# recursive function 재귀함수

## 팩토리얼



##### for 반복문 사용

```python
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(4))
```



##### while 반복문 사용

```python
def factorial(n):
    result = 1
    while 1 < n:
        result *=n
        n -= 1
    return result

print(factorial(4))
```



##### 팩토리얼 사용

```python
def factorial(n):
    if n == 1:  # n이 1이면 더이상 추가 함수를 호출하지 않는다. (basecase)
        return n 
    else:
        return n * factorial(n-1)

print(factorial(4))
```



## 피보나치 수열



##### for 문 사용

```python
def fib_loop(n):
    if n < 2:
        return n

    result = [0, 1]

    for in range(2, n+1):
        temp = result[i-2] + result[i-1]
        result.append(temp)

    return result[-1]    
```



##### 재귀함수 사용

```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```



