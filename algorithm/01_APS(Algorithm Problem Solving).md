# APS(Algorithm Problem Solving)

## 알고리즘

> 어떠한 문제를 해결하기 위한 절차

## 알고리즘 표현방법

- 슈더코드 (Pseudocode)
- 순서도

## 알고리즘 성능 측정방법

### 무엇이 좋은 알고리즘인가?

- 정확성 : 얼마나 정확하게 동작하는가
- **작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가** (연산 횟수가 적을수록 good)
- 메모리 사용량 : 얼마나 적은 메모리를 사용하는가
- 단순성 : 얼마나 단순한가
- 최적성 : 더 이상 개선할 여지없이 최적화되었는가

### 알고리즘의 작업량 표현 - 시간복잡도(Time Complexity) 

- 실제 걸리는 시간을 측정
- 실행되는 명령문의 개수를 계산

### 빅-오(O) 표기법(Big-Oh Notation)

- 시간 복잡도 함수 중 가장 큰 영향력을 주는 n에 대한 항만을 표시
- 계수(Coefficient)는 생략하여 표시

```bash
O(3n+2) = O(3n) = O(n)
O(2n² + 10n + 100) = O(n²)
```

<img src="01. APS(Algorithm Problem Solving).assets/bigOnotation.jpeg">

