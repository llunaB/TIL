# ECMA Script 6

- ECMAScript 라고도 불리며 국제표준화기구에서 제안하는 6번째 표준 명세
- 세미콜론을 선택적으로 사용 가능하며, 없을 경우 ASI(Automatic Semicolon Insertion)에 의해 자동 삽입됨.
- 자바스크립트 코딩스타일 가이드
  - Airbnb Javascript Style Guide
  - Google Javascript Style Guide

# variables

> 변수와 식별자

- 식별자란 변수를 구분할 수 있는 변수명으로 숫자로 시작할 수 없다.
- 대소문자를 구분하며 클래스 명 외에는 모두 소문자로 시작한다.

### 작성 스타일

- 카멜 케이스(camelCase) - 변수, 객체, 함수에 사용
- 파스칼 케이스(PascalCase) - 클래스, 생성자에 사용
- 대문자 스네이크 케이스(SNAKE_CASE) - 상수에 사용

```javascript
// 변수
let variableName
// 객체
const UserInfo = { name: 'juan', age: 27 }
// 함수
function onClick () {}

/////////////////
// 클래스
class User {
  ...
}
// 생성자
const good = new User({
  name: '홍길동',
})

/////////////////
//상수
const API_KEY = 'SOMEKEY'
const PI = Math.PI
```

### 선언, 할당, 초기화 차이

```javascript
// 선언
let foo

// 할당
foo = 11

// 선언 + 할당
let bar = 0
```

### const vs. let

- 둘 다 변수 재선언 불가능
- const는 재할당 불가, let은 재할당 가능
- 블록 스코프 (중괄호 내부, 블록 바깥에서 접근 불가)

### var

- 재선언과 재할당 모두 가능

- 호이스팅 특성으로 사용 비권장

  ```javascript
  // this place
  console.log(username) // undefined
  var username = '홍길동'
  ```

  - 호이스팅(hoisting) 이란?
    - 변수를 선언 이전에 참조할 수 있는 현상
    - 자바스크립트 특성상 변수를 초기화할 때, 그 이전에 미리 선언되기 때문
    - 변수 선언 이전의 위치에서 접근시 undefined 반환 

# types-and-operations

> 타입과 연산자

### 데이터 타입

- 크게 원시 타입과 참조 타입으로 분류
- 원시타입 : 숫자, 문자열, 불리언, null, undefined

![image-20211028174542100](/Users/euijinpang/Library/Application Support/typora-user-images/image-20211028174542100.png)

- 참조 타입 : 함수, 배열, 객체

# conditions

# loops

# functions

# arrays

# arrays-advanced

# objects



