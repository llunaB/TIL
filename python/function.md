# Function_input,return,scope

## 함수의 output - return

##### 복수의 객체를 return => 하나의 객체(tuple)을 반환

```python
def foo(a,b):
    return a+b, a-b

print(foo(1,2))

#=> (3, -1) : tuple
```



##### 명시적 return값이 없는 경우 => 하나의 객체(None) 반환

```python
def greeting():
    print('hi')

print(greeting())

#=> None : Nonetype
```



## 함수의 input

##### 주의사항

- 기본인자 뒤 위치인자 불가능
- 키워드 인자 뒤 위치인자 불가능



##### 위치 인자 (Positional Arguments) 

- 기본적으로 함수 호출시 인자는 위치에 따라 함수 내에 전달된다.

```python
def add(x, y):
  return x + y

add(2, 3)

def add(x, y):
  x = 2; y = 3
  return x + y
```



##### 기본 인자값 (Default Arguments Values)

- 기본값을 지정하여 함수 호출시 인자값을 설정하지 않도록 한다.

```python
def profile(name, age, main_lang):
	print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}")\
  		.format(name, age, main_lang)

# 같은 학교 같은 학년 같은 반 수업이라면
def profile(name, age=17, main_lang="Python"):
	print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
  		.format(name, age, main_lang))
    
profile("유재석")
profile("김태호")

# 이름 : 유재석   나이 : 17       주 사용 언어 : Python
# 이름 : 김태호   나이 : 17       주 사용 언어 : Python
  
```



##### 키워드 인자 (Keyword Arguments)

- 직접 변수의 이름으로 특정 인자를 전달 할 수 있다.
- 키워드 다음에 위치 인자를 활용할 수는 없다.

```python
def profile(name, age, main_lang):
  print(name, age, main_lang)
  
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="Java", name="김태호", age=20)

# 유재석 20 파이썬
# 김태호 20 Java
```



#####  가변 인자 리스트 (Arbitrary Argument Lists)

- 함수가 임의의 개수 인자로 호출될 수 있도록 지정한다.
- 인자들은 **튜플**로 묶여 처리되며, 매개변수에 *을 붙여 표현한다.

```python
def profile(name, age, *langs):
  print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
  for lang in langs:
    print(lang, end=" ")
  print()

profile ("유재석", 20, "Python", "Java", "C")
profile ("김태호", 25, "Kotlin", "Swift")

# 이름 : 유재석   나이 : 20        Python Java C 
# 이름 : 김태호   나이 : 25        Kotlin Swift 
```



##### 가변 키워드 인자 (Arbitrary Keyword Arguments)

- 함수가 임의의 개수 인자를 키워드 인자로 호출될 수 있도록 지정한다.
- 인자들은 **딕셔너리**로 묶여 처리되며, 매개변수에 **을 붙여 표현한다.

```python
def family(**kwargs):
  for key, value in kwargs:
    print(key, ":", value)
    
family(father='John', mother='Jame', me='Joy')
```



## 함수 Scope

### 이름 검색 규칙(Name Resolution) -  LEGB Rule

- Local scope : **지역 변수** -  해당 함수
- Enclosed scope : 특정 함수의 상위 함수
- Global scope : **전역 변수** - 함수 밖의 변수, Import 모듈
- Built-in scope : 파이썬 내장함수

```python
a = 0
b = 1
def enclosed():
  	# global a => 전역 공간에 있는 a 사용
    a = 10
    c = 3
    def local(c):
        print(a, b, c)
    local(300)
    print(a, b, c)
enclosed()
print(a, b)

#=> 10 1 300
#=> 10 1 3
#=> 0 1
```

