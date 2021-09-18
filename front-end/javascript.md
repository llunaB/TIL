# JavaScript

## 표기법

컴퓨터가 하나의 단어를 인식하는 방법

1. dash-case(kebab case)

- html, css

```
the-quick-brown-fox-jumps
```

2. snake_case

- html, css

```
the_quick_brown_fox_jumps
```

3. camelCase

- javascript

```
theQuickBrowmFoxJumps
```

4. PascalCase

- javescript

```
TheQuickBrownFoxJumps
```

** Zero-based Numbering

- 숫자는 0부터 센다

- 숫자 0 은 일요일을 의미, 1은 월요일을 의미



## 주석

```javascript
// 한 줄 메모

/**
 * 여러 줄 메모
 * 1
 * 2
*/ 
```



## 데이터 종류(자료형)

1. 문자데이터 string

![image-20210918182122274](javascript.assets/image-20210918182122274.png)

2. 숫자데이터 number

![image-20210918182317939](javascript.assets/image-20210918182317939.png)

3. 논리데이터 Boolean

![image-20210918182443822](javascript.assets/image-20210918182443822.png)

4. Undefined : 값이 할당되지 않은 상태

![image-20210918182612097](javascript.assets/image-20210918182612097.png)

5. Null : 값이 '의도적으로' 비어있음을 의미

![image-20210918182741984](javascript.assets/image-20210918182741984.png)

6. Object 객체 데이터 : 여러 데이터를 Key:Value 형태로 저장 , user 라는 변수에 담는다.

![image-20210918183007922](javascript.assets/image-20210918183007922.png)

7. Array 배열 데이터

![image-20210918183227024](javascript.assets/image-20210918183227024.png)



## 변수

- 데이터를 저장하고 참조(사용)하는 데이터의 이름

1. let

   - 재사용 가능
   - 재할당 가능

   ![image-20210918184103818](javascript.assets/image-20210918184103818.png)

2. const

   - 재할당 불가

   ![image-20210918184130755](javascript.assets/image-20210918184130755.png)



## 예약어

특별한 의미를 가져 변수나 함수명으로 사용할 수 없는 이름, SyntaxError 발생

- this
- if
- break
- ...



## 함수

특정 동작을 수행할 수 있는 일부 코드의 집합(부분)

![image-20210918190203444](javascript.assets/image-20210918190203444.png)

- `return` 을 통해 데이터를 내보내고, 그 값을 새 변수에 할당하여 사용

![image-20210918190351087](javascript.assets/image-20210918190351087.png)

- 매개변수와 인수
  - 매개변수는 함수 내부에서 사용하는 변수

![image-20210918190708854](javascript.assets/image-20210918190708854.png)

- 기명함수와 익명함수
  - 기명함수는 '함수를 선언한다'
  - 익명함수는 '함수를 표현한다' - 변수에 할당

![image-20210918191133379](javascript.assets/image-20210918191133379.png)

- const 통해 정의한 변수는 추가 재할당이 불가
- 객체 데이터 내부에는 다양한 데이터가 정의되어 있다.
- `속성` 부분에 함수가 할당되어 있으면 그것을 `메소드`라 한다.
  - getName은 함수의 표현, 함수라는 데이터를 할당
  - this 는 this 가 소속되어있는 객체 데이터

![image-20210918192029604](javascript.assets/image-20210918192029604.png)



## 조건문

![image-20210918192230260](javascript.assets/image-20210918192230260.png)

![image-20210918192318015](javascript.assets/image-20210918192318015.png)



## DOM API

- Document Object Model
- Application Programming Interface

> 자바스크립트에서 HTML 를 제어하는 명령들



- 정보구조에 유지하기 위해 `defer` 속성 부여하고 head 태그 내에 넣는다.

  - ```html
    <script defer src="./main.js"></script>
    ```

![image-20210918192938492](javascript.assets/image-20210918192938492.png)

- 상황(이벤트) 발생시 익명함수(핸들러)를 실행

![image-20210918193820262](javascript.assets/image-20210918193820262.png)

- `boxEL` 이라는 요소에서 `class`  라는 전역속성의 정보를 가진 객체 `classList` 를 사용
- `add` , `remove` 라는 메소드 사용

![image-20210918194659327](javascript.assets/image-20210918194659327.png)

- 클릭시 active 클래스가 추가된다.

![image-20210918195203280](javascript.assets/image-20210918195203280.png)

- 배열 `boxELs` 을 반복하는 메서드 `.forEach` 

![image-20210918200346431](javascript.assets/image-20210918200346431.png)

![image-20210918200447555](javascript.assets/image-20210918200447555.png)

- 텍스트 변경

![image-20210918201255930](javascript.assets/image-20210918201255930.png)



## 메소드 체이닝(Method Chaining)

- 메소드를 연결하여 작성

![image-20210918202055618](javascript.assets/image-20210918202055618.png)

