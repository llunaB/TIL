/* comment */
// comment

let espressoPrice;
espressoPrice = 3000;

console.log(espressoPrice)

let lattePrice = 4300;

// 변수명 camelCase

// 함수 선언
function greetings(sentence) {
  console.log('HI!');
  console.log('hihi');
  console.log(sentence);
};

// 함수 호출
greetings('hola');

function welcome(name) {
  console.log('안녕하세요' + name + '님');
};

welcome('의진');

function printSquare(x) {
  console.log(x * x);
};

printSquare(3);

function printSum(num1, num2) {
  console.log(num1 + num2);
};

printSum(10, 5);

function introduce(name, birth, nationality, job) {
  console.log('제 이름은' + name + '입니다.')
};

introduce('jessie')

function getTwo() {
  return 2;
}

console.log(getTwo());

console.log("He said \'I'm here.\'")
console.log(`He said "I'm here."`)

console.log(3 === 3);
console.log(3 !== 3);

// and 연산 - 둘다 true여야 true
console.log(true && true);
console.log(true && false);
console.log(false && true);
console.log(false && false);
// or 연산 - 하나라도 true이면 true
console.log(true || true);
console.log(true || false);
console.log(false || true);
console.log(false || false);
// not 연산
console.log(!true);
console.log(!!false);

// typeof 연산자 - 오른쪽 값의 자료형을 '문자열'로 반환
console.log(typeof 1);
console.log(typeof 'hi');
console.log(typeof 8 - 3); // NaN
console.log(typeof (8 - 3));

// 형변환
console.log(Number('10') + Number('5'));
console.log(String(10) + String(5));
console.log(Number(false)) // 0
console.log(Number(true)) // 1
console.log(Boolean('')) // false  -> ''는 flasy 값
console.log(Boolean('text')) // true
console.log(Boolean(0)) // false
console.log(Boolean(3)) // true
console.log(Boolean(NaN)) // false


// 산술연산 - str 제외하고는 모두 숫자로 변환, NaN은 항상 NaN
console.log(4 + '2'); // 42(str)
console.log('5'/true) // 5 / 1 => 5
console.log(4 + 2);
console.log(4 - true); // 3
console.log(true * true); // 1
console.log(4 * false); // 0
console.log(4 * 'two'); // NaN

// 관계 비교 연산 - 비교 불가시 false 반환
console.log(2 < '3');
console.log(2 > true);
console.log('2' <= false);
console.log('two' >= 1);

// 같음 비교 연산
console.log(1 === '1'); // 일치 - 형변환 x (불일치 !==)
console.log(1 == '1'); // 동등 (일치 !=)

// 템플릿 문자열
let myNumber = 3;
function getTwice(x) {
  return x * 2;
};
console.log(`${myNumber}의 두 배는 ${getTwice(myNumber)}입니다.`)

// null - 의도적으로 값이 없다고 표현하는 것. undefined - 진짜 값이 없다..
let hi;
console.log(hi); // undefined

hi = null
console.log(hi); // null

console.log(null == undefined); // true
console.log(null === undefined); // false

