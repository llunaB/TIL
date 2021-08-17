## 4864. 문자열 비교 : Brute Force Algorithm

```python
TC = int(input())

def find_brute(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)   # introduce convinient notations
    for i in range(n-m+1):  # try every potential stating index within T
        k = 0               # an index into pattern P
        while k < m and T[i+k] == P[k]: # kth character of P matches
            k += 1
        if k == m:          # if we reached the end of pattern,
            return i        # substring T[i:i+m] matches P
    return -1               # failed to find a match string with any i    

for test_case in range(TC):
    str1 = input()
    str2 = input()

    T = str2
    P = str1

    P_idx = find_brute(T, P)
    
    if P_idx == -1:
        result = 0
    else:
        result = 1

    print("#{} {}".format(test_case + 1,P_idx))
```



## 4865. 글자수

- 중복제거하기
- 딕셔너리 활용하기

```python
import sys
sys.stdin = open('input.txt')

TC = int(input())

for test_case in range(TC):
    str1 = input()      # abccc
    str2 = input()      # dsfaggdvasbdc
    set1 = set(str1)    # {'c', 'b', 'a'}
    strboard = ''       # dbaabcc

    for i in range(len(str2)):
        if str2[i] in set1:
            strboard += str2[i]

    board = {
        "A" : 0,
        "B" : 0,
        "C" : 0,
        "D" : 0,
        "E" : 0,
        "F" : 0,
        "G" : 0,
        "H" : 0,
        "I" : 0,
        "J" : 0,
        "K" : 0,
        "L" : 0,
        "M" : 0,
        "N" : 0,
        "O" : 0,
        "P" : 0,
        "Q" : 0,
        "R" : 0,
        "S" : 0,
        "T" : 0,
        "U" : 0,
        "V" : 0,
        "W" : 0,
        "X" : 0,
        "Y" : 0,
        "Z" : 0,
    }

    for char in strboard:
        board[char] += 1

    result_board = list(board.values())

    print("#{} {}".format(test_case + 1, max(result_board)))
```

