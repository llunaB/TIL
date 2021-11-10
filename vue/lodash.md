# lodash

https://lodash.com/docs/4.17.15

- array, object 등 자료구조를 다룰 때 사용하는 유용하고 간편한 유틸리티 함수 제공

```vue
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
```

## reverse 역순정렬

```javascript
const array2 = [1 ,2, 3, 4]
const reversedArray2 = _.reverse(array2)
console.log(reversedArray2) // [4, 3, 2, 1]
```

## sortBy 오름차순 정렬

```javascript
const numbers2 = [10, 1, 3, 5, 6]
const sortedNums = _.sortBy(numbers2)
console.log(sortedNums) // [1, 3, 5, 6, 10]
```

## range 범위

```javascript
const num1 = _.range(4)
console.log(num1) // [0, 1, 2, 3]
```

## random 랜덤 1개 뽑기

```javascript
const randomNums = _.random(0, 5)
console.log(randomNums) // 3
```

## sampleSize 랜덤 3개 뽑기

```javascript
const result = _.sampleSize([1, 2, 3, 4, 5, 6, 7, 8], 3)
console.log(result) // [2, 4, 8]
```

