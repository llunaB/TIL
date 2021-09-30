# README

---

- 접근방법은 맞았지만 구현하는 과정에서 오류가 존재하였다.

### 오류 1

- 원인
  - 암호비트 패턴은 순서대로 나열되어 있다 하였는데 딕셔너리를 사용하였다. 

- 해결방안
  - 딕셔너리는 순서가 없는 자료형이기 때문에 리스트로 만들어야 한다.



### 오류 2

- 원인 

  - 10진수를 2진수로 변환하는 bit 내장함수를 사용할 경우 앞의 0이 생략되어 출력되기 때문에 4자리로 나오지 않는다.

    ```python
    for i in range(20):
        binary_number = bin(i)
        print(binary_number)
    
    #1  0b0
    #2  0b1
    #3  0b10
    #4  0b11
    #5  0b100
    #6  0b101
    #7  0b110
    #8  0b111
    #9  0b1000
    #10  0b1001
    #11  0b1010
    #12  0b1011
    #13  0b1100
    #14  0b1101
    #15  0b1110
    #16  0b1111
    #17  0b10000
    #18  0b10001
    #19  0b10010
    #20  0b10011
    ```

    

- 해결방안

  - 1) format 함수를 사용한다.

    ```python
    for i in range(20):
        binary_number = format(i, 'b')
        print(binary_number)
        
    0
    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010
    1011
    1100
    1101
    1110
    1111
    10000
    10001
    10010
    10011
    ```

    

### 문제

![image-20210929171337887](/Users/euijinpang/algorithm/0929/README copy.assets/image-20210929171337887.png)

### 답

```python

```

### 내코드 (오류) 0929

```python
## 암호비트
hiddenbit = {
    '0' : '001101',
    '1' : '010011',
    '2' : '111011',
    '3' : '110001',
    '4' : '100011',
    '5' : '110111',
    '6' : '001011',
    '7' : '111101',
    '8' : '011001',
    '9' : '101111',
}

import sys
sys.stdin = open('input.txt')

passkey = ''
for i in list(input()):
    hex = '0x0' + i
    # 1. 16진수를 10진수로 변환
    octal_number = int(hex, 16)
    # 2. 10진수를 2진수로 변환 
    binary_number = bin(octal_number) # 앞에 0 붙이기!!
    binary_number_no_0b = binary_number.split('b')[1]
    passkey += binary_number_no_0b

result = []
# huddenbit 암호비트 딕셔너리 및 passkey 탐색, 일치시 암호반환

passkey = '0000001001101001111110101100100110100000'
## 수정:
i = 0
while i < len(passkey)-5:
    check = passkey[i:i+6]
    for items in hiddenbit.items():
        if items[1] == check:
            result.append(items[0])
            i += 6
    else:
        i += 1

print(f'{result}')

# passkey = 0101101001111110101100100110100
# result = 01178
```

### 맞는 코드

### 수정코드

