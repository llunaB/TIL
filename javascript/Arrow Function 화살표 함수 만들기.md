**- function 키워드 생략**

**- 함수의 매개변수가 1개라면 () 생략**

**- 함수 몸통이 표현식 하나라면 {}, return 도 생략 가능**



```javascript
const arrow = function (name) {
	return 'hello! &{name}'
}

// 1. function 키워드 삭제
const arrow = (name) => { return 'hello! &{name}' }

// 2. () 생략
const arrow = name => { return 'hello! &{name}' }

// 3. {} & return 생략
const arrow = name => 'hello! &{name}'
```