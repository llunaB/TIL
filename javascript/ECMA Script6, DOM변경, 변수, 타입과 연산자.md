# ECMA Script 6

- ECMAScript 라고도 불리며 국제표준화기구에서 제안하는 6번째 표준 명세
- 세미콜론을 선택적으로 사용 가능하며, 없을 경우 ASI(Automatic Semicolon Insertion)에 의해 자동 삽입됨.
- 자바스크립트 코딩스타일 가이드
  - Airbnb Javascript Style Guide
  - Google Javascript Style Guide



# DOM 변경 메서드

## Document.createElement()

작성한 태그명의 html 요소 생성하여 반환

## Element.append()

특정 부모 노드의 자식리스트 중 마지막 자식 다음에 노드객체나 스트링을 삽입

반환값 없음

여러 노드 객체와 문자열 추가 가능

## Node.appendChild()

한 Node를 특정 부모 노드의 자식 노드리스트 중 마지막 자식으로 삽입

반환값 있음

하나의 노드 객체만 추가 가능

## Node.innerText

노드 객체와 그 자손의 텍스트 컨텐츠를 표현 => 태그까지 출력

## Element.innerHTML

요소 내 HTML마크업을 반환 => 태그 제외하고 출력(반영)

### XSS(Cross-site Scripting) 주의

태그 포함한 악성 코드를 삽입하여 민감한 정보를 탈취할 수 있다.

## ChildNode.remove()

노드가 속한 트리에서 해당 노드를 제거

## Node.removeChild()

DOM에서 자식 Node를 제거하고 제거된 노드를 반환

## Element.setAttribute(name, value)

## Element.getAttribute(attributeName)





---



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



